#!/usr/bin/env python3
"""Deterministic half of /kb-scrapecontent: find pending URLs, probe them, and close out the run.

  scrape_queue.py probe URL...           probe the given URLs, print JSON
  scrape_queue.py discover [--out FILE]  read raw/url/, drop already-scraped URLs, probe the rest;
                                         writes the queue to FILE (default: a fresh temp dir) and
                                         prints a summary naming it
  scrape_queue.py seen URL...            split URLs into inVault (a source_url in raw/ or wiki/),
                                         failedBefore (named in kbm.log.md, e.g. scrape-failed) and fresh
  scrape_queue.py finalize QUEUE ROWS    append ROWS (JSON list of {filename, activity}) to
                                         kbm.log.md and archive the source files named in QUEUE

Probe verdicts: ok (article text saved to text_path), thin, paywall, blocked, unreachable,
dead (HTTP 404/410). Every URL resolves within TIMEOUT_S, and a whole batch within DEADLINE_S
per 32 URLs, so a stalling site can never hang a run.

Run from the vault root. Standard library only.
"""
import hashlib
import json
import re
import socket
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

TIMEOUT_S = 10
DEADLINE_S = 20
SLOTS = 32
MAX_BYTES = 3_000_000
MAX_TEXT_CHARS = 60_000
THIN_CHARS = 600
TEASER_CHARS = 2_500
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
URL_RE = re.compile(r"https?://[^\s<>\"'`)\]]+")
CHALLENGE_RE = re.compile(
    r"cf-chl-|challenge-platform|<title>\s*(just a moment|attention required|access denied|"
    r"are you a robot|pardon our interruption|security check)|captcha-delivery|px-captcha|"
    r"perimeterx|datadome|_incapsula_|enable javascript and cookies to continue",
    re.I,
)
PAYWALL_RE = re.compile(
    r"subscribe to (continue|read)|to continue reading|already a subscriber|"
    r"this (article|content) is (for|available to) (subscribers|members)|"
    r"create a free account to (continue|read)|sign in to read",
    re.I,
)
LIVE_BLOG_RE = re.compile(r"live-updates|/live/|liveblog", re.I)
DEAD_STATUSES = {404, 410}


@dataclass
class Probe:
    url: str
    verdict: str
    reason: str
    status: int | None = None
    chars: int = 0
    title: str = ""
    author: str = ""
    published: str = ""
    text_path: str | None = None


class _Extract(HTMLParser):
    SKIP = {"script", "style", "noscript", "nav", "header", "footer", "aside", "svg", "button"}
    BLOCK = {"p", "h1", "h2", "h3", "h4", "li", "blockquote", "pre"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.block = None
        self.buf = []
        self.paras = []
        self.loose = []
        self.meta = {}
        self.ld = []
        self.ldbuf = []
        self.in_ld = False
        self.in_title = False
        self.title = ""
        self.time = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta":
            key = (a.get("property") or a.get("name") or "").lower()
            if key and a.get("content"):
                self.meta.setdefault(key, a["content"].strip())
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self.in_ld = True
            self.ldbuf = []
        elif tag == "title":
            self.in_title = True
        elif tag == "time" and a.get("datetime") and not self.time:
            self.time = a["datetime"]
        elif tag == "br":
            self.loose.append("\n")
        if tag in self.SKIP and not self.in_ld:
            self.skip += 1
        elif tag in self.BLOCK and not self.skip:
            self.block = tag
            self.buf = []

    def handle_endtag(self, tag):
        if tag == "script" and self.in_ld:
            self.ld.append("".join(self.ldbuf))
            self.in_ld = False
            return
        if tag == "title":
            self.in_title = False
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        elif tag == self.block:
            text = " ".join("".join(self.buf).split())
            if text:
                self.paras.append(("## " if tag in ("h2", "h3") else "") + text)
            self.block = None

    def handle_data(self, data):
        if self.in_ld:
            self.ldbuf.append(data)
        elif self.skip:
            return
        elif self.block:
            self.buf.append(data)
        elif self.in_title:
            self.title += data
        else:
            self.loose.append(data.replace("\n", " "))


def _ld_objects(blobs):
    for blob in blobs:
        try:
            data = json.loads(blob)
        except ValueError:
            continue
        stack = [data]
        while stack:
            node = stack.pop()
            if isinstance(node, list):
                stack.extend(node)
            elif isinstance(node, dict):
                yield node
                stack.extend(v for k, v in node.items() if k == "@graph")


def _ld_first(objs, key):
    for o in objs:
        v = o.get(key)
        if isinstance(v, list) and v:
            v = v[0]
        if isinstance(v, dict):
            v = v.get("name")
        if v not in (None, ""):
            return v
    return None


def parse(html):
    p = _Extract()
    p.feed(html)
    objs = list(_ld_objects(p.ld))
    free = _ld_first(objs, "isAccessibleForFree")
    text = "\n\n".join(p.paras)
    lines = (" ".join(line.split()) for line in "".join(p.loose).split("\n"))
    loose = "\n\n".join(line for line in lines if line)
    if len(loose) > 3 * len(text):
        # Table/<font> layouts (e.g. paulgraham.com) keep the essay outside <p>; on 484 real
        # article pages this switch fired only for those.
        text = loose
    return {
        "text": text,
        "title": (p.meta.get("og:title") or _ld_first(objs, "headline") or p.title).strip(),
        "author": str(p.meta.get("author") or _ld_first(objs, "author") or "").strip(),
        "published": str(p.meta.get("article:published_time") or _ld_first(objs, "datePublished")
                         or p.time or "")[:10],
        "paywalled": str(free).lower() == "false",
    }


# Ordered: the first matching rule decides the verdict.
RULES = [
    ("dead", lambda s, h, d, u: s in DEAD_STATUSES, "http {status}"),
    ("blocked", lambda s, h, d, u: bool(CHALLENGE_RE.search(h[:20000])), "bot challenge page"),
    ("unreachable", lambda s, h, d, u: s >= 500, "http {status}"),
    ("blocked", lambda s, h, d, u: s >= 400, "http {status}"),
    ("paywall", lambda s, h, d, u: d["paywalled"] and len(d["text"]) < TEASER_CHARS,
     "isAccessibleForFree=false, {chars} chars visible"),
    ("paywall", lambda s, h, d, u: bool(PAYWALL_RE.search(d["text"])) and len(d["text"]) < TEASER_CHARS,
     "subscribe prompt, {chars} chars visible"),
    ("thin", lambda s, h, d, u: bool(LIVE_BLOG_RE.search(u)), "live blog url"),
    ("thin", lambda s, h, d, u: len(d["text"]) < THIN_CHARS, "{chars} chars of text, likely js-rendered"),
    ("ok", lambda s, h, d, u: len(d["text"]) > MAX_TEXT_CHARS, "{chars} chars of text, first %d kept" % MAX_TEXT_CHARS),
    ("ok", lambda s, h, d, u: True, "{chars} chars of text"),
]


def classify(url, status, html):
    d = parse(html)
    for verdict, test, reason in RULES:
        if test(status, html, d, url):
            return verdict, reason.format(status=status, chars=len(d["text"])), d


def _fetch(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_S) as r:
            status, raw, ctype = r.status, r.read(MAX_BYTES), r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        with e:
            status, raw, ctype = e.code, e.read(MAX_BYTES), e.headers.get("Content-Type", "")
    charset = (re.search(r"charset=([\w-]+)", ctype) or [None, "utf-8"])[1]
    try:
        return status, raw.decode(charset, errors="replace"), ctype
    except LookupError:
        return status, raw.decode("utf-8", errors="replace"), ctype


def probe_one(url, outdir):
    try:
        status, html, ctype = _fetch(url)
    except (socket.timeout, TimeoutError):
        return Probe(url, "unreachable", f"no response in {TIMEOUT_S}s")
    except urllib.error.URLError as e:
        # Not "dead": a sandbox without network (e.g. Cowork) fails the same way, and the
        # one remote fallback can still reach the page.
        return Probe(url, "unreachable", f"connection failed: {e.reason}")
    except Exception as e:
        return Probe(url, "unreachable", f"fetch error: {type(e).__name__}: {e}")
    if "pdf" in ctype.lower():
        return Probe(url, "thin", "pdf, not html", status)
    verdict, reason, d = classify(url, status, html)
    p = Probe(url, verdict, reason, status, len(d["text"]), d["title"], d["author"], d["published"])
    if verdict == "ok":
        path = Path(outdir) / (hashlib.sha1(url.encode()).hexdigest()[:12] + ".md")
        head = f"url: {url}\ntitle: {p.title}\nauthor: {p.author}\npublished: {p.published}\n\n"
        path.write_text(head + d["text"][:MAX_TEXT_CHARS])
        p.text_path = str(path)
    return p


def probe_all(urls, outdir=None):
    # Daemon threads, not ThreadPoolExecutor: its workers are joined at exit, so one
    # slow-drip server would hold the process open past the deadline.
    outdir = outdir or tempfile.mkdtemp(prefix="kb-scrape-")
    results = {}
    slots = threading.Semaphore(SLOTS)

    def run(u):
        with slots:
            results[u] = probe_one(u, outdir)

    for u in urls:
        threading.Thread(target=run, args=(u,), daemon=True).start()
    end = time.monotonic() + DEADLINE_S * -(-len(urls) // SLOTS)
    while len(results) < len(urls) and time.monotonic() < end:
        time.sleep(0.1)
    return [results.get(u) or Probe(u, "unreachable", f"probe exceeded {DEADLINE_S}s") for u in urls]


def scraped_urls(root):
    seen = set()
    for sub in ("raw", "wiki"):
        for f in (root / sub).rglob("*.md"):
            seen.update(re.findall(r"source_url:\s*(\S+)", f.read_text(errors="replace")))
    return seen


def find_urls(text):
    return list(dict.fromkeys(u.rstrip(".,;:*") for u in URL_RE.findall(text)))


def pending_urls(root):
    files = sorted(f for f in (root / "raw" / "url").glob("*.md") if not f.name.endswith(".processed.md"))
    return [str(f.relative_to(root)) for f in files], find_urls("\n".join(f.read_text(errors="replace") for f in files))


def seen(root, urls):
    in_vault = scraped_urls(root)
    logged = set(find_urls((root / "kbm.log.md").read_text(errors="replace")))
    urls = find_urls(" ".join(urls))
    return {
        "inVault": [u for u in urls if u in in_vault],
        "failedBefore": [u for u in urls if u not in in_vault and u in logged],
        "fresh": [u for u in urls if u not in in_vault and u not in logged],
    }


def discover(root, outdir):
    source_files, urls = pending_urls(root)
    seen = scraped_urls(root)
    fresh = [u for u in urls if u not in seen]
    probes = probe_all(fresh, outdir)
    return {
        "date": date.today().isoformat(),
        "sourceFiles": source_files,
        "alreadyScraped": [u for u in urls if u in seen],
        "items": [asdict(p) for p in probes],
    }


def finalize(root, queue, rows):
    log = root / "kbm.log.md"
    today = date.today().isoformat()
    existing = set(log.read_text().splitlines())
    lines = [f"| {today} | {re.sub(r'[|\n]', '/', r['filename'])} | {r['activity']} |" for r in rows]
    for src in queue["sourceFiles"]:
        path = root / src
        done = path.with_name(path.name[: -len(".md")] + ".processed.md")
        if path.exists():
            path.rename(done)
        lines.append(f"| {today} | {done.name} | archive |")
    new = [line for line in lines if line not in existing]
    if new:
        text = log.read_text()
        log.write_text(text + ("" if text.endswith("\n") else "\n") + "\n".join(new) + "\n")
    return {"appended": len(new), "skipped_existing": len(lines) - len(new)}


def main(argv):
    cmd, args = (argv[0], argv[1:]) if argv else ("", [])
    root = Path.cwd()
    if cmd == "probe" and args:
        out = [asdict(p) for p in probe_all(args)]
    elif cmd == "discover":
        path = Path(args[args.index("--out") + 1]) if "--out" in args else \
            Path(tempfile.mkdtemp(prefix="kb-scrape-")) / "queue.json"
        queue = discover(root, path.parent)
        path.write_text(json.dumps(queue, indent=1))
        items = queue["items"]
        out = {"queue": str(path), "toScrape": len(items), "alreadyScraped": len(queue["alreadyScraped"]),
               "verdicts": {v: sum(i["verdict"] == v for i in items) for v in sorted({i["verdict"] for i in items})}}
    elif cmd == "seen" and args:
        out = seen(root, args)
    elif cmd == "finalize" and len(args) == 2:
        out = finalize(root, json.loads(Path(args[0]).read_text()), json.loads(Path(args[1]).read_text()))
    else:
        sys.exit(__doc__)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main(sys.argv[1:])

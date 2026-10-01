#!/usr/bin/env python3
"""Measure where scrape agents spend time per URL, from Claude Code transcripts.

Usage: forensics.py [--since YYYY-MM-DD] [--detail] [--labels out.json] [transcript_root ...]
Defaults to every ~/.claude/projects/*Developer-kb* and *PARA-kb* directory (this vault).
"""
import glob
import json
import os
import re
import sys
from collections import defaultdict
from datetime import datetime

FETCH_TOOLS = {
    "WebFetch",
    "mcp__tavily__tavily_extract",
    "mcp__tavily__tavily_crawl",
    "mcp__serper-search__scrape",
    "mcp__tavily__tavily_search",
    "mcp__serper-search__google_search",
}
URL_RE = re.compile(r"https?://[^\s\"'\\)\]]+")
BLOCK_RE = re.compile(
    r"403|401|429|451|forbidden|access denied|captcha|cloudflare|just a moment|"
    r"enable javascript|are you a robot|bot detection|permission_error|paywall|"
    r"subscribe to (continue|read)|failed to scrape|scraping failed|"
    r"unable to fetch|blocked",
    re.I,
)


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def first_user_text(rows):
    for o in rows:
        m = o.get("message")
        if o.get("type") == "user" and isinstance(m, dict):
            c = m.get("content")
            if isinstance(c, str):
                return c
            if isinstance(c, list):
                for b in c:
                    if b.get("type") == "text":
                        return b["text"]
    return ""


def is_scrape_transcript(rows):
    head = first_user_text(rows)[:400].lower()
    return "web scraping agent" in head or "kb-scrapecontent" in head


def urls_in(inp):
    return sorted(set(URL_RE.findall(json.dumps(inp))))


def result_text(block):
    c = block.get("content")
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return " ".join(b.get("text", "") for b in c if isinstance(b, dict))
    return ""


def analyze(path):
    rows = [json.loads(l) for l in open(path) if l.strip()]
    if not rows or not is_scrape_transcript(rows):
        return None
    pending = {}
    calls = []
    saved = set()
    stamps = [ts(o["timestamp"]) for o in rows if o.get("timestamp")]
    for o in rows:
        m = o.get("message")
        if not isinstance(m, dict) or not isinstance(m.get("content"), list):
            continue
        for b in m["content"]:
            if b.get("type") == "tool_use" and b["name"] == "Write":
                hit = re.search(r"source_url:\s*(\S+)", b["input"].get("content", ""))
                if hit:
                    saved.add(hit.group(1))
            if b.get("type") == "tool_use":
                pending[b["id"]] = (b["name"], b["input"], ts(o["timestamp"]))
            elif b.get("type") == "tool_result" and b.get("tool_use_id") in pending:
                name, inp, t0 = pending.pop(b["tool_use_id"])
                text = result_text(b)
                calls.append(
                    {
                        "tool": name,
                        "urls": urls_in(inp) if name in FETCH_TOOLS or name == "Bash" else [],
                        "secs": (ts(o["timestamp"]) - t0).total_seconds(),
                        "bytes": len(text),
                        "error": bool(b.get("is_error")),
                        "blocked": bool(BLOCK_RE.search(text[:2000])) and len(text) < 3000,
                        "t0": t0,
                    }
                )
    for name, inp, t0 in pending.values():
        calls.append({"tool": name, "urls": urls_in(inp), "secs": None, "bytes": 0,
                      "error": True, "blocked": False, "t0": t0})
    wall = (max(stamps) - min(stamps)).total_seconds() if stamps else 0
    return {"path": path, "start": min(stamps) if stamps else None, "wall": wall, "calls": calls,
            "saved": saved}


def per_url(run):
    by = defaultdict(list)
    for c in run["calls"]:
        if c["tool"] in FETCH_TOOLS or (c["tool"] == "Bash" and c["urls"]):
            for u in c["urls"]:
                by[u].append(c)
    out = {}
    for u, cs in by.items():
        cs.sort(key=lambda c: c["t0"])
        span = (cs[-1]["t0"] - cs[0]["t0"]).total_seconds() + (cs[-1]["secs"] or 0)
        out[u] = {
            "saved": u in run["saved"],
            "attempts": len(cs),
            "tools": [c["tool"].replace("mcp__", "").split("__")[-1] for c in cs],
            "blocked_hits": sum(c["blocked"] or c["error"] for c in cs),
            "span": span,
            "hung": any(c["secs"] is None for c in cs),
            "max_call": max((c["secs"] or 0) for c in cs),
        }
    return out


def main(argv):
    since = labels_out = None
    detail = "--detail" in argv
    args = [a for a in argv if a != "--detail"]
    if "--since" in args:
        i = args.index("--since")
        since = args[i + 1]
        del args[i : i + 2]
    if "--labels" in args:
        i = args.index("--labels")
        labels_out = args[i + 1]
        del args[i : i + 2]
    roots = args or glob.glob(os.path.expanduser("~/.claude/projects/*Developer-kb*")) + glob.glob(
        os.path.expanduser("~/.claude/projects/*PARA-kb*"))
    files = [f for r in roots for f in glob.glob(os.path.join(r, "**", "*.jsonl"), recursive=True)]
    runs = [r for r in map(analyze, files) if r and r["start"]]
    if since:
        runs = [r for r in runs if r["start"].strftime("%Y-%m-%d") >= since]
    runs.sort(key=lambda r: r["start"])

    all_urls = []
    labels = {}
    for r in runs:
        pu = per_url(r)
        all_urls.extend(pu.values())
        for u, s in pu.items():
            prev = labels.get(u, {"saved": False, "blocked_hits": 0, "attempts": 0, "span": 0})
            labels[u] = {"saved": prev["saved"] or s["saved"],
                         "blocked_hits": prev["blocked_hits"] + s["blocked_hits"],
                         "attempts": prev["attempts"] + s["attempts"],
                         "span": prev["span"] + s["span"]}
        if detail:
            print(f"\n## {r['start']:%Y-%m-%d %H:%M} wall={r['wall']:.0f}s {os.path.basename(r['path'])}")
            for u, s in sorted(pu.items(), key=lambda kv: -kv[1]["span"]):
                flag = "HUNG " if s["hung"] else ("BLOCK" if s["blocked_hits"] else "     ")
                print(f"  {flag} att={s['attempts']:<2} span={s['span']:>5.0f}s max={s['max_call']:>5.0f}s "
                      f"{','.join(s['tools'])[:60]:<60} {u[:90]}")

    blocked = [s for s in all_urls if s["blocked_hits"]]
    clean = [s for s in all_urls if not s["blocked_hits"]]
    calls = [c for r in runs for c in r["calls"] if c["tool"] in FETCH_TOOLS]
    tool_secs = defaultdict(list)
    for c in calls:
        if c["secs"] is not None:
            tool_secs[c["tool"]].append(c["secs"])

    def med(xs):
        xs = sorted(xs)
        return xs[len(xs) // 2] if xs else 0

    print(f"\nscrape runs: {len(runs)}  urls: {len(all_urls)}  fetch calls: {len(calls)}")
    print(f"urls that hit a block/error: {len(blocked)}")
    if blocked:
        print(f"  attempts per blocked url: median={med([s['attempts'] for s in blocked])} "
              f"max={max(s['attempts'] for s in blocked)}")
        print(f"  seconds per blocked url:  median={med([s['span'] for s in blocked]):.0f} "
              f"max={max(s['span'] for s in blocked):.0f}")
    if clean:
        print(f"clean urls: attempts median={med([s['attempts'] for s in clean])} "
              f"seconds median={med([s['span'] for s in clean]):.0f}")
    blocked_lost = [s for s in blocked if not s["saved"]]
    print(f"  of those, eventually saved anyway: {len(blocked) - len(blocked_lost)}  never saved: {len(blocked_lost)}")
    if blocked_lost:
        print(f"  seconds burned on never-saved blocked urls: total={sum(s['span'] for s in blocked_lost):.0f} "
              f"max={max(s['span'] for s in blocked_lost):.0f}")
    print(f"hung calls (tool_use with no result): {sum(1 for c in calls if c['secs'] is None)}")
    if labels_out:
        json.dump(labels, open(labels_out, "w"), indent=1, sort_keys=True)
        print(f"wrote {len(labels)} labelled urls to {labels_out}")
    print("per-tool call latency (median / max seconds, n):")
    for t, xs in sorted(tool_secs.items()):
        print(f"  {t:<40} {med(xs):>6.1f} / {max(xs):>6.1f}  n={len(xs)}")


if __name__ == "__main__":
    main(sys.argv[1:])

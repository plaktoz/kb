#!/usr/bin/env python3
"""Search wiki notes (or topic files) for terms and print matches in rank order.

  vault_search.py TERM... [--category C] [--since D] [--until D] [--limit N] [--topics]

  --category C   search only wiki/C/
  --since D      keep notes whose date_consumed is on or after D (YYYY-MM-DD)
  --until D      keep notes whose date_consumed is on or before D (YYYY-MM-DD)
  --limit N      print at most N notes; total still counts every match
  --topics       search topics/*.md instead of wiki/ (not combinable with the three filters above)

Each TERM is one term. A term with spaces, hyphens or underscores is a phrase whose words may be
joined by any run of those, so "spaced repetition" matches spaced-repetition and spaced_repetition.
Matching is case-insensitive, needs a word boundary on both ends (no letter or digit adjacent) and
allows a plural s or es, so agent matches agents but sti does not match still. A term is looked for
in the filename stem, each frontmatter tag, and the body after the frontmatter. Paths with an
archived directory are skipped. When --since or --until is given, notes without date_consumed are
dropped.

Output is {"total", "notes": [{path, title, date_consumed, tags, matched, terms}]}. matched lists
the fields any term hit, in the order filename, tags, body; terms lists the terms that hit anything.
Notes rank, each step descending, by distinct terms hit in the filename, then in filename or tags,
then anywhere, then total body occurrences, then date_consumed (undated last), then path ascending.

Run from the vault root. Standard library only.
"""
import json
import re
import sys
from datetime import date
from pathlib import Path
from typing import NamedTuple, Optional

FIELDS = ("filename", "tags", "body")
FRONT_RE = re.compile(r"\A---[ \t]*\n(.*?)^---[ \t]*$\n?", re.S | re.M)
DATE_CONSUMED_RE = re.compile(r"^date_consumed:\s*['\"]?(\d{4}-\d{2}-\d{2})", re.M)
TAGS_RE = re.compile(r"^tags:[ \t]*(.*)$((?:\n[ \t]*-[ \t].*)*)", re.M)
TITLE_RE = re.compile(r"^# (.+)$", re.M)


class Term(NamedTuple):
    text: str
    pattern: re.Pattern


class Note(NamedTuple):
    path: str
    stem: str
    title: str
    date_consumed: Optional[str]
    tags: list
    body: str


def compile_term(text):
    words = [w for w in re.split(r"[\s_-]+", text) if w]
    if not words:
        sys.exit(f"empty term {text!r}")
    phrase = r"[\s_-]+".join(re.escape(w) for w in words)
    return Term(text, re.compile(rf"(?<![a-z0-9]){phrase}(?:e?s)?(?![a-z0-9])", re.I))


def parse_tags(front):
    m = TAGS_RE.search(front)
    if not m:
        return []
    inline, block = m.group(1).strip(), m.group(2)
    items = inline.strip("[]").split(",") if inline else re.findall(r"^[ \t]*-[ \t]+(.*)$", block, re.M)
    return [t for t in (i.strip().strip("'\"") for i in items) if t]


def load(root, path):
    text = path.read_text(errors="replace")
    m = FRONT_RE.match(text)
    front, body = (m.group(1), text[m.end():]) if m else ("", text)
    consumed = DATE_CONSUMED_RE.search(front)
    title = TITLE_RE.search(body)
    return Note(path.relative_to(root).as_posix(), path.stem,
                title.group(1).strip() if title else path.stem,
                consumed and consumed.group(1), parse_tags(front), body)


def candidates(root, category, topics):
    if topics:
        paths = (root / "topics").glob("*.md")
    else:
        base = root / "wiki" / category if category else root / "wiki"
        if not base.is_dir():
            sys.exit(f"no such category directory: {base.relative_to(root).as_posix()}/")
        paths = base.rglob("*.md")
    return sorted(p for p in paths if p.is_file() and "archived" not in p.relative_to(root).parts[:-1])


def hits(note, terms):
    fields = {name: set() for name in FIELDS}
    body_count = 0
    for term in terms:
        if term.pattern.search(note.stem):
            fields["filename"].add(term.text)
        if any(term.pattern.search(tag) for tag in note.tags):
            fields["tags"].add(term.text)
        found = len(term.pattern.findall(note.body))
        if found:
            fields["body"].add(term.text)
            body_count += found
    hit = set().union(*fields.values())
    if not hit:
        return None
    return {
        "rank": (len(fields["filename"]), len(fields["filename"] | fields["tags"]), len(hit), body_count,
                 note.date_consumed is not None, note.date_consumed or ""),
        "out": {"path": note.path, "title": note.title, "date_consumed": note.date_consumed,
                "tags": note.tags, "matched": [f for f in FIELDS if fields[f]],
                "terms": [t.text for t in terms if t.text in hit]},
    }


def search(root, terms, category=None, since=None, until=None, limit=None, topics=False):
    found = []
    for path in candidates(root, category, topics):
        note = load(root, path)
        if since or until:
            if not note.date_consumed or (since and note.date_consumed < since) \
                    or (until and note.date_consumed > until):
                continue
        if hit := hits(note, terms):
            found.append(hit)
    found.sort(key=lambda h: h["out"]["path"])
    found.sort(key=lambda h: h["rank"], reverse=True)
    return {"total": len(found), "notes": [h["out"] for h in found[:limit]]}


def _iso(text, what):
    try:
        return date.fromisoformat(text).isoformat()
    except ValueError:
        sys.exit(f"{what} must be YYYY-MM-DD, got {text!r}")


def _limit(text):
    if not text.isdigit():
        sys.exit(f"--limit must be a non-negative integer, got {text!r}")
    return int(text)


def main(argv):
    opts, terms, args = {}, [], iter(argv)
    for arg in args:
        if arg in ("--category", "--since", "--until", "--limit"):
            opts[arg] = next(args, None)
            if opts[arg] is None:
                sys.exit(__doc__)
        elif arg == "--topics":
            opts[arg] = True
        elif arg.startswith("--"):
            sys.exit(__doc__)
        else:
            terms.append(arg)
    if not terms or ("--topics" in opts and opts.keys() & {"--category", "--since", "--until"}):
        sys.exit(__doc__)
    since, until, limit = opts.get("--since"), opts.get("--until"), opts.get("--limit")
    out = search(Path.cwd(), [compile_term(t) for t in dict.fromkeys(terms)],
                 category=opts.get("--category", "").strip("/") or None,
                 since=since and _iso(since, "--since"), until=until and _iso(until, "--until"),
                 limit=limit and _limit(limit), topics="--topics" in opts)
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1:])

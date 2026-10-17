#!/usr/bin/env python3
"""Read, append to and reconcile kbm.log.md, so skills never parse the log by hand.

  kb_log.py append DATE FILE ACTIVITY       append one row
  kb_log.py append --rows ROWS.json         append a JSON list of {date?, file, activity} rows
                                            (date defaults to today; ROWS.json may be - for stdin)
  kb_log.py rows [--activity A[,B]] [--since D] [--until D]
                                            list matching rows as {date, file, activity, note, path},
                                            in log order, keeping only the latest row per wiki note
                                            (or per File cell, for rows that name no live note)
  kb_log.py week [DATE]                     ISO week of DATE (default today): {year, week, monday, sunday}
  kb_log.py reconcile [--dry-run]           drop blank lines inside the table, append an ingest row for
                                            every wiki note no ingest or ingest-dupe row points to (dated by
                                            its date_consumed, else the commit that added it, else today),
                                            and report ingest rows whose note no longer exists

A row's activity is the first word of its Activity cell; any words after it are its note. A row's
path is the live wiki note (outside wiki/archived/) its File cell names: the cell's first word if
that is such a note's path, else the one live note with that basename, else null. append rejects
an activity not in ACTIVITIES and skips rows already in the log. Neither append nor reconcile
rewrites an existing row, so every command is safe to rerun.

Run from the vault root. Standard library only.
"""
import json
import re
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path
from typing import NamedTuple

LOG = Path("kbm.log.md")
HEADER = "| Date | File | Activity |"
ACTIVITIES = (
    "ingest", "ingest-dupe", "scrape", "scrape-failed", "scrape-dupe", "news-fetch", "newsletter",
    "compound", "delete", "reorg", "research", "lessons", "canvas", "archive", "librarian",
)
INGESTS = ("ingest", "ingest-dupe")
DATE_CONSUMED_RE = re.compile(r"^date_consumed:\s*['\"]?(\d{4}-\d{2}-\d{2})", re.M)


class Row(NamedTuple):
    date: str
    file: str
    activity: str
    note: str


def parse_line(line):
    if not line.startswith("|"):
        return None
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) < 3 or cells[0] == "Date" or set(cells[0]) <= set("-: "):
        return None
    activity, _, note = cells[-1].partition(" ")
    return Row(cells[0], "|".join(cells[1:-1]).strip(), activity, note.strip())


def parse(text):
    return [row for line in text.splitlines() if (row := parse_line(line))]


class Wiki:
    def __init__(self, root):
        self.root = root
        self.live = sorted(p.relative_to(root).as_posix() for p in (root / "wiki").rglob("*.md")
                           if p.relative_to(root / "wiki").parts[0] != "archived")
        self.live_set = set(self.live)
        self.by_name = {}
        for path in self.live:
            self.by_name.setdefault(path.rsplit("/", 1)[-1], []).append(path)

    def resolve(self, file):
        token = file.split(" ", 1)[0]
        if token in self.live_set:
            return token
        name = token.rstrip("/").rsplit("/", 1)[-1]
        found = self.by_name.get(name if name.endswith(".md") else name + ".md", [])
        return found[0] if len(found) == 1 else None


def _iso(text, what):
    try:
        return date.fromisoformat(text).isoformat()
    except ValueError:
        sys.exit(f"{what} must be YYYY-MM-DD, got {text!r}")


def _cell(text):
    return re.sub(r"\s*[\r\n]+\s*", " ", str(text)).replace("|", "/").strip()


def _activities(names):
    bad = [a for a in names if a not in ACTIVITIES]
    if bad:
        sys.exit(f"unknown activity {', '.join(bad)}; valid: {', '.join(ACTIVITIES)}")
    return names


def render(rows):
    today = date.today().isoformat()
    _activities([r["activity"] for r in rows])
    return [f"| {_iso(r.get('date') or today, 'date')} | {_cell(r['file'])} | {r['activity']} |" for r in rows]


def insert_lines(text, new):
    lines = text.splitlines()
    table = [i for i, line in enumerate(lines) if line.startswith("|")]
    if not table:
        lines += ["", HEADER] if lines else [HEADER]
        table = [len(lines) - 1]
    at = table[-1] + 1
    return "\n".join(lines[:at] + new + lines[at:]) + "\n"


def append(root, rows):
    log = root / LOG
    text = log.read_text() if log.exists() else "# KBM Activity Log\n"
    existing = {line.strip() for line in text.splitlines()}
    new = [line for line in dict.fromkeys(render(rows)) if line not in existing]
    if new:
        log.write_text(insert_lines(text, new))
    return {"appended": len(new), "skipped_existing": len(rows) - len(new)}


def rows(root, activities=None, since=None, until=None):
    wiki = Wiki(root)
    latest = {}
    for row in parse((root / LOG).read_text(errors="replace")):
        if activities and row.activity not in activities:
            continue
        if (since or until) and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", row.date):
            continue
        if (since and row.date < since) or (until and row.date > until):
            continue
        path = wiki.resolve(row.file)
        key = path or row.file
        latest.pop(key, None)
        latest[key] = {**row._asdict(), "path": path}
    return list(latest.values())


def week(day):
    year, number, weekday = day.isocalendar()
    monday = day - timedelta(days=weekday - 1)
    return {"year": year, "week": number, "monday": monday.isoformat(),
            "sunday": (monday + timedelta(days=6)).isoformat()}


def ingest_date(root, path):
    m = DATE_CONSUMED_RE.search((root / path).read_text(errors="replace"))
    if m:
        return m.group(1)
    added = subprocess.run(["git", "log", "--diff-filter=A", "--format=%as", "-1", "--", path],
                           cwd=root, capture_output=True, text=True).stdout.strip()
    return added or None


def reconcile(root, dry_run=False):
    log = root / LOG
    lines = log.read_text().splitlines()
    table = [i for i, line in enumerate(lines) if line.startswith("|")]
    inside = range(table[0], table[-1] + 1) if table else range(0)
    blank = {i for i in inside if not lines[i].strip()}
    kept = [line for i, line in enumerate(lines) if i not in blank]

    wiki = Wiki(root)
    logged = parse("\n".join(kept))
    resolved = {wiki.resolve(r.file) for r in logged if r.activity in INGESTS}
    today = date.today().isoformat()
    unlogged = [{"date": ingest_date(root, path) or today, "file": path, "activity": "ingest"}
                for path in wiki.live if path not in resolved]
    missing = [{"date": r.date, "file": r.file} for r in logged
               if r.activity == "ingest" and wiki.resolve(r.file) is None]

    new = render(unlogged)
    if not dry_run and (blank or new):
        log.write_text(insert_lines("\n".join(kept) + "\n", new))
    return {"dry_run": dry_run, "blank_lines_removed": len(blank), "ingest_rows_appended": len(new),
            "missing_count": len(missing), "missing": missing}


def _flag(args, name):
    if name not in args:
        return None
    i = args.index(name) + 1
    if i >= len(args):
        sys.exit(__doc__)
    return args[i]


def main(argv):
    cmd, args = (argv[0], argv[1:]) if argv else ("", [])
    root = Path.cwd()
    if cmd == "append" and args[:1] == ["--rows"] and len(args) == 2:
        source = sys.stdin.read() if args[1] == "-" else Path(args[1]).read_text()
        out = append(root, json.loads(source))
    elif cmd == "append" and len(args) == 3:
        out = append(root, [{"date": args[0], "file": args[1], "activity": args[2]}])
    elif cmd == "rows":
        activity = _flag(args, "--activity")
        since, until = _flag(args, "--since"), _flag(args, "--until")
        out = rows(root, _activities(activity.split(",")) if activity else None,
                   since and _iso(since, "--since"), until and _iso(until, "--until"))
    elif cmd == "week" and len(args) <= 1:
        out = week(date.fromisoformat(_iso(args[0], "DATE")) if args else date.today())
    elif cmd == "reconcile" and args in ([], ["--dry-run"]):
        out = reconcile(root, dry_run=bool(args))
    else:
        sys.exit(__doc__)
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main(sys.argv[1:])

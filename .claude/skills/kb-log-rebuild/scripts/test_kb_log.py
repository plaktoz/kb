import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import kb_log

SCRIPT = Path(__file__).parent / "kb_log.py"
TODAY = date.today().isoformat()


class VaultTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        for sub in ("wiki/finance", "wiki/health", "wiki/archived"):
            (self.root / sub).mkdir(parents=True)
        self.note("wiki/finance/fed-cuts.md", "2026-10-01")
        self.note("wiki/health/sleep.md", "2026-10-02")
        self.note("wiki/archived/old.md", "2026-01-01")
        self.write_log(
            "| 2026-10-01 | wiki/finance/fed-cuts.md | ingest |",
            "| 2026-10-02 | sleep.md | ingest |",
            "| 2026-10-03 | wiki/finance/fed-cuts.md (merged update) | ingest |",
            "| 2026-10-04 | wiki/technology/gone.md | ingest |",
            "| 2026-10-04 | wiki/health/sleep.md (identical source_url, no new info) "
            "| ingest-dupe (same study as existing note) |",
            "| 2026-10-05 | 2026-10-05-news.md | news-fetch |",
        )

    def note(self, path, consumed=None):
        front = f"---\ndate_consumed: {consumed}\n---\n" if consumed else "---\n---\n"
        (self.root / path).write_text(front + "# Note\n")

    def write_log(self, *lines, header="# KBM Activity Log\n\n| Date | File | Activity |\n"):
        (self.root / "kbm.log.md").write_text(header + "".join(line + "\n" for line in lines))

    def log(self):
        return (self.root / "kbm.log.md").read_text()

    def cli(self, *args, check=True):
        return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=self.root,
                              capture_output=True, text=True, check=check)

    def test_append_rejects_unknown_activity_and_leaves_log_alone(self):
        before = self.log()
        out = self.cli("append", "2026-10-06", "wiki/finance/fed-cuts.md", "ingested", check=False)
        self.assertNotEqual(out.returncode, 0)
        self.assertIn("unknown activity ingested", out.stderr)
        self.assertEqual(self.log(), before)

    def test_append_is_idempotent_and_sanitizes_cells(self):
        rows = [{"file": "wiki/finance/fed-cuts.md (a | b\nc)", "activity": "ingest"},
                {"date": "2026-10-06", "file": "daily-update/2026-10/2026-10-06.md", "activity": "newsletter"}]
        rows_file = self.root / "rows.json"
        rows_file.write_text(json.dumps(rows))
        first = json.loads(self.cli("append", "--rows", str(rows_file)).stdout)
        once = self.log()
        second = json.loads(self.cli("append", "--rows", str(rows_file)).stdout)
        self.assertEqual((first["appended"], second["appended"], second["skipped_existing"]), (2, 0, 2))
        self.assertEqual(self.log(), once)
        self.assertTrue(once.endswith(
            f"| {TODAY} | wiki/finance/fed-cuts.md (a / b c) | ingest |\n"
            "| 2026-10-06 | daily-update/2026-10/2026-10-06.md | newsletter |\n"))

    def test_append_goes_after_the_last_table_line(self):
        (self.root / "kbm.log.md").write_text(self.log() + "\nTrailing prose.\n")
        kb_log.append(self.root, [{"date": "2026-10-06", "file": "x.md", "activity": "scrape"}])
        self.assertIn("| 2026-10-05 | 2026-10-05-news.md | news-fetch |\n"
                      "| 2026-10-06 | x.md | scrape |\n\nTrailing prose.\n", self.log())

    def test_rows_resolve_paths_split_notes_and_keep_latest_per_note(self):
        got = json.loads(self.cli("rows", "--activity", "ingest,ingest-dupe").stdout)
        self.assertEqual([(r["date"], r["path"], r["activity"], r["note"]) for r in got], [
            ("2026-10-03", "wiki/finance/fed-cuts.md", "ingest", ""),
            ("2026-10-04", None, "ingest", ""),
            ("2026-10-04", "wiki/health/sleep.md", "ingest-dupe", "(same study as existing note)"),
        ])

    def test_rows_resolve_bare_basename_with_or_without_extension(self):
        self.write_log("| 2026-10-02 | sleep.md | ingest |", "| 2026-10-02 | fed-cuts | ingest |",
                       "| 2026-10-02 | old.md | ingest |")
        self.assertEqual([r["path"] for r in kb_log.rows(self.root)],
                         ["wiki/health/sleep.md", "wiki/finance/fed-cuts.md", None])

    def test_rows_filter_by_date_range(self):
        got = kb_log.rows(self.root, ("ingest",), since="2026-10-02", until="2026-10-03")
        self.assertEqual([(r["date"], r["file"]) for r in got],
                         [("2026-10-02", "sleep.md"), ("2026-10-03", "wiki/finance/fed-cuts.md (merged update)")])

    def test_week_spans_iso_year_boundary(self):
        self.assertEqual(json.loads(self.cli("week", "2027-01-01").stdout),
                         {"year": 2026, "week": 53, "monday": "2026-12-28", "sunday": "2027-01-03"})

    def test_reconcile_removes_blank_lines_backfills_and_reports_missing(self):
        self.note("wiki/health/unlogged.md", "2026-09-30")
        self.write_log("| 2026-10-01 | wiki/finance/fed-cuts.md | ingest |", "",
                       "| 2026-10-02 | wiki/health/sleep.md | ingest-dupe |", "",
                       "| 2026-10-04 | wiki/technology/gone.md | ingest |")
        out = kb_log.reconcile(self.root)
        self.assertEqual((out["blank_lines_removed"], out["ingest_rows_appended"]), (2, 1))
        self.assertEqual(out["missing"], [{"date": "2026-10-04", "file": "wiki/technology/gone.md"}])
        self.assertEqual(self.log(), "# KBM Activity Log\n\n| Date | File | Activity |\n"
                         "| 2026-10-01 | wiki/finance/fed-cuts.md | ingest |\n"
                         "| 2026-10-02 | wiki/health/sleep.md | ingest-dupe |\n"
                         "| 2026-10-04 | wiki/technology/gone.md | ingest |\n"
                         "| 2026-09-30 | wiki/health/unlogged.md | ingest |\n")

    def test_reconcile_dry_run_writes_nothing(self):
        self.write_log("| 2026-10-01 | wiki/finance/fed-cuts.md | ingest |", "")
        before = self.log()
        out = json.loads(self.cli("reconcile", "--dry-run").stdout)
        self.assertEqual((out["blank_lines_removed"], out["ingest_rows_appended"]), (0, 1))
        self.assertEqual(self.log(), before)

    def test_reconcile_second_run_is_a_no_op(self):
        self.note("wiki/health/undated.md")
        self.write_log("| 2026-10-01 | wiki/finance/fed-cuts.md | ingest |", "", "| 2026-10-02 | x.md | scrape |")
        first = kb_log.reconcile(self.root)
        after_first = self.log()
        second = kb_log.reconcile(self.root)
        self.assertEqual((first["blank_lines_removed"], first["ingest_rows_appended"]), (1, 2))
        self.assertEqual((second["blank_lines_removed"], second["ingest_rows_appended"]), (0, 0))
        self.assertEqual(self.log(), after_first)
        self.assertIn(f"| {TODAY} | wiki/health/undated.md | ingest |", after_first)

    def test_activities_match_claude_md(self):
        claude_md = Path(__file__).resolve().parents[4] / "CLAUDE.md"
        line = next(l for l in claude_md.read_text().splitlines() if l.startswith("Valid activity values"))
        self.assertEqual(tuple(line.split(":", 1)[1].replace("`", "").replace(",", " ").split()),
                         kb_log.ACTIVITIES)


if __name__ == "__main__":
    unittest.main()

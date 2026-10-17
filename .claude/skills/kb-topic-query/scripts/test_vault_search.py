import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).parent / "vault_search.py"


class VaultSearchTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        for sub in ("wiki/finance", "wiki/learning", "wiki/archived", "topics"):
            (self.root / sub).mkdir(parents=True)

    def note(self, path, body="", consumed=None, tags=None, block_tags=None):
        front = ["---", "type: article", "source_url: https://example.com/agent-sti-still"]
        if tags is not None:
            front.append(f"tags: [{', '.join(tags)}]")
        if block_tags is not None:
            front += ["tags:", *(f"  - {t}" for t in block_tags)]
        if consumed:
            front.append(f"date_consumed: {consumed}")
        (self.root / path).parent.mkdir(parents=True, exist_ok=True)
        (self.root / path).write_text("\n".join(front + ["---", "", body, ""]))

    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], cwd=self.root,
                              capture_output=True, text=True)

    def search(self, *args):
        out = self.run_cli(*args)
        self.assertEqual(out.returncode, 0, out.stderr)
        return json.loads(out.stdout)

    def paths(self, *args):
        return [n["path"] for n in self.search(*args)["notes"]]

    def test_phrase_matches_hyphenated_filename_and_spaced_body_but_not_words_apart(self):
        self.note("wiki/learning/spaced-repetition-basics.md", "Review cards.")
        self.note("wiki/learning/flashcards.md", "Use spaced \n repetition daily.")
        self.note("wiki/learning/apart.md", "Spaced out sessions aid repetition.")
        got = self.search("spaced repetition")
        self.assertEqual([(n["path"], n["matched"]) for n in got["notes"]], [
            ("wiki/learning/spaced-repetition-basics.md", ["filename"]),
            ("wiki/learning/flashcards.md", ["body"]),
        ])
        self.assertEqual(got["total"], 2)

    def test_ranking_order(self):
        self.note("wiki/finance/zeta-rates.md", "nothing here", consumed="2026-10-01")
        self.note("wiki/finance/alpha.md", "nothing here", consumed="2026-10-01", tags=["rates"])
        self.note("wiki/finance/newer.md", "nothing here", consumed="2026-10-05", tags=["rates"])
        self.note("wiki/finance/undated.md", "nothing here", tags=["rates"])
        self.note("wiki/finance/body-heavy.md", "rates rates rates rates rates", consumed="2026-10-09")
        self.note("wiki/finance/two-terms.md", "rates and bonds")
        self.note("wiki/finance/bonds-rates.md", "")
        self.assertEqual(self.paths("rates", "bonds"), [
            "wiki/finance/bonds-rates.md",
            "wiki/finance/zeta-rates.md",
            "wiki/finance/newer.md",
            "wiki/finance/alpha.md",
            "wiki/finance/undated.md",
            "wiki/finance/two-terms.md",
            "wiki/finance/body-heavy.md",
        ])

    def test_output_fields(self):
        self.note("wiki/finance/fed-rates.md", "# Fed Rates\n\nThe Fed held rates.", consumed="2026-10-02",
                  tags=["fed", "interest-rates"])
        self.note("wiki/finance/untitled.md", "fed note")
        self.assertEqual(self.search("rates", "fed", "nomatch")["notes"], [
            {"path": "wiki/finance/fed-rates.md", "title": "Fed Rates", "date_consumed": "2026-10-02",
             "tags": ["fed", "interest-rates"], "matched": ["filename", "tags", "body"],
             "terms": ["rates", "fed"]},
            {"path": "wiki/finance/untitled.md", "title": "untitled", "date_consumed": None,
             "tags": [], "matched": ["body"], "terms": ["fed"]},
        ])

    def test_frontmatter_is_not_body(self):
        self.note("wiki/finance/plain.md", "nothing relevant")
        self.assertEqual(self.search("example")["total"], 0)

    def test_date_window_is_inclusive_and_drops_undated(self):
        for name, consumed in (("before", "2026-09-30"), ("first", "2026-10-01"),
                               ("last", "2026-10-03"), ("after", "2026-10-04"), ("undated", None)):
            self.note(f"wiki/finance/{name}.md", "market", consumed=consumed)
        self.assertEqual(self.paths("market", "--since", "2026-10-01", "--until", "2026-10-03"),
                         ["wiki/finance/last.md", "wiki/finance/first.md"])
        self.assertEqual(self.paths("market", "--since", "2026-10-03"),
                         ["wiki/finance/after.md", "wiki/finance/last.md"])

    def test_archived_is_excluded(self):
        self.note("wiki/archived/market.md", "market")
        self.note("wiki/finance/archived/market-old.md", "market")
        self.note("wiki/finance/market.md", "market")
        got = self.search("market")
        self.assertEqual([n["path"] for n in got["notes"]], ["wiki/finance/market.md"])
        self.assertEqual(got["total"], 1)

    def test_limit_truncates_notes_but_keeps_total(self):
        for name in ("a", "b", "c"):
            self.note(f"wiki/finance/{name}.md", "market")
        got = self.search("market", "--limit", "2")
        self.assertEqual((got["total"], [n["path"] for n in got["notes"]]),
                         (3, ["wiki/finance/a.md", "wiki/finance/b.md"]))
        self.assertEqual(self.search("market", "--limit", "0"), {"total": 3, "notes": []})

    def test_category_filter(self):
        self.note("wiki/finance/market.md", "market")
        self.note("wiki/learning/market.md", "market")
        self.assertEqual(self.paths("market", "--category", "learning/"), ["wiki/learning/market.md"])
        self.assertEqual(self.paths("market", "--category", "learning"), ["wiki/learning/market.md"])
        missing = self.run_cli("market", "--category", "nope")
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("no such category directory: wiki/nope/", missing.stderr)

    def test_topics_searches_topics_only(self):
        (self.root / "topics/ai-agents.md").write_text("---\ntype: topic-file\n---\n\n# AI Agents\n")
        self.note("wiki/finance/ai-agents.md", "agents")
        got = self.search("agent", "--topics")
        self.assertEqual([(n["path"], n["title"], n["date_consumed"]) for n in got["notes"]],
                         [("topics/ai-agents.md", "AI Agents", None)])

    def test_word_boundary_and_plural(self):
        self.note("wiki/finance/still.md", "Prices still rose.")
        self.note("wiki/finance/sti.md", "The STI index.")
        self.note("wiki/finance/agents.md", "Agents everywhere.")
        self.note("wiki/finance/budget.md", "The federal budget grew.")
        self.note("wiki/finance/sp.md", "The S&P 500 rose.")
        self.assertEqual(self.paths("sti"), ["wiki/finance/sti.md"])
        self.assertEqual(self.paths("agent"), ["wiki/finance/agents.md"])
        self.assertEqual(self.paths("fed"), [])
        self.assertEqual(self.paths("s&p 500"), ["wiki/finance/sp.md"])

    def test_block_list_tags_parsed(self):
        self.note("wiki/learning/memory.md", "unrelated", block_tags=["spaced-repetition", "memory"])
        got = self.search("spaced repetition")
        self.assertEqual([(n["path"], n["tags"], n["matched"]) for n in got["notes"]],
                         [("wiki/learning/memory.md", ["spaced-repetition", "memory"], ["tags"])])

    def test_usage_errors(self):
        for args in ([], ["--topics", "x", "--since", "2026-10-01"], ["x", "--category", "finance", "--topics"],
                     ["x", "--limit"], ["x", "--bogus"]):
            out = self.run_cli(*args)
            self.assertNotEqual(out.returncode, 0, args)
            self.assertIn("vault_search.py TERM...", out.stderr, args)
        for args, message in ((["x", "--limit", "-1"], "--limit must be a non-negative integer"),
                              (["x", "--since", "2026-13-01"], "--since must be YYYY-MM-DD")):
            out = self.run_cli(*args)
            self.assertNotEqual(out.returncode, 0, args)
            self.assertIn(message, out.stderr)


if __name__ == "__main__":
    unittest.main()

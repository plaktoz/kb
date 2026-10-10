#!/usr/bin/env python3
"""Tests for mental_models.py. Run: python3 .claude/skills/kb-librarian/scripts/test_mental_models.py"""
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name("mental_models.py").resolve()
sys.path.insert(0, str(SCRIPT.parent))
import mental_models as mm  # noqa: E402

OLD_NOTE = """## Key Takeaways
- **Point**: text

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: why it applies
- **[[Feedback Loop]]**: why it applies

## 🃏 Review Questions
"""

NEW_NOTE = """## 🧠 Core Principles

**T1. Proxies get gamed** — invariant · *model:* [[Goodhart's Law]]
→ explains: Point

**T2. Coined label** — invariant · *model:* [[Decoupling Dividend]]
→ explains: Point

## 🃏 Review Questions
"""


class Vault:
    def __enter__(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        (root / "wiki" / "strategy").mkdir(parents=True)
        (root / "data").mkdir()
        (root / "wiki" / "strategy" / "old.md").write_text(OLD_NOTE)
        (root / "wiki" / "strategy" / "new.md").write_text(NEW_NOTE)
        self.cwd = os.getcwd()
        os.chdir(root)
        return root

    def __exit__(self, *exc):
        os.chdir(self.cwd)
        self.tmp.cleanup()


def run(*args):
    return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True, text=True)


class VariantKeyTest(unittest.TestCase):
    def test_collapses_case_punctuation_and_plurals(self):
        self.assertEqual(mm.variant_key("Feedback Loops"), mm.variant_key("feedback loop"))
        self.assertEqual(mm.variant_key("Correlation vs. Causation"), mm.variant_key("Correlation vs Causation"))
        self.assertEqual(mm.variant_key("Map Is Not the Territory"), mm.variant_key("Map is Not Territory"))


class HarvestTest(unittest.TestCase):
    def test_reads_old_and_new_sections(self):
        with Vault():
            uses = mm.harvest()
        self.assertEqual(uses["Goodhart's Law"], 2)
        self.assertEqual(uses["Feedback Loop"], 1)
        self.assertEqual(uses["Decoupling Dividend"], 1)


class CommandsTest(unittest.TestCase):
    def test_build_from_map_counts_aliases_and_excludes_the_rest(self):
        with Vault() as root:
            (root / "map.json").write_text(json.dumps({"Goodhart's Law": [], "Feedback Loops": ["Feedback Loop"]}))
            self.assertEqual(run("build", "--map", "map.json").returncode, 0)
            entries = mm.load_list()
            self.assertEqual(entries, {"Feedback Loops": ["Feedback Loop"], "Goodhart's Law": []})
            self.assertIn("| [[Feedback Loops]] | Feedback Loop | 1 |", mm.LIST_PATH.read_text())
            self.assertIn("| [[Goodhart's Law]] |  | 2 |", mm.LIST_PATH.read_text())
            self.assertEqual(mm.load_excluded(), ["Decoupling Dividend"])
            self.assertEqual(json.loads(run("unlisted").stdout), [])

    def test_rebuild_without_map_is_stable(self):
        with Vault() as root:
            (root / "map.json").write_text(json.dumps({"Feedback Loops": ["Feedback Loop"]}))
            run("build", "--map", "map.json")
            first = mm.LIST_PATH.read_text()
            run("build")
            self.assertEqual(mm.LIST_PATH.read_text(), first)

    def test_unlisted_suggests_spelling_matches(self):
        with Vault() as root:
            (root / "map.json").write_text(json.dumps({"Feedback Loops": []}))
            run("build", "--map", "map.json")
            mm.write_excluded([])
            found = {e["name"]: e for e in json.loads(run("unlisted").stdout)}
            self.assertEqual(found["Feedback Loop"]["likely_alias_of"], "Feedback Loops")
            self.assertIsNone(found["Decoupling Dividend"]["likely_alias_of"])

    def test_add_alias_exclude(self):
        with Vault() as root:
            (root / "map.json").write_text(json.dumps({"Feedback Loops": []}))
            run("build", "--map", "map.json")
            self.assertEqual(run("alias", "Feedback Loop", "--to", "Feedback Loops").returncode, 0)
            self.assertEqual(run("add", "Goodhart's Law").returncode, 0)
            self.assertNotEqual(run("add", "goodhart's law").returncode, 0)
            self.assertNotEqual(run("alias", "X", "--to", "Missing").returncode, 0)
            self.assertNotEqual(run("exclude", "Feedback Loop").returncode, 0)
            self.assertEqual(mm.load_list()["Feedback Loops"], ["Feedback Loop"])
            run("exclude", "Some Label")
            self.assertIn("Some Label", mm.load_excluded())
            run("add", "Decoupling Dividend")
            self.assertNotIn("Decoupling Dividend", mm.load_excluded())


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Run the scrape probe over URLs with a known historical outcome and compare.

Usage: probe_vs_history.py labels.json [out.json]
Labels come from forensics.py --labels. Pages may have changed since they were scraped,
so disagreement is a lead to inspect, not proof the probe is wrong.
"""
import json
import sys
import time
from collections import Counter
from dataclasses import asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / ".claude/skills/kb-scrapecontent/scripts"))
import scrape_queue as sq


def bucket(label):
    if not label["saved"]:
        return "never-saved"
    return "saved-after-block" if label["blocked_hits"] else "saved-clean"


def main(labels_path, out_path=None):
    labels = json.load(open(labels_path))
    urls = sorted(labels)
    start = time.monotonic()
    probes = sq.probe_all(urls)
    wall = time.monotonic() - start
    table = Counter((bucket(labels[p.url]), p.verdict) for p in probes)
    verdicts = sorted({v for _, v in table})
    print(f"probed {len(urls)} urls in {wall:.1f}s\n")
    print(f"{'history':<20}" + "".join(f"{v:>12}" for v in verdicts) + f"{'not-ok%':>9}")
    for b in ("saved-clean", "saved-after-block", "never-saved"):
        row = [table[(b, v)] for v in verdicts]
        n = sum(row)
        if n:
            not_ok = n - table[(b, "ok")]
            print(f"{b:<20}" + "".join(f"{x:>12}" for x in row) + f"{100 * not_ok / n:>8.0f}%")
    if out_path:
        json.dump([dict(asdict(p), history=bucket(labels[p.url])) for p in probes], open(out_path, "w"), indent=1)


if __name__ == "__main__":
    main(*sys.argv[1:])

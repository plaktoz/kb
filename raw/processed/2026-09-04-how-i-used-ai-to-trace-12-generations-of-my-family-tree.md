---
source_url: https://hackernoon.com/how-i-used-ai-to-trace-12-generations-of-my-family-tree
author: Nicolas Fränkel
date: 2026-09-04
---

# How I Used AI to Trace 12 Generations of My Family Tree

Nicolas Fränkel, a Developer Advocate, spent roughly one month using Claude Code (an AI assistant) to build a family tree, ultimately documenting over 600 individuals across up to 12 generations.

## Setup

He treated it like a software project, using:

- **Git** (Codeberg for primary work, GitHub as a mirror)
- **Cloudflare Pages** for visualization
- **GEDCOM 5.5.1** as the data format — a genealogical data standard originally created by the Church of Jesus Christ of Latter-day Saints in 1984

## The Workflow Loop

Pick a person with unknown parents → AI searches genealogy sites and civil record archives → transcribes found documents → adds individuals to the GEDCOM file → commits. Repeat until records run out.

## Key AI Tips

- **Match model to task complexity** — don't waste powerful models on simple work, but don't use weak models for complex research
- **Create reusable "skills"** — packaged instruction sets that don't bloat context; he created skills for site navigation, image transcription, and autonomous sessions
- **Transcribe records to plain text once** — cheaper to reuse than re-parse PDFs/images repeatedly
- **Validate GEDCOM at every commit** — use pre-commit hooks or CI jobs; errors compound quickly
- **Use subagents for long sessions** — a subagent works in a branch, the main agent reviews and merges, preventing drift in overnight runs

## Genealogy Lessons Learned

- Results vary dramatically by country and even region
- Many genealogy sites offer free tiers and existing research — but always verify with official certificates
- Birth certificates are the most useful documents; they name parents with birth details
- Marriage certificates are second-best but often lack birth data for the parents listed
- French civil records become publicly accessible 75 years after the event date
- In small villages, identical surnames (and first names) required additional discriminants — particularly notable in Savoy, which developed a second-surname tradition
- GEDCOM supports flexible place formatting

## Visualization

He chose **Topola Genealogy Viewer** (web-based, supports GEDCOM 5.5.1) over Gramps (desktop/SQLite). Cloudflare Pages hosts the private site, offering GitHub integration, OTP-based access control, and per-branch preview subdomains — with a free tier limit of 500 builds/month.

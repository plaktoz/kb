---
type: literature-note
source_url: https://hackernoon.com/how-i-used-ai-to-trace-12-generations-of-my-family-tree
author: Nicolas Fränkel
tags: [ai-agents, genealogy, claude-code, workflow-automation]
date_consumed: 2026-09-16
---

## Summary

Developer Advocate Nicolas Fränkel used [[Claude Code]] over roughly one month to build a family tree, documenting over 600 individuals across up to 12 generations. He treated the project as a software engineering effort — using Git, [[GEDCOM]] as a data format, and Cloudflare Pages for visualization. The result demonstrates how AI agents with reusable "skills" and subagent orchestration can tackle long-horizon, document-heavy research tasks.

## Core Concepts

- **[[Claude Code]]** — the AI assistant used to drive the entire genealogy research and data-entry workflow autonomously
- **[[GEDCOM]]** — the genealogical data standard (v5.5.1) created by the Church of Latter-day Saints in 1984; used as the canonical data format
- **[[Reusable AI Skills]]** — packaged instruction sets that keep individual agent contexts lean; Fränkel built skills for site navigation, image transcription, and autonomous sessions
- **[[Subagent Orchestration]]** — a pattern where a subagent works on a branch while the main agent reviews and merges, preventing context drift in long overnight runs
- **[[Pre-commit Hooks]]** / [[CI Validation]] — used to validate GEDCOM after every commit; errors compound quickly without automated checks
- **[[Topola Genealogy Viewer]]** — web-based GEDCOM viewer chosen over Gramps (desktop/SQLite); hosted on [[Cloudflare Pages]] with OTP access control and per-branch previews
- **Civil Records** — birth, marriage, and death certificates sourced from national and regional archives; quality and accessibility vary significantly by country and region

## Key Takeaways

- **Workflow loop**: pick person → AI searches archives → transcribes documents → adds to GEDCOM → commit → repeat
- **Match model to task**: don't use powerful models for simple work, nor weak models for complex research
- **Reusable skills**: prevent context bloat; build once, invoke repeatedly across sessions
- **Transcribe once**: convert PDFs/images to plain text once; cheaper to reuse than re-parse
- **Validate every commit**: GEDCOM errors cascade — use pre-commit hooks or CI jobs
- **Subagents for long sessions**: branch + merge pattern prevents overnight context drift
- **Birth certificates are most useful**: name both parents with birth details; marriage certificates are second-best
- **Regional variation is significant**: country and even region affect record availability dramatically
- **French civil records**: publicly accessible 75 years after the event date
- **Small-village naming conflicts**: Savoy developed a second-surname tradition to disambiguate identical names

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Fränkel's architecture separates data (GEDCOM), visualization (Topola/Cloudflare), and agent logic (reusable skills) — each layer is independently replaceable and testable, which is why the project remained manageable at 600+ individuals.
- **[[Compounding Errors]]**: Skipping GEDCOM validation at each commit lets structural errors silently propagate; validating at every commit is the same principle as catching bugs at unit-test time rather than integration time.

## 🃏 Review Questions

**Q1**: What is the core thesis of this article?
**A**: AI agents with reusable skills and subagent orchestration can handle long-horizon, document-heavy research tasks end-to-end — Fränkel traced 600+ individuals across 12 generations in roughly one month using Claude Code.

**Q2**: What is the subagent pattern Fränkel used for long sessions, and why does it matter?
**A**: A subagent works on a dedicated branch while the main agent reviews and merges; this prevents context drift during overnight runs and keeps the primary agent's context clean.

**Q3**: What is the most important genealogical document type, and why?
**A**: Birth certificates — they name both parents along with their birth details, making them the most information-dense single document for extending the family tree upward.

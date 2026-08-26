---
name: kb-ingest-parallel
description: Parallel ingest of raw articles into structured wiki notes — 1 dedicated agent per file, up to 14 concurrent. Faster and higher quality than kb-ingest for large batches. Use when the user wants a parallel ingest run.
---

If the Workflow tool is available (Claude Code sessions), run it with `name: "kb-ingest-parallel"`. Wait for the workflow to complete, then report the result: how many files were ingested.

**Fallback (no Workflow tool, e.g. Cowork sessions):** Before dispatching any agents, run the exact-duplicate check from `.claude/skills/kb-ingest/SKILL.md` step 2 (`grep -rl "source_url: {URL}" wiki/`) yourself for every pending raw file, so duplicates never reach a sub-agent. For files flagged as duplicates, skip agent dispatch — just move the raw file to `raw/processed/` and log `ingest-dupe` yourself per step 2a. For the remaining non-duplicate files, dispatch one general-purpose Agent/Task call per file (batch in groups of ~8 concurrent per message if there are more) in a single message, each instructed to follow `.claude/skills/kb-ingest/SKILL.md`'s steps 3–11 and "After processing each file" for its one assigned file. If Agent/Task tooling is also unavailable, fall back to running `/kb-ingest` sequentially, unbatched.

---
name: kb-scrapecontent-parallel
description: Parallel scrape of URLs from /raw/url/ files using up to 8 concurrent agents. Faster than kb-scrapecontent for large URL batches. Use when the user wants a parallel scrape run.
---

If the Workflow tool is available (Claude Code sessions), run it with `name: "kb-scrapecontent-parallel"`. Wait for the workflow to complete, then report the result: how many articles were scraped and how many failed.

**Fallback (no Workflow tool, e.g. Cowork sessions):** Split the pending URLs into roughly equal batches (aim for 4–8 batches). In a single message, dispatch one general-purpose Agent/Task call per batch, each instructed to follow `.claude/skills/kb-scrapecontent/SKILL.md`'s per-URL instructions (steps 1–5) for its assigned subset only — each agent logs its own `scrape`/`scrape-failed` rows per step 6. After all agents return, run kb-scrapecontent's "After all URLs in a file are processed" step yourself once (rename the source file(s) in `raw/url/`, log the single `archive` row) — don't let sub-agents do this or the archive row will be duplicated. If Agent/Task tooling is also unavailable, fall back to running `/kb-scrapecontent` sequentially, unbatched.

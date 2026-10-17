---
name: kb-newsagent-parallel
description: Parallel news search — one agent per category in data/wiki-categories.md plus one for your holdings. Faster than kb-newsagent for the daily pipeline. Use when the user wants a parallel news search run.
---

If the Workflow tool is available (Claude Code sessions), run it with `name: "kb-newsagent-parallel"`. Wait for the workflow to complete, then report the result: output filename and article count per category (with any shortfalls).

**Fallback (no Workflow tool, e.g. Cowork sessions):** Read `data/investments.md` for holdings, read the news categories from the table in `data/wiki-categories.md` the way `/kb-newsagent` does, and determine the output filename yourself (check `raw/url/` for an existing `YYYY-MM-DD-news-aggregation*.md` and number accordingly). In a single message, dispatch one general-purpose Agent/Task call per category plus one for My Holdings, each instructed to follow `.claude/skills/kb-newsagent/references/rules.md` for its one category only and return its formatted markdown section. After all agents return, assemble the sections into one file at the filename you determined, and append the single `news-fetch` row to `kbm.log.md` yourself — don't let sub-agents write the file or log row directly, to avoid collisions. If Agent/Task tooling is also unavailable, fall back to running `/kb-newsagent` sequentially.

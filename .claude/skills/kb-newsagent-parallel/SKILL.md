---
name: kb-newsagent-parallel
description: Parallel news search — one agent per category (Technology/Finance/Productivity/Learning/Health/Holdings), up to 6 concurrent. Faster than kb-newsagent for the daily pipeline. Use when the user wants a parallel news search run.
---

If the Workflow tool is available (Claude Code sessions), run it with `name: "kb-newsagent-parallel"`. Wait for the workflow to complete, then report the result: output filename and article count per category (with any shortfalls).

**Fallback (no Workflow tool, e.g. Cowork sessions):** Read `data/investments.md` for holdings and determine the output filename yourself (check `raw/url/` for an existing `YYYY-MM-DD-news-aggregation*.md` and number accordingly). In a single message, dispatch one general-purpose Agent/Task call per category (6 total: Technology, Finance, Productivity, Learning, Health, My Holdings), each instructed to follow `.claude/skills/kb-newsagent/SKILL.md`'s search/dedup/blacklist/viability-check rules for its one category only and return its formatted markdown section. After all agents return, assemble the sections into one file at the filename you determined, and append the single `news-fetch` row to `kbm.log.md` yourself — don't let sub-agents write the file or log row directly, to avoid collisions. If Agent/Task tooling is also unavailable, fall back to running `/kb-newsagent` sequentially.

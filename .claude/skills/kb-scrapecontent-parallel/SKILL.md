---
name: kb-scrapecontent-parallel
description: Parallel scrape of URLs from /raw/url/ files using up to 8 concurrent agents. Faster than kb-scrapecontent for large URL batches. Use when the user wants a parallel scrape run.
---

Same three steps as `.claude/skills/kb-scrapecontent/SKILL.md`, with step 2 fanned out one agent per URL.

1. **Build the queue.** Run `python3 .claude/skills/kb-scrapecontent/scripts/scrape_queue.py discover`. It prints a summary in seconds; its `queue` field is this run's queue file. If `toScrape` is 0, go to step 3 with rows `[]`.
2. **Scrape.** Read the queue file. If the Workflow tool is available (Claude Code sessions), run it with `name: "kb-scrapecontent-parallel"` and `args: {"date": <queue.date>, "items": <queue.items>}` copied verbatim from the file. Wait for it to finish; it returns `rows`, one per item, including a `scrape-failed` row for any agent that stalled.

   **Fallback (no Workflow tool, e.g. Cowork sessions):** dispatch one general-purpose Agent/Task call per queue item, up to 8 per message. Give each agent its one item and tell it to follow step 2 of `.claude/skills/kb-scrapecontent/SKILL.md` for that item only and return `{filename, activity, reason}`. Turn any agent that errors or returns nothing into `{"filename": "<URL> (agent failed)", "activity": "scrape-failed"}`. If Agent/Task tooling is also unavailable, run `/kb-scrapecontent` sequentially instead.
3. **Finalize.** Write `rows` as JSON to `rows.json` next to the queue file and run `python3 .claude/skills/kb-scrapecontent/scripts/scrape_queue.py finalize <queue> <rows.json>`. Don't let agents write `kbm.log.md` or touch `raw/url/`.

Report how many articles were scraped and how many failed, with the failure reasons.

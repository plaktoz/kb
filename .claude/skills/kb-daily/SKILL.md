---
name: kb-daily
description: Run the full daily knowledge pipeline in sequence: news fetch → scrape → ingest → newsletter, plus compound → weekly newsletter on Sundays. Continues through failures and prints an end-of-run summary. Use when the user wants to run the complete daily knowledge base update.
---

# Daily Workflow

Run the full daily knowledge pipeline in this exact sequence. After each step, continue to the next regardless of errors — collect all errors and report them at the end.

## Step 1: News Agent

Invoke the `/kb-newsagent-parallel` skill and execute it (it uses the Workflow tool where available, and falls back to batched Agent/Task calls otherwise — see its `SKILL.md`).

If this step fails, note the error and continue to Step 2.

## Step 2: Scrape Content

Invoke the `/kb-scrapecontent-parallel` skill and execute it (it uses the Workflow tool where available, and falls back to batched Agent/Task calls otherwise — see its `SKILL.md`). Note how many articles were scraped and how many failed.

If this step fails, note the error and continue to Step 3.

## Step 3: Ingest

Invoke the `/kb-ingest-parallel` skill and execute it (same fallback behavior as Step 2). Note how many files were ingested as new/merged notes (`ingest`) versus flagged as duplicates (`ingest-dupe`).

If this step fails, note the error and continue to Step 4.

## Step 4: Newsletter

Invoke the `/kb-newsletter` skill and execute it.

If this step fails, note the error and continue to Step 5.

## Step 5: Weekly close-out (Sundays only)

Check the day of the week:

```bash
date +%u
```

If the result is not `7`, skip this step and print `Weekly close-out: skipped (not Sunday)` in the summary.

If it is `7`, run these two skills in order. They need today's daily ingest and newsletter to exist, which is why they run last. On a Sunday both skills treat the week that just ended as "this week".

1. Invoke the `/kb-compound` skill and execute it. Note how many topic files it created or updated.
2. Invoke the `/kb-weekly-newsletter` skill and execute it, even if compound failed. Note the filename it saved.

If either skill fails, note the error. Compound and the weekly newsletter are independent failures: a compound error does not stop the newsletter.

## End-of-run summary

After all steps are complete, print a summary in this format:

```
## Daily Pipeline Summary — YYYY-MM-DD

- News fetched: [N URLs saved to /raw/url/] or FAILED: [error]
- Articles scraped: [N files saved to /raw/] or FAILED: [error]
- Notes ingested: [N wiki notes created] or FAILED: [error]
- Newsletter: [filename saved to daily-update/] or FAILED: [error]
- Compound: [N topic files updated in topics/] or FAILED: [error] or skipped (not Sunday)
- Weekly newsletter: [filename saved to weekly-update/] or FAILED: [error] or skipped (not Sunday)
```

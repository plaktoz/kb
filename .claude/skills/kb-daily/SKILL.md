---
name: kb-daily
description: Run the full daily knowledge pipeline in sequence: news fetch → scrape → ingest → newsletter. Continues through failures and prints an end-of-run summary. Use when the user wants to run the complete daily knowledge base update.
---

# Daily Workflow

Run the full daily knowledge pipeline in this exact sequence. After each step, continue to the next regardless of errors — collect all errors and report them at the end.

## Step 1: News Agent

Invoke the `/kb-newsagent` skill and execute it.

If this step fails, note the error and continue to Step 2.

## Step 2: Scrape Content

Invoke the `/kb-scrapecontent-parallel` skill and execute it (it uses the Workflow tool where available, and falls back to batched Agent/Task calls otherwise — see its `SKILL.md`). Note how many articles were scraped and how many failed.

If this step fails, note the error and continue to Step 3.

## Step 3: Ingest

Invoke the `/kb-ingest-parallel` skill and execute it (same fallback behavior as Step 2). Note how many files were ingested as new/merged notes (`ingest`) versus flagged as duplicates (`ingest-dupe`).

If this step fails, note the error and continue to Step 4.

## Step 4: Newsletter

Invoke the `/kb-newsletter` skill and execute it.

If this step fails, note the error.

## End-of-run summary

After all four steps are complete, print a summary in this format:

```
## Daily Pipeline Summary — YYYY-MM-DD

- News fetched: [N URLs saved to /raw/url/] or FAILED: [error]
- Articles scraped: [N files saved to /raw/] or FAILED: [error]
- Notes ingested: [N wiki notes created] or FAILED: [error]
- Newsletter: [filename saved to daily-update/] or FAILED: [error]
```

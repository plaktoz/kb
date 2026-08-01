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

Run the Workflow tool with `name: "kb-scrapecontent-parallel"`. Wait for the workflow to complete, then note how many articles were scraped and how many failed.

If this step fails, note the error and continue to Step 3.

## Step 3: Ingest

Run the Workflow tool with `name: "kb-ingest-parallel"`. Wait for the workflow to complete, then note how many files were ingested.

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

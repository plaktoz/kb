# Daily Workflow Prompt

Run the full daily knowledge pipeline in this exact sequence. After each step, continue to the next regardless of errors — collect all errors and report them at the end.

## Step 1: News Agent

Read `skills/News-agent-prompt.md` and execute the instructions exactly as written.

If this step fails, note the error and continue to Step 2.

## Step 2: Scrape Content

Run the Workflow tool with `name: "kb-scrapecontent-parallel"`. Wait for the workflow to complete, then note how many articles were scraped and how many failed.

If this step fails, note the error and continue to Step 3.

## Step 3: Ingest

Run the Workflow tool with `name: "kb-ingest-parallel"`. Wait for the workflow to complete, then note how many files were ingested.

If this step fails, note the error and continue to Step 4.

## Step 4: Newsletter

Read `skills/Daily-newsletter-prompt.md` and execute the instructions exactly as written.

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

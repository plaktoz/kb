## Why

The daily pipeline skill currently runs scrape and ingest sequentially using single-agent serial prompts. The parallel workflow equivalents (`kb-scrapecontent-parallel`, `kb-ingest-parallel`) already exist and fan out up to 8 concurrent agents each, making them significantly faster for large batches. Updating the daily skill to invoke these workflows keeps the pipeline fast without requiring manual workflow invocation.

## What Changes

- `skills/Daily-workflow-prompt.md` Step 2: replace "Read `skills/Scrape-content-prompt.md` and execute" with "Run the Workflow tool with `name: "kb-scrapecontent-parallel"`"
- `skills/Daily-workflow-prompt.md` Step 3: replace "Read `skills/Karpathy-Ingest-prompt.md` and execute" with "Run the Workflow tool with `name: "kb-ingest-parallel"`"

## Capabilities

### New Capabilities

- `daily-workflow-parallel-steps`: The daily pipeline skill uses parallel scrape and ingest workflows instead of serial single-agent prompts

### Modified Capabilities

<!-- none — no existing main specs to delta against -->

## Impact

- `skills/Daily-workflow-prompt.md` — Steps 2 and 3 only
- No changes to Step 1 (news), Step 4 (newsletter), or the end-of-run summary format

## Why

After scraping, the URL source files in `raw/url/` are deleted — but Claude treats file deletion as a high-privilege destructive action, causing permission prompts or refusals in automated pipeline runs. Renaming to a `.processed.md` suffix is non-destructive, sidesteps the permission issue, and leaves a recoverable audit trail.

## What Changes

- `skills/Scrape-content-prompt.md`: skip `*.processed.md` on input; rename source file to `<name>.processed.md` after scraping all its URLs; log `archive` instead of `delete`
- `.claude/workflows/kb-scrapecontent-parallel.js`: exclude `*.processed.md` in the discover phase; rename source files in the finalize phase; log `archive` instead of `delete`

## Capabilities

### New Capabilities

- `url-file-cleanup`: Rename processed URL source files to `*.processed.md` instead of deleting them, with exclusion of already-processed files on next discovery

### Modified Capabilities

<!-- none — no existing spec-level behavior changes -->

## Impact

- `skills/Scrape-content-prompt.md` — input filtering and post-scrape cleanup section
- `.claude/workflows/kb-scrapecontent-parallel.js` — discover agent prompt and finalize agent prompt
- `kbm.log.md` activity values: `delete` → `archive` for URL source file cleanup rows

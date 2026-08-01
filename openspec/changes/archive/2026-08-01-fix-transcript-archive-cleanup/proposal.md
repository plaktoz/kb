## Why

The `kb-ingest-transcript` workflow archive phase deletes both the YouTube transcript video folders and the source URL files in `raw/youtube/`. Claude treats file and directory deletion as high-privilege destructive actions, causing permission prompts that stall automated pipeline runs. Replacing deletes with moves/renames makes cleanup non-destructive, sidesteps the permission issue, and leaves processed assets recoverable for manual review.

## What Changes

- `.claude/workflows/kb-ingest-transcript.js` — five changes across the workflow:
  1. **Discover phase (line 66)**: exclude `*.processed.md` from `raw/youtube/` discovery
  2. **Stage phase (line 134)**: exclude `youtube-transcript/processed/` from `transcript.md` search
  3. **Early-exit cleanup (line 167)**: rename source URL files to `*.processed.md`; log `archive`
  4. **Archive phase — folder cleanup (line 229)**: move each video folder (preserving `<channel>/<video>` hierarchy) into `youtube-transcript/processed/`; log `archive`
  5. **Archive phase — source URL cleanup (line 232)**: rename source URL files to `*.processed.md`; log `archive`

## Capabilities

### New Capabilities

- `transcript-archive-cleanup`: Non-destructive post-ingest cleanup — video folders moved to `youtube-transcript/processed/` and URL source files renamed to `*.processed.md`, with discovery exclusions so re-runs skip already-processed assets

### Modified Capabilities

<!-- none — no existing spec-level behavior changes -->

## Impact

- `.claude/workflows/kb-ingest-transcript.js` — discover, stage, early-exit, and archive agent prompts
- `kbm.log.md` activity values: `delete` → `archive` for cleanup rows
- `youtube-transcript/processed/` directory created on first run

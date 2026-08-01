## Context

The `kb-ingest-transcript` workflow has five phases: Fetch → Stage → Ingest → Archive → Newsletter. The Archive phase currently issues three delete operations: two targeting source URL files in `raw/youtube/` (one in the early-exit path, one in the main path) and one targeting the downloaded video folders under `youtube-transcript/`. Claude treats these as high-privilege destructive actions.

The Stage phase discovers transcripts by scanning for `transcript.md` anywhere inside `youtube-transcript/`. The Discover phase reads all `.md` files from `raw/youtube/`.

## Goals / Non-Goals

**Goals:**
- Replace all delete operations with non-destructive alternatives (move/rename)
- Prevent re-processing on subsequent runs via discovery exclusions
- Apply consistent `archive` log activity across both cleanup types
- Preserve channel/video folder hierarchy when moving to `youtube-transcript/processed/`

**Non-Goals:**
- No purge or auto-management of accumulated processed assets — manual step
- No changes to Fetch, Ingest, or Newsletter phases
- No changes to how wiki notes or `raw/processed/` files are handled

## Decisions

**Video folders: move to `youtube-transcript/processed/<channel>/<video>/`**
Moving the entire folder (rather than renaming `transcript.md` inside it) preserves all downloaded assets for manual inspection and keeps the channel hierarchy intact. The Stage agent's exclusion of `youtube-transcript/processed/` is a single-line addition to its discovery prompt — simpler than a suffix-based filter.

**Source URL files: rename to `*.processed.md` (consistent with scrape pipeline)**
This mirrors the pattern established for `raw/url/` files in the scrape workflow. Discovery exclusion is a single suffix check.

**Hierarchy preservation on folder move**
Given `folderPath` like `youtube-transcript/ai-engineer/video-title/`, the archive agent creates `youtube-transcript/processed/ai-engineer/` if needed, then moves the video folder into it. The channel segment is derived from the existing path structure.

**Log activity: `archive` for both cleanup types**
Consistent with the scrape pipeline fix. `delete` rows in `kbm.log.md` should mean the asset is gone; `archive` signals it was moved/renamed and is recoverable.

## Risks / Trade-offs

- **Channel directory left empty after move** → `youtube-transcript/ai-engineer/` may become an empty directory after all its videos are moved. Harmless — next fetch will recreate it if needed, and the `processed/` subtree remains clean.
- **Move fails if `processed/` already has a folder with the same name** → Duplicate video runs would conflict. Acceptable edge case; pipeline is not designed for re-ingesting the same video.

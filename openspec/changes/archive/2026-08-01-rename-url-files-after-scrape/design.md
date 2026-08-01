## Context

Two files own scrape cleanup: the serial skill prompt (`skills/Scrape-content-prompt.md`) and the parallel workflow (`.claude/workflows/kb-scrapecontent-parallel.js`). Both follow the same pattern: discover URL source files in `raw/url/` → scrape each URL → clean up the source file.

Currently the cleanup step issues a file deletion. Claude treats deletion as a high-privilege destructive action — this triggers permission prompts in automated pipeline runs and can cause the finalize step to stall or fail silently.

## Goals / Non-Goals

**Goals:**
- Replace all delete calls with rename (`<file>.md` → `<file>.processed.md`) in both the serial and parallel paths
- Prevent re-processing: discovery must exclude `*.processed.md` files
- Update log activity from `delete` to `archive` to reflect the non-destructive action

**Non-Goals:**
- No changes to scrape logic, output format, article storage, or scheduling
- No purge or management of accumulated `.processed.md` files — that remains a manual step

## Decisions

**Rename in-place vs. move to subdirectory**
Renaming in-place (`raw/url/news.md` → `raw/url/news.processed.md`) was chosen over moving to `raw/url/processed/`. Reason: no directory creation needed, the file stays co-located with pending files, and the `.processed.md` suffix is self-documenting. Subdirectory would require the finalize agent to create the directory if absent, adding a failure mode.

**Exclusion by suffix**
Discovery filters out `*.processed.md` by suffix pattern rather than checking a separate manifest. Reason: simpler, requires no state file, and aligns with how agents naturally read "all .md files except those ending in .processed.md."

**Log activity: `archive` not `delete`**
The existing `kbm.log.md` schema uses `delete` for source file removal. Changing to `archive` accurately describes a rename and avoids confusion when reviewing the log (a `delete` row should mean the file is gone).

## Risks / Trade-offs

- **Rename fails silently** → If the finalize agent cannot rename a file (unlikely in local vault), the source file remains as-is and will be re-discovered on the next run. URLs in it will be de-duplicated against existing `raw/` files, so no data is re-scraped; the only cost is a wasted discovery round.
- **`.processed.md` accumulation** → Files are not auto-purged. Over time `raw/url/` will accumulate processed files. This is intentional — they serve as an audit trail and are removed manually.

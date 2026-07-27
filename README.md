# Knowledge Base (kb)

A personal knowledge management (PKM) system that captures raw information, transforms it into structured notes, and synthesizes it into daily and weekly digests.

## How it works

1. **Capture** — raw articles and URLs are pulled into `raw/`
2. **Transform** — source material is processed into atomic, link-rich notes filed under `wiki/`
3. **Synthesize** — notes are compiled into daily and weekly digests

## Outputs

- **[daily-update/](daily-update/)** — daily newsletter digests, organized by month (`YYYY-MM/YYYY-MM-DD-N.md`)
- **[weekly-update/](weekly-update/)** — weekly synthesis digests, organized by month (`YYYY-MM/YYYY-WXX-weekly.md`)

## Folder map

| Folder | Purpose |
|--------|---------|
| `raw/url/` | URL lists waiting to be scraped |
| `raw/processed/` | Scraped articles waiting to be ingested |
| `wiki/` | Canonical notes organized by category |
| `Skills/` | Prompt templates that power the automated workflows |
| `daily-update/` | Daily newsletter digests |
| `weekly-update/` | Weekly synthesis digests |
| `data/` | Supporting reference data (investment holdings, wiki categories) |

## Automated workflows

The `Skills/` folder contains prompt templates for each recurring task:

- **Daily pipeline** — news fetch → scrape → ingest → newsletter
- **Weekly compound** — synthesizes the week's daily digests into a high-signal summary

See `CLAUDE.md` for full workflow conventions and prompt instructions.

# CLAUDE.md

## Project purpose
This repository is a local-first personal knowledge management (PKM) system built around Obsidian-style markdown notes. The core goal is to capture raw information, turn it into structured notes, and connect those notes into a durable knowledge graph.

## Repository map
- `glossary.md` — canonical vocabulary (personal reference only, do not read or rely on during tasks)
- `kbm.log.md` — activity log; append a row after every pipeline action
- `raw/` — source material at different pipeline stages
  - `url/` — URL lists waiting to be scraped (consumed and deleted by the scrape step)
  - `processed/` — post-ingest archive; articles moved here by Karpathy after wiki notes are created
- `wiki/` — canonical notes; categories defined in `data/wiki-categories.md`
  - `others/` — staging area for notes whose category is unclear; revisit with /kb-reorg
- `skills/` — prompt templates for recurring workflows (see Skills section below)
- `daily-update/` — daily newsletter digests
- `weekly-update/` — weekly synthesis digests
- `data/` — supporting reference data
  - `investments.md` — investment holdings (do not modify unless explicitly asked)
  - `wiki-categories.md` — canonical list of wiki subdirectory categories

## Skills
Read the matching skill file before executing any recurring task.

| Skill file | Purpose |
|-----------|---------|
| `sills/Daily-workflow-prompt.md` | Runs the full daily pipeline in sequence: news → scrape → ingest → newsletter |
| `skills/News-agent-prompt.md` | Fetches today's top news across investment holdings and topic categories; saves URL list to `raw/url/` |
| `skills/Scrape-content-prompt.md` | Scrapes URLs from `raw/url/` and saves each as a clean markdown file in `raw/processed/` |
| `skills/Karpathy-Ingest-prompt.md` | Transforms `raw/processed/` files into structured wiki notes |
| `skills/Daily-newsletter-prompt.md` | Compiles today's ingested notes into a daily newsletter digest |
| `skills/Weekly-workflow-prompt.md` | Runs the full weekly pipeline in sequence: compound → weekly digest |
| `skills/Research-topic-prompt.md` | Grills user to refine a topic, builds a research outline, searches 10–20 articles, saves report to `research/<context-slug>/` |
| `skills/Weekly-compound-prompt.md` | Compounds the week's daily digests into a high-signal weekly synthesis |
| `skills/Wiki-reorg-prompt.md` | Reconciles wiki/ structure against wiki-categories.md, reclassifies notes, refreshes glossary |

## Core workflow
1. Capture raw content into the vault with minimal friction.
2. Transform it into structured notes that are concise, atomic, and link-rich.
3. Connect new notes to existing concepts using Obsidian-style wiki links.
4. Use the matching skill from `skills/` for each recurring task.

## Conventions

### Note naming
- `wiki/` notes: kebab-case slug only, no date prefix — e.g. `trump-strait-of-hormuz-sp500.md`
- `raw/processed/` files: date-prefixed — e.g. `2026-07-26-article-slug.md`

### Output file locations
- Daily digests: `daily-update/YYYY-MM/YYYY-MM-DD-N.md` (N = sequence number for multiple digests per day)
- Weekly digests: `weekly-update/YYYY-MM/YYYY-WXX-weekly.md`

### Wiki categories
Read `data/wiki-categories.md` for the current list of categories. When filing a note:
- Use the closest matching category.
- If no category fits, place the note under `wiki/others/` and propose a new category to the user. Do not create a new category directory without confirmation.

### Activity log
Append a row to `kbm.log.md` after every pipeline action using this table format:

```
| Date | File | Activity |
```

Valid activity values: `ingest`, `scrape`, `scrape-failed`, `news-fetch`, `newsletter`, `delete`, `reorg`, `research`

### General conventions
- Prefer working inside the existing vault structure rather than creating ad hoc folders.
- Use Obsidian-compatible markdown links such as `[[Note Name]]` when linking related ideas.
- Before creating a new concept note, check existing wiki notes to avoid duplicates.
- Favor durable, reusable notes over verbose drafts.

## Content rules
- Do not invent facts or add unsupported claims.
- Rely on source material and the existing knowledge base.
- Keep notes focused on one idea or topic whenever possible.
- Prefer clear summaries, strong links, and practical usefulness for later retrieval.

## Preferred behavior
- Read relevant existing notes before creating new ones.
- Update an existing note when a strong match already exists.
- Keep the knowledge graph coherent by linking related notes thoughtfully.
- When asked to create a new artifact, use the matching skill from `Skills/` and save output in the expected location.

## Do not
- Modify `skills-lock.json` or anything in `.obsidian/`.
- Modify `data/investments.md` unless explicitly asked.
- Delete files from `raw/processed/` — that is a manual step after you have verified the ingest.

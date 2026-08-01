# CLAUDE.md

## Project purpose
This repository is a local-first personal knowledge management (PKM) system built around Obsidian-style markdown notes. The core goal is to capture raw information, turn it into structured notes, and connect those notes into a durable knowledge graph.

## Repository map
- `glossary.md` — canonical vocabulary (personal reference only, do not read or rely on during tasks)
- `kbm.log.md` — activity log; append a row after every pipeline action
- `raw/` — source material at different pipeline stages
  - `url/` — URL lists waiting to be scraped (consumed and deleted by the scrape step)
  - `*.md` — scraped articles awaiting ingest
  - `processed/` — post-ingest archive; articles moved here after wiki notes are created
- `wiki/` — canonical notes; categories defined in `data/wiki-categories.md`
  - `others/` — staging area for notes whose category is unclear; revisit with /kb-librarian
- `daily-update/` — daily newsletter digests
- `weekly-update/` — weekly synthesis digests
- `research/` — sourced research reports organized by topic slug (`<context-slug>/report.md`)
- `data/` — supporting reference data
  - `investments.md` — investment holdings (do not modify unless explicitly asked)
  - `wiki-categories.md` — canonical list of wiki subdirectory categories

## Skills
Invoke the matching slash command for each recurring task. Skills are self-contained in `.claude/skills/`.

| Slash command | Purpose |
|--------------|---------|
| `/kb-daily` | Runs the full daily pipeline in sequence: news → scrape → ingest → newsletter |
| `/kb-newsagent` | Fetches today's top news across investment holdings and topic categories; saves URL list to `raw/url/` |
| `/kb-scrapecontent` | Scrapes URLs from `raw/url/` and saves each as a clean markdown file in `raw/` |
| `/kb-ingest` | Transforms `raw/` files into structured wiki notes |
| `/kb-newsletter` | Compiles today's ingested notes into a daily newsletter digest |
| `/kb-research-topic` | Grills user to refine a topic, builds a research outline, searches 10–20 articles, saves report to `research/<context-slug>/` |
| `/kb-compound` | Deepens existing wiki notes and creates synthesis notes from recurring cross-category themes — run before `/kb-weekly-newsletter` |
| `/kb-weekly-newsletter` | Compiles this week's ingested notes into a weekly newsletter digest |
| `/kb-librarian` | Full vault maintenance: reconciles wiki/ structure, reclassifies notes, refreshes glossary, detects duplicates/superseded notes, rebuilds kbm.log.md, and checks raw/processed/ for unmatched stragglers |
| `/kb-librarian-apply` | Executes human-filled decisions from librarian-report.md |
| `/kb-quizme` | Quizzes you on recently ingested wiki articles using spaced repetition |
| `/kb-topic-query` | Searches the local wiki vault and synthesizes what you already know about a topic — no internet |
| `/kb-note-deepen` | Enriches an existing wiki note with new insights and links found in newer vault notes |
| `/kb-investment-digest` | Summarizes recent vault notes about your holdings into a per-ticker weekly digest |
| `/kb-research-to-lessons` | Converts a research report into an interactive HTML lesson course with curriculum plan, shared assets, and parallel-generated lessons |

### Parallel skills (opt-in)

| Workflow script | Slash command | Purpose |
|----------------|---------------|---------|
| `.claude/workflows/kb-scrapecontent-parallel.js` | `/kb-scrapecontent-parallel` | Same as kb-scrapecontent but fans out up to 8 concurrent scrape agents; log written by coordinator |
| `.claude/workflows/kb-ingest-parallel.js` | `/kb-ingest-parallel` | Same as kb-ingest but fans out up to 8 concurrent ingest agents; log written by coordinator |
| `.claude/workflows/kb-ingest-transcript.js` | `/kb-ingest-transcript` | Full YouTube pipeline: fetch URLs from `raw/youtube/`, download + speaker-ID transcripts, stage to `raw/`, parallel ingest into wiki, then archive |

## Core workflow
1. Capture raw content into the vault with minimal friction.
2. Transform it into structured notes that are concise, atomic, and link-rich.
3. Connect new notes to existing concepts using Obsidian-style wiki links.
4. Use the matching slash command (see Skills section above) for each recurring task.

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

Valid activity values: `ingest`, `scrape`, `scrape-failed`, `news-fetch`, `newsletter`, `compound`, `delete`, `reorg`, `research`, `lessons`

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
- When asked to create a new artifact, use the matching slash command and save output in the expected location.

## Do not
- Modify `skills-lock.json` or anything in `.obsidian/`.
- Modify `data/investments.md` unless explicitly asked.
- Delete files from `raw/processed/` — that is a manual step after you have verified the ingest.

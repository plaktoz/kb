# CLAUDE.md

## Project purpose
This repository is a local-first personal knowledge management (PKM) system built around Obsidian-style markdown notes. The core goal is to capture raw information, turn it into structured notes, and connect those notes into a durable knowledge graph.

## Repository map
- kb/ — the main vault content and workflow assets
  - glossary.md — canonical vocabulary and note conventions
  - kbm.log.md — activity log for ingests, scrapes, newsletters, and compounds
  - raw/ — raw source material and processed content
  - wiki/ — canonical notes organized by category
  - Skills/ — prompt templates for ingestion and synthesis workflows
  - daily-update/ — daily newsletter digests
  - weekly-update/ — weekly synthesis digests
- data/ — supporting reference data such as investment holdings

## Core workflow
1. Capture raw content into the vault with minimal friction.
2. Transform it into structured notes that are concise, atomic, and link-rich.
3. Connect new notes to existing concepts using Obsidian-style wiki links.
4. Use the prompt templates in kb/Skills/ for recurring workflows such as ingestion, newsletter generation, and weekly compounding.

## Conventions to follow
- Prefer working inside the existing vault structure rather than creating ad hoc folders.
- Use Obsidian-compatible markdown links such as [[Note Name]] when linking related ideas.
- Before creating a new concept note, check the glossary and existing wiki notes to avoid duplicate concepts.
- Preserve the existing naming patterns and keep note titles descriptive and stable.
- Favor durable, reusable notes over verbose drafts.
- When generating outputs such as newsletters or weekly summaries, place them in the appropriate dated folder and keep the formatting consistent with the existing prompt templates.

## Content rules
- Do not invent facts or add unsupported claims.
- Rely on source material and the existing knowledge base.
- Keep notes focused on one idea or topic whenever possible.
- Prefer clear summaries, strong links, and practical usefulness for later retrieval.

## Preferred behavior for Claude
- Read relevant existing notes before creating new ones.
- Update an existing note when a strong match already exists.
- Keep the knowledge graph coherent by linking related notes thoughtfully.
- Respect the repository’s automation patterns and avoid breaking the log or note conventions.
- When asked to create a new artifact, follow the repository’s existing prompt structure and save it in the expected location.

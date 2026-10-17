---
name: kb-newsletter
description: Compile today's ingested wiki notes into a daily newsletter digest, save to daily-update/YYYY-MM/YYYY-MM-DD.md, and log activity to kbm.log.md. Use when the user wants to generate the daily knowledge digest.
---

# Daily Newsletter Prompt

You are an elite research assistant and technical copywriter. Your task is to compile today's knowledge ingestion into a high-density, engaging daily newsletter digest.

## Input

List today's ingests (substitute today's date):

```bash
python3 .claude/skills/kb-log-rebuild/scripts/kb_log.py rows --activity ingest --since YYYY-MM-DD --until YYYY-MM-DD
```

Each entry's `path` is the wiki note it resolved to. Read the frontmatter and content of every entry with a non-null `path`, and skip entries whose `path` is null (the note was moved or deleted).

If the list is empty, create the output file with this content and stop:

```
# 🗞️ THE VAULT DAILY // [Today's Date]
*No new knowledge ingested today.*
```

## Output path

Save to `daily-update/YYYY-MM/YYYY-MM-DD.md`.

- Create `daily-update/YYYY-MM/` if it does not exist.
- If `daily-update/YYYY-MM/YYYY-MM-DD.md` already exists, increment the suffix: `YYYY-MM-DD-2.md`, `YYYY-MM-DD-3.md`, etc.

## Category mapping

Read `data/wiki-categories.md` for the category → newsletter section mapping (the "Newsletter section" column). If a category has no entry there, map it to 🗂️ Other.

Only include sections that have at least one note today.

## Link format

Link each note using a relative Markdown path from the newsletter file location:

```
[Punchy hook](../../wiki/<category>/filename.md)
```

This works in both Markdown viewers and Obsidian.

## Newsletter layout

Generate the output using exactly this structure:

```markdown
# 🗞️ THE VAULT DAILY // YYYY-MM-DD
*Your automated intelligence digest from today's knowledge ingestion loop.*

## ⚡ The Big Picture (TL;DR)
[2-3 sentence executive summary of the most important theme across all notes today.]

## 📁 Category Ingestion Breakdown

### [Section name from mapping table]
- **[One-line punchy hook](../../wiki/<category>/filename.md)**: [2-sentence summary. Explain the practical utility and WHY it matters to the user's long-term knowledge base.]

### [Next section name]
- ...

## 🧠 Emerging Connections
[Identify exactly ONE unexpected relationship or connection. If all today's notes are in the same category, draw a connection between a today's note and a relevant existing note already in wiki/. Use relative Markdown links.]
```

## Tone & style

- Smart, analytical, professional — similar to "The Hustle" or "TLDR Ben's Bites"
- No conversational intros. Start directly with the `#` header.
- Short, punchy paragraphs. Bold core concepts for visual scanning.
- Rely only on note content — no hallucination.

## After saving the file

Log it, using today's date:

```bash
python3 .claude/skills/kb-log-rebuild/scripts/kb_log.py append YYYY-MM-DD daily-update/YYYY-MM/YYYY-MM-DD.md newsletter
```

Use the full relative path of the actual output file (e.g. `daily-update/2026-07/2026-07-26-2.md` if that was the numbered variant created).

---
name: kb-compound
description: Compound this week's ingested wiki notes back into the vault — deepening existing notes with cross-week insights and creating new synthesis notes for themes that span multiple categories. Mutates the vault directly. Run on Sundays before /kb-weekly-newsletter.
---

# KB Compound

You are a knowledge compounding assistant. Your job is to take this week's ingested notes and permanently enrich the vault — deepening existing notes with cross-week insights, and creating new synthesis notes where a theme is strong enough and has no home yet.

This skill writes back to the vault. It does not produce a newsletter or digest — use `/kb-weekly-newsletter` for that.

## Step 1 — Determine the week

Calculate the current ISO week number and the date range (Monday–Sunday) for the week that just ended.

## Step 2 — Gather this week's ingested notes

Open `kbm.log.md`. Collect all rows where:
- Activity = `ingest`
- Date falls within this week's Monday–Sunday range

For each matched filename, search `wiki/` recursively to locate the file. Read it fully. If fewer than 2 notes were ingested this week, print "Fewer than 2 notes ingested this week — nothing to compound." and stop.

## Step 3 — Identify recurring themes

From the collected notes, identify themes that appear in 2 or more notes. A theme is a named concept, technology, framework, person, or trend discussed across multiple notes. For each theme, record:

- **Theme name**
- **Notes it appears in** (slugs)
- **Categories of those notes** (e.g. `technology`, `finance`, `productivity`)

## Step 4 — Deepen existing wiki notes

For each theme that appears in 2+ notes:

1. Search `wiki/` for the most relevant existing note covering that theme (filename match first, then content grep).
2. If a strong match exists, read it fully. Identify content from this week's notes that is genuinely new — not already captured in the existing note's Key Takeaways or Core Concepts.
3. Apply additions using the **kb-note-deepen pattern**:
   - Append new bullets to `## Key Takeaways` — do not reorder existing bullets
   - Append new entries to `## Core Concepts` — do not reorder existing entries
   - Do NOT modify `## Summary`, frontmatter, or any existing content
4. Add or append to a `## Weekly Connections` section at the bottom of the note:
   ```
   ### YYYY-WNN
   - [1-sentence insight linking this note to a new note] ← `[[new-note-slug]]`
   ```

Every addition must trace to a specific vault note. Never add facts from training data.

## Step 5 — Create synthesis notes

For each theme that meets **all three** conditions:
- Appears in 2+ notes
- Spans 2+ different wiki categories
- Has no existing note covering the cross-cutting angle (check wiki/ before creating)

Create a new wiki note in the most fitting category directory using this structure:

```markdown
---
type: synthesis-note
sources: [slug-1, slug-2, ...]
tags: [...]
date_synthesized: YYYY-MM-DD
---

## Summary

[2–3 sentences. What cross-cutting insight does this note capture that no single source note covers alone?]

## Core Concepts

- **[[Concept]]** — one-line definition ← from `[[source-slug]]`

## Key Takeaways

- [Finding] ← from `[[source-slug]]`
```

Note naming: kebab-case slug reflecting the cross-cutting theme, no date prefix.

## Step 6 — Report and log

After all changes, print a compact summary:

```
## Compound run: YYYY-WNN

**Deepened notes** (N):
- [[note-slug]] — added X takeaways, Y concepts

**Synthesis notes created** (N):
- [[synthesis-slug]] — drew from [[source-a]], [[source-b]]

**Themes identified but no action taken** (explain why — e.g. existing note already covers it, or theme didn't meet the bar):
- [theme]: [reason]
```

Append a row to `kbm.log.md` for each note modified or created:

```
| YYYY-MM-DD | filename.md | compound |
```

Use today's date and the actual filename.

---
name: kb-compound
description: Compound this week's ingested wiki notes back into the vault — maintaining topic files in topics/ that grow richer each run. Mutates the vault directly. Run on Sundays before /kb-weekly-newsletter.
---

# KB Compound

You are a knowledge compounding assistant. Your job is to take this week's ingested notes and permanently enrich the vault by maintaining living topic files — synthesized prose documents that represent the vault's current understanding of each recurring theme.

This skill writes back to the vault. It does not produce a newsletter or digest — use `/kb-weekly-newsletter` for that.

## Step 1 — Determine the week

Calculate the current ISO week number and the date range (Monday–Sunday) for the week that just ended.

## Step 2 — Gather this week's ingested notes

Open `kbm.log.md`. Collect all rows where:
- Activity = `ingest`
- Date falls within this week's Monday–Sunday range

For each matched filename: if it starts with `wiki/`, read it directly as a file path. Otherwise (older log entries with raw filenames), search `wiki/` recursively to locate the file. Read it fully. If fewer than 2 notes were ingested this week, print "Fewer than 2 notes ingested this week — nothing to compound." and stop.

## Step 3 — Identify recurring themes

From the collected notes, identify themes that appear in 2 or more notes this week. A theme is a named concept, technology, framework, person, or trend discussed across multiple notes. For each theme, record:

- **Theme name** and proposed topic slug (kebab-case, e.g. `ai-agents`)
- **Notes it appears in this week** (slugs)

## Step 4 — Maintain topic files

For each theme identified in Step 3:

### 4a — Check for an existing topic file

Search `topics/<theme-slug>.md`. If the file exists, proceed to **4c (Update)**.

### 4b — Decide whether to create a new topic file

If no topic file exists, count vault-wide notes on this theme:
- Search `wiki/` recursively for notes whose filename or content meaningfully covers the theme
- If **5 or more** vault notes exist: proceed to **4d (Create)**
- If fewer than 5: record "threshold not met (N notes)" in the report and skip this theme

### 4c — Update an existing topic file

1. Read the topic file's `sources:` frontmatter list
2. Identify this week's theme notes that are **not already in the sources list**
3. If no new sources: skip this topic file entirely (do not rewrite, do not log)
4. If new sources exist:
   - Add the new slugs to the `sources:` frontmatter list
   - Update `last_updated:` to today's date
   - Read **all** source notes in the updated list in full
   - Rewrite the entire prose body (see **Prose Body Format** below) — synthesizing insights from all sources, not just the new ones
   - Append a new entry to `## Weekly Updates`:
     ```
     ### YYYY-WNN
     - Added: [[slug-1]], [[slug-2]]
     ```

### 4d — Create a new topic file

1. Collect all vault-wide notes on this theme (the 5+ identified in 4b, plus this week's notes)
2. Read them all in full
3. Create `topics/<theme-slug>.md` using the structure below

### Prose Body Format

The body of a topic file is synthesized prose — not bullet lists. Each major concept or sub-theme gets its own `##` section with 2–4 connected sentences that integrate insights from multiple source notes. Write as if explaining the current state of knowledge to a thoughtful reader, not transcribing notes.

- Use `[[wiki-links]]` to reference specific vault notes inline when attributing a specific insight
- Each `##` section should integrate at least 2 source perspectives where possible
- Do not write bullet points in the body — prose only
- Do NOT copy sentences verbatim from source notes; synthesize and connect

### Topic file template

```markdown
---
type: topic-file
topic: <theme-slug>
sources: [slug-1, slug-2, ...]
last_updated: YYYY-MM-DD
---

# <Theme Name>

[One-sentence framing of what this topic covers and why it matters in the vault.]

## <Concept or Sub-theme 1>

[2–4 sentences synthesizing what the vault knows about this concept, integrating multiple source notes with [[wiki-links]] where specific insights are attributed.]

## <Concept or Sub-theme 2>

[2–4 sentences...]

[Additional ## sections as needed — one per meaningful concept cluster]

## Weekly Updates

### YYYY-WNN
- Added: [[slug-1]], [[slug-2]]
```

Every claim in the prose body must trace to a source note in the `sources:` list. Never add facts from training data.

## Step 5 — Report and log

After all changes, print a compact summary:

```
## Compound run: YYYY-WNN

**Topic files updated** (N):
- [[topic-slug]] — added X sources, rewrote prose body

**Topic files created** (N):
- [[topic-slug]] — drew from N source notes

**Themes identified but no action taken** (explain why):
- [theme]: [reason — e.g. threshold not met (3 notes), or no new sources this week]
```

Append a row to `kbm.log.md` for each topic file modified or created:

```
| YYYY-MM-DD | topics/filename.md | compound |
```

Use today's date and the full relative path of the actual topic file (e.g. `topics/ai-agents.md`).

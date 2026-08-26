---
name: kb-ingest
description: Process scraped articles from /raw/ into structured wiki notes, archive to /raw/processed/, and log activity to kbm.log.md. Use when the user wants to ingest raw articles into the knowledge base wiki.
---

# Karpathy Ingest Prompt

You are an expert Personal Knowledge Management (PKM) assistant specializing in compiling raw literature into a highly organized, dense Obsidian wiki.

## Input

Read all `.md` files in `/raw/` that contain a `source_url:` header. Skip everything else (subdirectories, news-aggregation files, files without `source_url:`) silently. Process all eligible files in one run.

## Per-File Instructions

### 1. Categorize

Place the file into exactly one category. Read `data/wiki-categories.md` for the current list of valid categories. Use exactly the category slugs listed there. Do not create new categories — if nothing fits, use `others`.

### 2. Check for existing notes

First, run an exact-duplicate check on the raw file's `source_url`: `grep -rl "source_url: {URL}" wiki/`. If this returns a match, the article has already been ingested — go to step 2a and do not write any new content.

If no exact match is found, do a topical scan: search `wiki/<category>/` (and skim adjacent categories if the topic could straddle two) for an existing note covering the same underlying story or concept from a different source. If one exists, treat it as a near-duplicate and also go to step 2a.

If neither check finds a match, this is a genuinely new topic — continue to step 3.

#### 2a. Duplicate / near-duplicate handling

Read the matched note and compare it against the new raw file.

- **No new information** — the raw file adds nothing beyond what the existing note already covers: do not modify the note. Move the raw file to `raw/processed/` per the usual post-processing step, then log it with activity value `ingest-dupe`, using the *existing note's* path as the File column plus a short parenthetical reason, e.g. `wiki/productivity/seven-productivity-habits-remove-friction.md (identical source_url, no new info)`.
- **New information** — e.g. a follow-up development, updated figures, a deal completion: merge it into the existing note (update the relevant section(s), bump `date_consumed` to today) rather than creating a second note. Move the raw file to `raw/processed/` as usual, then log it with activity value `ingest` — this counts as a real ingest and will surface in the next newsletter — using the note's path plus a note like `(merged update)`.

Either way, this file is done — skip steps 3–11 and the "After processing each file" section below (their move/log already happened here).

### 3. Create output directory if missing

If `wiki/<category>/` does not exist, create it before writing the file.

### 4. Write the output file

Write directly to `wiki/<category>/kebab-case-title.md`. Do not output a filename line or any chat meta-text — start the file content directly with the YAML frontmatter.

### 5. Frontmatter

Begin every file with exactly this YAML structure:

```yaml
---
type: literature-note
source_url: [source_url value from the raw file, or "Unknown"]
author: [Author Name, or "Unknown"]
tags: [3-4 specific lowercase tags]
date_consumed: [today's date in YYYY-MM-DD format]
---
```

### 6. Summary section

Create a `## Summary` section. Write a maximum of 3 sentences covering the article's core thesis.

### 7. Core Concepts section

Create a `## Core Concepts` section. Extract the primary themes, methodologies, and entities.

**Mandatory:** Turn every major concept, technology, or person into an Obsidian WikiLink: `[[Concept Name]]` or `[[Person Name]]`.

### 8. Key Takeaways section

Create a `## Key Takeaways` section. Use a bulleted list of the most important arguments, statistics, or steps. Keep each bullet under 15 words for rapid scannability.

Example:

- **Architectural Shifts**: The transition from centralized databases to [[Decentralized Systems]].
- **Performance Metrics**: A 40% reduction in token consumption using active semantic filtering.

### 9. First Principles & Mental Models section (conditional)

**Only include this section if** a named mental model maps cleanly enough that a thoughtful reader would independently reach the same connection. If the link requires stretching, omit the section entirely — an absent section is better than a forced one.

When the bar is met, add this section after `## Key Takeaways`:

```markdown
## 🧠 First Principles & Mental Models

- **[[Mental Model Name]]**: [1 sentence — why this model applies and what it explains about the article's core claim]
```

Use WikiLinks for every model name so they connect across the vault. Include 1–3 entries maximum. Each entry must cover both a named model AND the first-principles reasoning it illuminates — not just a label.

Example (from an article on AI productivity claims):
- **[[Goodhart's Law]]**: When productivity becomes the target metric, workers optimize for its proxies rather than actual output — exactly the dynamic Newport documents with AI tool adoption.
- **[[Availability Bias]]**: The vividness of individual AI wins makes the aggregate productivity stagnation invisible — people generalize from memorable examples, not base rates.

### 10. Review Questions section

Create a `## 🃏 Review Questions` section at the end of the note (after First Principles & Mental Models, or after Key Takeaways if that section was omitted).

Generate exactly 3 Q&A pairs. Cover these angles in order:
1. The article's **core claim** — what is the central argument or finding?
2. A **key mechanism or data point** — how does it work, or what specific evidence supports it?
3. An **application or implication** — so what? How would you use or apply this?

Each answer should be 1–2 sentences, drawn only from the article.

```markdown
## 🃏 Review Questions

**Q1**: [question about the core claim]
**A**: [answer in 1–2 sentences]

**Q2**: [question about a key mechanism or data point]
**A**: [answer in 1–2 sentences]

**Q3**: [question about an application or implication]
**A**: [answer in 1–2 sentences]
```

### 11. Compilation rules

- Rely exclusively on the text provided. Do not use pre-trained memory to add unsubstantiated facts.
- Do not output any chat meta-text. Start directly with the YAML frontmatter.

## After processing each file

(Applies only to files that resulted in a brand-new note. Duplicate/near-duplicate files already moved their raw file and logged their row in step 2a — do not repeat this section for them.)

1. Move the source file from `/raw/` to `/raw/processed/`
2. Append a row to `kbm.log.md`:

```
| YYYY-MM-DD | wiki/<category>/note-slug.md | ingest |
```

Use the full relative path of the wiki note created (e.g. `wiki/science/entropy.md`), not the raw source filename.

## Expected outcome

1 raw file → 1 wiki note in `wiki/<category>/`

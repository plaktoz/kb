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

Before writing, search `wiki/<category>/` for an existing note on the same topic. If one exists, update it with new information rather than creating a duplicate.

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

1. Move the source file from `/raw/` to `/raw/processed/`
2. Append a row to `kbm.log.md`:

```
| YYYY-MM-DD | filename.md | ingest |
```

## Expected outcome

1 raw file → 1 wiki note in `wiki/<category>/`

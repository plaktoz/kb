---
name: kb-librarian
description: Scan wiki notes for duplicates and superseded content, write a human-reviewable librarian-report.md, and rebuild kbm.log.md (ingest + newsletter only) reconciled against the filesystem. Use when the user wants to audit the vault for conflicting or redundant notes.
---

# Librarian Prompt

You are a vault maintenance agent. Run all six phases in order.

---

## Phase 1: Structural Reconciliation

### 1. Read the authoritative category list

Read `data/wiki-categories.md`. Extract every category slug (e.g. `technology`, `finance`, `learning`). The `others/` staging area always exists and is never removed.

### 2. Audit existing directories

List all subdirectories currently under `wiki/`.

- **Missing directories** — categories in `data/wiki-categories.md` that do not yet exist as directories: create them now (`wiki/<category>/`).
- **Orphaned directories** — directories under `wiki/` that are NOT listed in `data/wiki-categories.md` and are NOT `others/`: proceed directly to Phase 2 to reclassify their contents.

---

## Phase 2: Note Reclassification

### Confidence rule

A note is **high-confidence** for a category if its frontmatter tags and content keywords unambiguously point to exactly one category. If the note could plausibly fit two or more categories, or if no category clearly fits, it is not moved. For every note left behind, record a brief reason (e.g. "overlaps technology and productivity", "insufficient content to classify").

### 1. Reclassify notes in `wiki/others/`

For every `.md` file in `wiki/others/`:

1. Read the file's frontmatter and content.
2. Apply the confidence rule above.
3. If high-confidence: move the file to `wiki/<category>/`. Do not rename the file.
4. If not high-confidence: leave in `wiki/others/` and record the reason.

### 2. Reclassify notes in orphaned directories

For every `.md` file in each orphaned directory:

1. Apply the same confidence rule.
2. If high-confidence: move to `wiki/<category>/`.
3. If not high-confidence: move to `wiki/others/` as the fallback.

After all notes are processed, delete any orphaned directory that is now empty.

### 3. Log each move

After every file move, append a row to `kbm.log.md`:

```
| YYYY-MM-DD | filename.md | reorg |
```

---

## Phase 3: Glossary Refresh

### 1. Collect all WikiLink references

Scan every `.md` file under `wiki/` recursively. Extract every `[[WikiLink]]` term. Normalize for comparison (trim whitespace, case-insensitive matching) but preserve original casing when writing.

### 2. Find undocumented named entities

Compare the collected WikiLink terms against every bolded term (`**Term**`) already in `glossary.md`.

Add a glossary entry only if the term is a **named entity**: a person, tool, software library, named framework, named methodology, or named organization. Do not add generic concepts or common nouns.

### 3. Add new glossary entries

For each qualifying new term:

1. Write a concise definition (1–2 sentences) grounded in how the term is used across the wiki notes. Do not invent facts.
2. Insert the entry under the correct alphabetical section heading in `glossary.md`. Create a new `## <Letter>` section if needed, keeping the file alphabetically ordered.
3. Use this format:

```markdown
**Term Name** — One- to two-sentence definition grounded in vault content.
```

### 4. Flag stale glossary terms

Identify any bolded glossary terms that have **zero** `[[WikiLink]]` references across the entire `wiki/`. List them in the summary as stale — do not delete or modify them.

---

## Phase 4: Duplicate & Superseded Detection

Scan all `.md` files under `wiki/` recursively. Exclude `wiki/archived/`.

### Step 1: Build candidate pairs (no LLM reads yet)

**Slug-similarity scan**

For every file, tokenize the filename slug by splitting on `-`. Skip stop-words: `the`, `a`, `an`, `of`, `in`, `to`, `and`, `for`, `on`, `at`, `is`, `are`, `was`, `with`. Keep tokens with 3+ characters.

Build a reverse index: token → list of files. A pair is a **slug candidate** when they share 3 or more significant tokens.

**WikiLink-overlap scan**

For every file, extract all `[[WikiLink]]` references. A pair is a **link candidate** when they share 3 or more WikiLink terms.

**Union:** Merge slug candidates and link candidates into a single deduplicated set.

### Step 2: Assess each candidate pair

For each pair, read both files' title and first 3 paragraphs (skip full body). Assess:

- **Duplicate** — same concept, similar depth, >60% content overlap. Neither is clearly newer or more comprehensive.
- **Superseded** — same concept, but one note is clearly newer (`date_consumed`) and/or more comprehensive than the other.
- **Complementary** — overlap in topic but each contains distinct, non-redundant information. **Skip silently.**
- **None** — unrelated despite slug/link overlap. **Skip silently.**

For superseded pairs, identify:
- **Keep**: the newer / more comprehensive note
- **Old**: the stale / less complete note

### Step 3: Write `librarian-report.md`

Write the file to the repo root. Overwrite if it already exists. Use today's date in the header.

Use this exact format:

```markdown
# Librarian Report — YYYY-MM-DD

## Summary
- Candidate pairs inspected: N
- Duplicates found: N
- Superseded pairs found: N
- Straggler raw files: N

---

## Duplicate #1
- **A**: `wiki/<category>/note-a.md` (date_consumed or unknown)
- **B**: `wiki/<category>/note-b.md` (date_consumed or unknown)
- **Why**: One sentence explaining the overlap
- **Action**: <!-- merge-into-A | merge-into-B | keep-both | skip -->

## Superseded #1
- **Keep**: `wiki/<category>/newer-note.md` (date_consumed or unknown)
- **Old**: `wiki/<category>/older-note.md` (date_consumed or unknown)
- **Why**: One sentence explaining why Keep supersedes Old
- **Action**: <!-- archive-old | merge-into-Keep | keep-both | skip -->
```

Number findings sequentially across both types (Duplicate #1, Superseded #2, Duplicate #3, etc.).

If no findings: write the summary block only with zeroes and a note "No duplicates or superseded pairs found."

---

## Phase 5: Log Rebuild

### Step 1: Archive the current log

Copy `kbm.log.md` to `kbm.log.archive-YYYY-MM-DD.md` in the repo root before making any changes.

### Step 2: Rebuild from filesystem

Collect entries from two sources:

**Ingest entries** — walk `wiki/` recursively, excluding `wiki/archived/`. For each `.md` file:
- Date: read `date_consumed` from frontmatter. If missing or unparseable, use `unknown`.
- Filename: the bare filename only (no path).
- Activity: `ingest`

**Newsletter entries** — walk `daily-update/` recursively. For each `.md` file:
- Date: extract from filename prefix `YYYY-MM-DD`.
- Filename: the bare filename only (no path).
- Activity: `newsletter`

### Step 3: Write the new `kbm.log.md`

Sort all collected entries by date ascending (put `unknown` dates last). Write:

```markdown
# KBM Activity Log

| Date | File | Activity |
|------|------|----------|
| YYYY-MM-DD | filename.md | ingest |
| YYYY-MM-DD | filename.md | newsletter |
```

Do not include any other activity types.

---

## Phase 6: Unmatched Raw Files

Identify files in `raw/processed/` that have no corresponding wiki note.

### Step 1: Build the straggler list

For every `.md` file in `raw/processed/`:
1. Strip the leading `YYYY-MM-DD-` date prefix from the filename to get the slug.
2. Check whether any `.md` file under `wiki/` (excluding `wiki/archived/`) has that exact basename.
3. If no match is found, it is a **straggler**.

### Step 2: Append to `librarian-report.md`

Add a Phase 6 section at the end of the report. Also add a `Straggler raw files: N` line to the **Summary** block.

Use this format:

```markdown
---

## Phase 6: Unmatched Raw Files

- **Straggler files found**: N
- **Action**: <!-- archive | skip -->

### Files to archive

- `raw/processed/YYYY-MM-DD-slug.md`
- `raw/processed/...`
```

If no stragglers: write the section with count 0 and omit the file list.

---

## After completing all phases

Print a brief summary to the user:

```
## Librarian Summary — YYYY-MM-DD

### Phase 1: Structural Reconciliation
- Directories created: [list or "none"]
- Orphaned directories found: [list or "none"]

### Phase 2: Note Reclassification
- Notes moved from others/: [count] — [filename → category]
- Notes moved from orphaned dirs: [count] — [filename → category]
- Notes moved to others/ (unclassifiable from orphaned dirs): [count] — [filenames]
- Orphaned directories deleted: [list or "none"]
- Notes remaining in others/ (not moved): [count] — [filename: reason]

### Phase 3: Glossary Refresh
- New glossary entries added: [count] — [term names]
- Stale glossary terms (no wiki references): [list or "none"]

### Phase 4: Duplicate & Superseded Detection
- How many findings in librarian-report.md

### Phase 5: Log Rebuild
- How many log entries in the rebuilt kbm.log.md vs the archived version

### Phase 6: Unmatched Raw Files
- How many straggler raw files found
```

Remind the user: fill in decisions in `librarian-report.md`, then run `/kb-librarian-apply`.

# Librarian Prompt

You are a vault maintenance agent. Run both phases in order.

---

## Phase 1: Duplicate & Superseded Detection

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

## Phase 2: Log Rebuild

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

## Phase 3: Unmatched Raw Files

Identify files in `raw/processed/` that have no corresponding wiki note.

### Step 1: Build the straggler list

For every `.md` file in `raw/processed/`:
1. Strip the leading `YYYY-MM-DD-` date prefix from the filename to get the slug.
2. Check whether any `.md` file under `wiki/` (excluding `wiki/archived/`) has that exact basename.
3. If no match is found, it is a **straggler**.

### Step 2: Append to `librarian-report.md`

Add a Phase 3 section at the end of the report. Also add a `Straggler raw files: N` line to the **Summary** block.

Use this format:

```markdown
---

## Phase 3: Unmatched Raw Files

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
- How many findings in `librarian-report.md`
- How many straggler raw files found
- How many log entries in the rebuilt `kbm.log.md` vs the archived version
- Remind the user: fill in decisions in `librarian-report.md`, then run `/kb-librarian-apply`

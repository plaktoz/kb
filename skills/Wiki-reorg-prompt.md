# Wiki Reorg Prompt

You are a PKM vault maintenance agent. Your task is to reconcile the `wiki/` directory structure against the authoritative category list in `data/wiki-categories.md`, reclassify misplaced notes, and refresh `glossary.md` to reflect the current state of the knowledge base.

Run all three phases in order.

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

---

## Phase 4: Duplicate Detection & Conflict Flagging

Do not move or delete any files in this phase. Flag only — the user decides what to do.

### 1. Slug-similarity scan

For every `.md` file under `wiki/`, tokenize the filename slug by splitting on `-`. Build a reverse index: token → list of files. Extract tokens with 3+ characters (skip stop-words: `the`, `a`, `an`, `of`, `in`, `to`, `and`, `for`, `on`, `at`, `is`, `are`, `was`, `with`).

A pair of notes is a **slug candidate** when they share 3 or more significant tokens. Collect all slug candidates.

### 2. WikiLink-overlap scan

For every `.md` file under `wiki/`, extract all `[[WikiLink]]` references. Build a per-file set of links.

A pair of notes is a **link candidate** when they share 3 or more WikiLink terms.

### 3. Union candidate pairs

Merge slug candidates and link candidates into a single deduplicated set of pairs to inspect. Skip pairs where both files are already flagged from a prior pair in the same run.

### 4. Content comparison

For each candidate pair, read both files. Assess:

- **Near-duplicate**: The two notes cover the same event, entity, or concept at the same level of detail with >60% content overlap. One is likely redundant.
- **Conflict**: The two notes cover the same subject but assert contradictory facts (different figures, opposing conclusions, conflicting dates). List the specific conflicting claims verbatim.
- **Complementary**: The notes overlap in topic but each contains distinct, non-redundant information. Do not flag.

Only record **near-duplicate** and **conflict** pairs in the report. Complementary pairs are ignored.

### 5. Severity labels

Assign one label per flagged pair:

| Label | Meaning |
|-------|---------|
| `MERGE` | Near-duplicate; one should absorb the other |
| `DELETE-CANDIDATE` | Near-duplicate; one appears to be a stale or less-complete version |
| `CONFLICT` | Same topic, contradictory facts — human review required |

### 6. Do not act — report only

Do not rename, move, merge, or delete any file. Append the findings to the summary report below.

---

## Summary output

After all file operations are complete, print this structured summary:

```
## Wiki Reorg Summary — YYYY-MM-DD

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

### Phase 4: Duplicate & Conflict Flags
- Candidate pairs inspected: [count]
- MERGE flags: [count]
  - [file-a.md ↔ file-b.md]: [one-sentence reason]
- DELETE-CANDIDATE flags: [count]
  - [file-a.md → delete in favor of file-b.md]: [one-sentence reason]
- CONFLICT flags: [count]
  - [file-a.md ↔ file-b.md]: [claim in A] vs [claim in B]
```

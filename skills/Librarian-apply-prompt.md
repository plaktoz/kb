# Librarian Apply Prompt

You are a vault maintenance agent executing decisions from a librarian report.

---

## Step 1: Determine input file

Check in this order:
1. If `librarian-followup.md` exists at repo root → read it as the input file.
2. Otherwise if `librarian-report.md` exists → read it as the input file.
3. If neither exists → stop and tell the user to run `/kb-librarian` first.

---

## Step 2: Parse findings

Read every finding block. A finding block starts with `## Duplicate #N` or `## Superseded #N`.

For each block, extract:
- **Type**: Duplicate or Superseded
- **Files**: the note paths listed under A/B or Keep/Old
- **Action line**: the text after `- **Action**: `

**Classify the action:**
- If the action line is `<!-- ... -->` (still a comment placeholder) → **undecided**
- If the action line is one of the valid actions below → **decided**
- Anything else → treat as **undecided** and include in the follow-up

Valid actions for Duplicate findings: `merge-into-A`, `merge-into-B`, `keep-both`, `skip`
Valid actions for Superseded findings: `archive-old`, `merge-into-Keep`, `keep-both`, `skip`

---

## Step 3: Execute decided findings

Process each decided finding in order.

### merge-into-A (Duplicate)
1. Read note B in full.
2. Read note A in full.
3. Merge B's Key Takeaways, Core Concepts WikiLinks, and any unique facts into note A without duplicating existing content.
4. Move note B to `wiki/archived/`.
5. Log to `kbm.log.md`: `| YYYY-MM-DD | merged B into A; archived B | librarian |`

### merge-into-B (Duplicate)
Same as merge-into-A with A and B swapped.

### merge-into-Keep (Superseded)
1. Read Old in full.
2. Read Keep in full.
3. Merge any unique content from Old into Keep.
4. Move Old to `wiki/archived/`.
5. Log to `kbm.log.md`: `| YYYY-MM-DD | merged Old into Keep; archived Old | librarian |`

### archive-old (Superseded)
1. Move Old to `wiki/archived/`.
2. Log to `kbm.log.md`: `| YYYY-MM-DD | archived Old (superseded by Keep) | librarian |`

### keep-both
No file changes. Do not add to follow-up — this is a conscious decision.

### skip
No file changes. Do not add to follow-up — this is a conscious decision.

---

## Step 4: Write follow-up file

Collect all **undecided** findings (action still a comment placeholder).

If any undecided findings exist:
- Write `librarian-followup.md` at repo root, **overwriting** any existing version.
- Use this format:

```markdown
# Librarian Follow-up — YYYY-MM-DD HH:MM

Decisions still needed: N

---

[paste each undecided finding block here, exactly as it appeared in the input file]
```

If zero undecided findings remain:
- If `librarian-followup.md` exists, delete it.
- Tell the user all decisions have been processed.

---

## Step 5: Summary

Print a brief summary:
- Findings executed: N (list each: type, files, action taken)
- Findings remaining in follow-up: N
- If `librarian-followup.md` was written: remind user to fill in decisions and re-run `/kb-librarian-apply`

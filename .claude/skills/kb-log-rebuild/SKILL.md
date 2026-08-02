---
name: kb-log-rebuild
description: Use when kbm.log.md is out of sync with the filesystem and a full librarian audit is not needed — rebuilds the log from wiki/ and daily-update/ without running vault maintenance phases.
---

# KB Log Rebuild

Rebuild `kbm.log.md` from scratch by walking the filesystem. Covers `ingest` and `newsletter` entries only.

---

## Step 1: Archive the current log

Copy `kbm.log.md` to `kbm.log.archive-YYYY-MM-DD.md` in the repo root before making any changes (use today's date).

## Step 2: Rebuild from filesystem

Collect entries from two sources:

**Ingest entries** — walk `wiki/` recursively, excluding `wiki/archived/`. For each `.md` file:
- Date: read `date_consumed` from frontmatter. If missing or unparseable, use `unknown`.
- Filename: full relative path from repo root (e.g. `wiki/science/entropy.md`).
- Activity: `ingest`

**Newsletter entries** — walk `daily-update/` recursively. For each `.md` file:
- Date: extract from filename prefix `YYYY-MM-DD`.
- Filename: full relative path from repo root (e.g. `daily-update/2026-08/2026-08-02-1.md`).
- Activity: `newsletter`

## Step 3: Write the new `kbm.log.md`

Sort all entries by date ascending; put `unknown` dates last. Write:

```markdown
# KBM Activity Log

| Date | File | Activity |
|------|------|----------|
| YYYY-MM-DD | wiki/<category>/note-slug.md | ingest |
| YYYY-MM-DD | daily-update/YYYY-MM/YYYY-MM-DD-N.md | newsletter |
```

Do not include any other activity types.

## Step 4: Print summary

```
## Log Rebuild — YYYY-MM-DD

- Archive: kbm.log.archive-YYYY-MM-DD.md (N entries)
- Rebuilt: kbm.log.md (N entries)
```

---
name: kb-run-issues
description: Fetch open GitHub issues from plaktoz/kb labelled "run skills", parse each issue body for skill names, run each skill in order, comment with results, and close the issue. Use when the user wants to dispatch skills queued as GitHub issues.
---

# Run Skills from GitHub Issues

Fetch all open issues on `plaktoz/kb` labelled **run skills**, execute the skills listed in each issue body, then comment and close each processed issue.

## Step 1: Fetch issues

Run:

```bash
gh issue list --repo plaktoz/kb --label "run skills" --state open --json number,title,body
```

Parse the JSON output. If the list is empty, print `No open "run skills" issues found.` and stop.

## Step 2: Parse skill names from each issue

For each issue, extract skill names from the body. Support these formats:

- Numbered list: `1. kb-daily-autocommit`
- Bullet list: `- kb-daily-autocommit`
- Slash-prefixed: `/kb-daily-autocommit`
- Bare name on its own line: `kb-daily-autocommit`

Normalise each match: strip leading whitespace, list markers (`-`, digits + `.`), and any leading `/`. The resulting token is the skill name (e.g. `kb-daily-autocommit`).

Ignore blank lines, comment lines starting with `#`, and any line that does not match a known skill name in the available-skills listing.

If no valid skill names are found in an issue, skip it and note it in the final summary.

## Step 3: Run each skill

For each parsed skill name, in the order they appear in the issue body:

1. Print: `Running skill: <skill-name> (from issue #<number>)`
2. Invoke the skill using the Skill tool with the exact skill name.
3. Collect the outcome: success (completed without error) or failure (error message).
4. Continue to the next skill regardless of failures — collect all errors.

## Step 4: Comment on the issue

After all skills for an issue have been attempted, post a comment using:

```bash
gh issue comment <number> --repo plaktoz/kb --body "<comment>"
```

Use this comment format:

```
## Skills run — YYYY-MM-DD

| Skill | Result |
|-------|--------|
| kb-daily-autocommit | ✅ success |
| kb-ingest | ❌ failed: <short error> |

Processed by Claude Code on YYYY-MM-DD.
```

## Step 5: Close the issue

After commenting, close the issue:

```bash
gh issue close <number> --repo plaktoz/kb
```

## Step 6: Print summary

After all issues have been processed, print:

```
## kb-run-issues summary — YYYY-MM-DD

Issues processed: N
Skills run: M (P succeeded, Q failed)

<list each issue number + title + outcome>
```

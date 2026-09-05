---
name: kb-issue-dispatch
description: Fetch open GitHub issues from plaktoz/kb labelled "run skills", parse each body with LLM intent extraction, run skills in parallel isolated worktrees, commit outputs, comment results, and close issues. Use when the user wants to dispatch skills queued as GitHub issues.
---

# Dispatch Skills from GitHub Issues

If the Workflow tool is available (Claude Code sessions), run:

```
name: "kb-issue-dispatch"
```

Wait for the workflow to complete, then report: how many issues were processed, how many fully succeeded vs failed, and any PR URLs opened.

**Fallback (no Workflow tool — e.g. Cowork):**

1. Run: `gh issue list --repo plaktoz/kb --label "run skills" --state open --json number,title,body`
2. If empty, stop and print `No open "run skills" issues found.`
3. For each issue in order:
   a. Read the body and use your judgment to map intent to skill names and arguments. Examples:
      - `"help me research AI agents"` → `kb-research-topic` with args `AI agents`
      - `"1. kb-daily-autocommit"` → `kb-daily-autocommit` with no args
      - `"/kb-newsletter"` → `kb-newsletter` with no args
   b. Only include skills that exist in the available-skills listing.
   c. Run each identified skill in order using the Skill tool. Continue on failure — collect all errors.
   d. After all skills finish, run `git status --porcelain`. If dirty: commit all changes and open a PR to `main` on branch `issue/<number>-<date>`.
   e. Post a results comment (markdown table: skill / result) to the issue.
   f. Close the issue: `gh issue close <number> --repo plaktoz/kb`
   g. If any skill failed, reopen: `gh issue reopen <number> --repo plaktoz/kb`
4. Print a summary: issues processed, skills run, failures, any PR URLs.

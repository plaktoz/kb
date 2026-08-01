---
name: kb-weekly
description: Run the full weekly knowledge pipeline: compound this week's notes into a weekly digest. Use when the user wants to run the complete weekly knowledge base update.
---

# Weekly Workflow

Run the full weekly knowledge pipeline in this exact sequence. After each step, continue to the next regardless of errors — collect all errors and report them at the end.

## Step 1: Weekly Compound

Invoke the `/kb-compound` skill and execute it.

If this step fails, note the error.

## End-of-run summary

After all steps are complete, print a summary in this format:

```
## Weekly Pipeline Summary — YYYY-WNN

- Weekly digest: [filename saved to weekly-update/] or FAILED: [error]
```

# Weekly Workflow Prompt

Run the full weekly knowledge pipeline in this exact sequence. After each step, continue to the next regardless of errors — collect all errors and report them at the end.

## Step 1: Weekly Compound

Read `skills/Weekly-compound-prompt.md` and execute the instructions exactly as written.

If this step fails, note the error.

## Step 2: Reorganize the information

Read `skills/Wiki-reorg-prompt.md` and execute the instructions exactly as written.

If this step fails, note the error.

## End-of-run summary

After all steps are complete, print a summary in this format:

```
## Weekly Pipeline Summary — YYYY-WNN

- Weekly digest: [filename saved to weekly-update/] or FAILED: [error]
```

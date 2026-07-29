---
name: kb-daily-autocommit
description: Run the full daily pipeline on a fresh branch, commit pipeline outputs, and open a PR into main. Use when cowork or automation should run the daily kb update unattended.
---

Run the following steps in order. Stop only if a git operation fails — pipeline failures are non-fatal and should be noted in the final commit message.

## Step 1: Prepare branch

### Pre-flight: check for untracked files

Run:

```bash
git status --porcelain wiki/ daily-update/ raw/processed/ kbm.log.md
```

Filter the output for lines beginning with `??`. If any exist, **stop immediately** and print:

```
Aborted: untracked files found in pipeline output paths. Resolve before running autocommit:
  <list each ?? file>
```

Do not proceed until the working tree is clean in those paths.

### Branch setup

```bash
git checkout main
git pull origin main
git checkout -b daily/$(date +%Y-%m-%d-%H%M)
```

Note the branch name for use in later steps.

## Step 2: Run the daily pipeline

Read `skills/Daily-workflow-prompt.md` and execute the instructions exactly as written.

Collect the end-of-run summary produced by that pipeline. You will need these counts:
- Number of wiki notes ingested
- Number of articles scraped
- Newsletter filename (if saved)

## Step 3: Check for output

Run:

```bash
git status --porcelain wiki/ daily-update/ raw/processed/ kbm.log.md
```

If the output is empty (nothing changed), do the following and then stop:
1. Append a row to `kbm.log.md`: `| YYYY-MM-DD | kb-daily-autocommit | ingest |` with a note `no output — branch skipped`
2. Run `git checkout main` to return to main
3. Delete the branch: `git branch -d <branch-name>`
4. Print: `No pipeline output — branch and commit skipped.`

## Step 4: Commit pipeline outputs

Stage only the pipeline output paths:

```bash
git add wiki/ daily-update/ raw/processed/ kbm.log.md
```

Build the commit message using the counts from Step 2 in this format:

```
daily run YYYY-MM-DD HH:MM — N notes ingested, M articles scraped, newsletter: <filename or none>
```

Commit:

```bash
git commit -m "<commit message>"
```

## Step 5: Push and open PR

```bash
git push -u origin <branch-name>
```

Then open a GitHub PR using the `gh` CLI:

```bash
gh pr create \
  --title "<commit message>" \
  --body "$(cat <<'EOF'
## Daily KB Run — YYYY-MM-DD HH:MM

<paste pipeline summary from Step 2 here>

> Merge to publish today's notes to main.
EOF
)" \
  --base main
```

Print the PR URL once created.

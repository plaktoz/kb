---
name: kb-daily-autocommit
description: Run the full daily pipeline on a fresh branch, commit pipeline outputs, and open a PR into main. Use when running the daily kb update unattended — e.g. on a schedule or via automation.
---

Run the following steps in order. Stop only if a git operation fails — pipeline failures are non-fatal and should be noted in the final commit message.

## Step 1: Prepare branch

Check for leftover untracked files in pipeline output paths:

```bash
git status --porcelain wiki/ daily-update/ raw/processed/ kbm.log.md
```

If any lines begin with `??`, stop immediately and print:

```
Aborted: untracked files found in pipeline output paths. Resolve before running autocommit:
  <list each ?? file>
```

Otherwise, create a fresh branch:

```bash
git checkout main
git pull origin main
git checkout -b daily/$(date +%Y-%m-%d-%H%M)
```

## Step 2: Run the daily pipeline

Invoke the `/kb-daily` skill and execute it.

Collect the end-of-run summary. Note:
- Number of wiki notes ingested
- Number of articles scraped
- Newsletter filename (if saved)

## Step 3: Check for output

```bash
git status --porcelain wiki/ daily-update/ raw/processed/ kbm.log.md
```

If the output is empty, do the following and stop:
1. Run `git checkout main`
2. Delete the branch: `git branch -d <branch-name>`
3. Print: `No pipeline output — branch and commit skipped.`

## Step 4: Commit pipeline outputs

```bash
git add wiki/ daily-update/ raw/processed/ kbm.log.md
```

Commit using this message format:

```
daily run YYYY-MM-DD HH:MM — N notes ingested, M articles scraped, newsletter: <filename or none>
```

```bash
git commit -m "<commit message>"
```

## Step 5: Push and open PR

```bash
git push -u origin <branch-name>
```

Open a PR using the `gh` CLI:

```bash
gh pr create \
  --title "<commit message>" \
  --body "$(cat <<'EOF'
## Daily KB Run — YYYY-MM-DD HH:MM

<insert end-of-run summary from Step 2>

> Merge to publish today's notes to main.
EOF
)" \
  --base main
```

Print the PR URL once created.

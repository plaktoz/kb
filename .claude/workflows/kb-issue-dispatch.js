export const meta = {
  name: 'kb-issue-dispatch',
  description: 'Fetch open "run skills" issues from plaktoz/kb, parse intent with LLM, run skills in parallel isolated worktrees, commit outputs, comment results, and close issues',
  phases: [
    { title: 'Fetch & Parse', detail: 'Fetch open issues and extract skill intent from each body' },
    { title: 'Execute', detail: 'Run skills in parallel isolated worktrees — one per issue' },
  ],
}

const FETCH_SCHEMA = {
  type: 'object',
  properties: {
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          number: { type: 'number' },
          title: { type: 'string' },
          body: { type: 'string' },
        },
        required: ['number', 'title', 'body'],
      },
    },
  },
  required: ['issues'],
}

const CATALOG_SCHEMA = {
  type: 'object',
  properties: {
    catalog: { type: 'string' },
  },
  required: ['catalog'],
}

const PARSE_SCHEMA = {
  type: 'object',
  properties: {
    number: { type: 'number' },
    skills: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' },
          args: { type: 'string' },
        },
        required: ['name', 'args'],
      },
    },
  },
  required: ['number', 'skills'],
}

const EXEC_SCHEMA = {
  type: 'object',
  properties: {
    issue_number: { type: 'number' },
    skills_run: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          name: { type: 'string' },
          args: { type: 'string' },
          success: { type: 'boolean' },
          error: { type: 'string' },
        },
        required: ['name', 'args', 'success'],
      },
    },
    pr_url: { type: 'string' },
    all_succeeded: { type: 'boolean' },
  },
  required: ['issue_number', 'skills_run', 'all_succeeded'],
}

// Phase 1: fetch issues + skill catalog in parallel — both needed before parsing can begin
phase('Fetch & Parse')

const [fetchResult, catalogResult] = await parallel([
  () => agent(
    'Run this command and return the issues array:\n\ngh issue list --repo plaktoz/kb --label "run skills" --state open --json number,title,body',
    { label: 'fetch-issues', schema: FETCH_SCHEMA, phase: 'Fetch & Parse' }
  ),
  () => agent(
    'Run this shell command and return its full stdout as the "catalog" string:\n\nfor f in .claude/skills/*/SKILL.md; do name=$(basename $(dirname "$f")); desc=$(grep \'^description:\' "$f" | head -1 | sed \'s/^description: //\'); echo "$name: $desc"; done',
    { label: 'list-skills', schema: CATALOG_SCHEMA, phase: 'Fetch & Parse' }
  ),
])

if (!fetchResult || !fetchResult.issues || fetchResult.issues.length === 0) {
  log('No open "run skills" issues found.')
  return { processed: 0 }
}

log(`Found ${fetchResult.issues.length} issue(s): ${fetchResult.issues.map(i => `#${i.number}`).join(', ')}`)

const catalog = catalogResult ? catalogResult.catalog : '(unavailable — use your knowledge of kb skills)'

// Phase 2: pipeline parse → execute; issue A executes as soon as it's parsed, without waiting for issue B
phase('Execute')

const results = await pipeline(
  fetchResult.issues,

  // Stage 1: extract skill intent from the issue body
  (issue) => agent(
    `Read this GitHub issue body and identify which kb skills the author wants to run.

Available skills (name: description):
${catalog}

Issue #${issue.number}: "${issue.title}"
Body:
---
${issue.body}
---

Use natural language understanding to map intent to skill names and arguments. Examples:
  "help me research AI agents"   → name: "kb-research-topic", args: "AI agents"
  "run the daily pipeline"       → name: "kb-daily-autocommit", args: ""
  "1. kb-newsletter"             → name: "kb-newsletter", args: ""
  "/kb-ingest"                   → name: "kb-ingest", args: ""

Rules:
- Only include skills present in the catalog above.
- Preserve the order they appear in the body.
- If no valid skills can be identified, return an empty skills array.`,
    { label: `parse-#${issue.number}`, schema: PARSE_SCHEMA, phase: 'Fetch & Parse' }
  ),

  // Stage 2: execute skills in an isolated worktree, commit output, comment, close/reopen
  (parsed, issue) => {
    if (!parsed || parsed.skills.length === 0) {
      log(`#${issue.number}: no valid skills identified — skipping`)
      return null
    }

    const skillsList = parsed.skills
      .map((s, i) => `${i + 1}. ${s.name}${s.args ? ` — args: "${s.args}"` : ''}`)
      .join('\n')

    const skillNames = parsed.skills.map(s => s.name).join(', ')

    return agent(
      `You are dispatching skills for GitHub issue #${issue.number} ("${issue.title}") in the plaktoz/kb repository. You are running in an isolated git worktree.

## Skills to run (in order)

${skillsList}

## Procedure

### Step 1 — Run each skill
Invoke each skill above using the Skill tool (pass the exact name and args). Record whether it succeeded or failed. Continue to the next skill regardless of outcome — collect all errors.

### Step 2 — Commit any uncommitted output
Run: git status --porcelain

If there are uncommitted changes:
  a. git add -A
  b. DATE=$(date +%Y-%m-%d)
  c. git checkout -b issue/${issue.number}-$DATE
  d. git commit -m "issue #${issue.number} dispatch — ${skillNames}

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>"
  e. git push -u origin issue/${issue.number}-$DATE
  f. gh pr create --repo plaktoz/kb --title "issue #${issue.number}: ${issue.title}" --body "Outputs from dispatching issue #${issue.number}.

Skills run: ${skillNames}

Triggered by: https://github.com/plaktoz/kb/issues/${issue.number}" --base main
  g. Note the PR URL from the output.

If the worktree is already clean (skills self-committed or produced no file output), skip this step entirely.

### Step 3 — Comment results on the issue
Post a comment summarising what ran. Build a markdown table with one row per skill. Use ✅ success or ❌ <short error>. If a PR was opened, append its URL. If the worktree was clean, note that instead.

gh issue comment ${issue.number} --repo plaktoz/kb --body "<your markdown comment>"

### Step 4 — Close the issue
gh issue close ${issue.number} --repo plaktoz/kb

### Step 5 — Reopen if any skill failed
If any skill failed: gh issue reopen ${issue.number} --repo plaktoz/kb

## Return
Return: issue_number (${issue.number}), skills_run (name, args, success, error for each), pr_url (empty string if no PR was opened), all_succeeded (true only if every skill succeeded).`,
      { label: `execute-#${issue.number}`, phase: 'Execute', isolation: 'worktree', schema: EXEC_SCHEMA }
    )
  }
)

const valid = results.filter(Boolean)
const succeeded = valid.filter(r => r.all_succeeded).length
const failed = valid.filter(r => !r.all_succeeded).length
const prs = valid.filter(r => r.pr_url).map(r => r.pr_url)

log(`Done: ${valid.length} issue(s) processed — ${succeeded} fully succeeded, ${failed} had failures (reopened).`)
if (prs.length > 0) log(`PRs opened: ${prs.join(', ')}`)

return { processed: valid.length, succeeded, failed, pr_urls: prs }

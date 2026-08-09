# Research: Loop Engineering Setup Guide
*Generated: 2026-08-09 | Scope: Hands-on, copy-paste step-by-step setup for building a greenfield personal project using Addy Osmani's loop engineering framework — covering all three workflows: new app, bug fix, and new feature*

---

## Research Outline

1. How the loop works — the full cycle visualized across all three workflows
2. Prerequisites & project scaffold — tools, repo structure, initial setup
3. Writing your CLAUDE.md — encoding project context so agents don't re-derive it
4. Configuring worktrees — isolated branches per agent task
5. Building the three workflows — hands-on setup for new app / bug fix / feature addition
6. Wiring sub-agents and MCP connectors — creation vs. verification agents, GitHub integration

---

## 1. How the Loop Works

### The Core Idea

Instead of *you* typing prompts to an AI agent, you build a **system** that types prompts for you. The system discovers work, delegates it to agents, verifies results, and opens PRs — all without you touching the keyboard.

> "You design the system that does it instead." — Addy Osmani

### The 6 Primitives

| Primitive | What it does | Where it lives |
|-----------|-------------|---------------|
| **Automations** | Scheduled discovery — finds work (CI failures, open issues, TODO comments) without you asking | Cron job, GitHub Actions, Claude Routines |
| **Worktrees** | Isolated git branches per task — agents never overwrite each other | `git worktree add` |
| **CLAUDE.md / Skills** | Persistent project knowledge — agents know your conventions without re-deriving them | `CLAUDE.md`, `.claude/skills/` |
| **Sub-agents** | Separate maker from checker — the model that wrote the code can't objectively grade it | `.claude/agents/` |
| **Connectors (MCP)** | Agents talk to real tools — GitHub, Linear, Slack | `.mcp.json`, `claude mcp add` |
| **State file** | Cross-run memory — the model forgets, the repo doesn't | `AGENTS.md` or `progress.md` |

### The Cycle (Visual)

```
┌─────────────────────────────────────────────────────────────────┐
│                        THE LOOP CYCLE                           │
│                                                                 │
│  [Trigger fires]                                                │
│       │  (cron / CI event / GitHub event / manual)             │
│       ▼                                                         │
│  [Automation reads repo state]                                  │
│       │  CI failures? Open issues? Spec file? TODO comments?    │
│       ▼                                                         │
│  [Writes findings → AGENTS.md state file]                       │
│       │                                                         │
│       ▼                                                         │
│  [For each finding: spawn isolated worktree]                    │
│       │  git worktree add ../agent-task-1 -b agent/task-1       │
│       ▼                                                         │
│  [Sub-agent A (Creator) works in worktree]                      │
│       │  reads CLAUDE.md + state file, writes code              │
│       ▼                                                         │
│  [Sub-agent B (Verifier) reviews the diff]                      │
│       │  adversarial check: tries to find problems              │
│       ▼                                                         │
│  [MCP Connector opens PR on GitHub]                             │
│       │  updates Linear ticket, pings Slack                     │
│       ▼                                                         │
│  [YOU review the PR — approve or reject]                        │
│       │                                                         │
│       └──────────[merge] ──────────► [loop repeats]             │
└─────────────────────────────────────────────────────────────────┘
```

### Three Workflow Variations

The cycle is the same for all three workflows. What changes is **what feeds the trigger** and **what the creator agent reads**.

```
WORKFLOW A — NEW APP
Trigger:    You drop a spec.md file into the repo
Agent reads: spec.md → scaffolds entire project structure
Output:     PR with full app scaffold

WORKFLOW B — BUG FIX
Trigger:    CI fails / you drop a bug report into issues/
Agent reads: CI failure logs + CLAUDE.md
Output:     PR with fix + tests

WORKFLOW C — NEW FEATURE
Trigger:    You create a GitHub Issue or drop feature.md
Agent reads: feature spec + existing codebase via CLAUDE.md
Output:     PR with implementation
```

---

## 2. Prerequisites & Project Scaffold

### Step 1 — Install Claude Code

**macOS / Linux / WSL:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows PowerShell:**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Verify installation:**
```bash
claude --version
```

You'll be prompted to log in with your claude.ai account on first run.

---

### Step 2 — Create Your Project Repo

```bash
# Create project directory
mkdir my-loop-project
cd my-loop-project

# Initialize git
git init
git branch -M main

# Create on GitHub (requires GitHub CLI)
gh repo create my-loop-project --private --source=. --remote=origin
git push -u origin main
```

---

### Step 3 — Scaffold the Loop Engineering Directory Structure

Run these commands to create the skeleton:

```bash
# Core loop engineering directories
mkdir -p .claude/agents
mkdir -p .claude/skills
mkdir -p .claude/hooks

# State tracking
touch AGENTS.md

# Spec and issue inboxes
mkdir -p specs
mkdir -p issues

# Placeholder for your app source
mkdir -p src
```

Your project tree should look like this:

```
my-loop-project/
├── .claude/
│   ├── agents/         ← sub-agent definitions
│   ├── skills/         ← reusable workflow skills
│   └── hooks/          ← shell scripts triggered by agent lifecycle
├── .github/
│   └── workflows/      ← GitHub Actions automation (created later)
├── .mcp.json           ← MCP connector config (created later)
├── AGENTS.md           ← state file: what's done / in progress / queued
├── CLAUDE.md           ← project knowledge for agents
├── specs/              ← drop spec.md here to trigger new app workflow
├── issues/             ← drop bug reports here to trigger fix workflow
└── src/                ← your application source code
```

---

### Step 4 — Run /init to Generate a Starter CLAUDE.md

Inside your project directory, start Claude Code and run:

```bash
cd my-loop-project
claude
```

Then inside the session:

```
/init
```

Claude will analyze your project and generate a starter `CLAUDE.md`. You'll refine it in the next section.

---

## 3. Writing Your CLAUDE.md

`CLAUDE.md` is the most important file in the loop. Every agent reads it at the start of every session. It is **not** for documenting what the code does — it's for the non-obvious things agents can't derive from the code alone.

### What to Put In It

- Build commands (`npm run dev`, `go build ./...`, `make test`)
- Test commands and how to run them
- Coding conventions specific to this project
- Directory layout decisions
- "Never do X" rules
- Architecture decisions that aren't obvious

### What NOT to Put In It

- Directory structure (agents can see it)
- Package names (agents can read package.json)
- Long tutorials or theory
- Anything that changes per-task

### Starter CLAUDE.md Template (copy and customize)

```markdown
# Project: my-loop-project

## Commands
- Install: `npm install`
- Dev server: `npm run dev`
- Tests: `npm test`
- Lint: `npm run lint`
- Build: `npm run build`

## Project Structure
- `src/` — application source
- `src/api/` — backend endpoints
- `src/components/` — UI components
- `specs/` — spec files that trigger new-app agent workflow
- `issues/` — bug reports that trigger fix workflow

## Conventions
- Use 2-space indentation
- File names: kebab-case (e.g. `user-profile.ts`)
- Function names: camelCase
- API handlers live in `src/api/handlers/`
- Always run `npm run lint` before committing
- Write tests for every new function in `src/`

## Never
- Push directly to main
- Skip tests
- Delete files from `specs/processed/` or `issues/processed/`

## Agent Workflow Notes
- State file is AGENTS.md — update it after every task
- Spec files in `specs/` trigger new-app workflow
- Bug reports in `issues/` trigger bug-fix workflow
- GitHub Issues trigger feature workflow
- All agent branches are prefixed `agent/`
```

### Keep It Under 200 Lines

Claude reads the entire file every session. Over 200 lines, adherence drops. Use `.claude/rules/` for topic-specific detail:

```bash
# Create rules for specific concerns
mkdir -p .claude/rules
touch .claude/rules/testing.md
touch .claude/rules/api-design.md
touch .claude/rules/security.md
```

Example `.claude/rules/testing.md`:
```markdown
---
paths:
  - "src/**/*.test.ts"
  - "tests/**/*"
---

# Testing Rules
- Every new function needs at least one test
- Use `describe` + `it` blocks
- Mock external APIs in tests, never call real ones
- Test file lives next to source file: `user.ts` → `user.test.ts`
```

---

### Set Up the AGENTS.md State File

This file persists memory across runs. Agents read it to know what's done, in progress, or queued.

```bash
cat > AGENTS.md << 'EOF'
# Agent State File
*Updated by agents after each run. Humans should not edit this directly.*

## Completed
<!-- agents mark tasks done here -->

## In Progress
<!-- agents mark tasks active here -->

## Queued
<!-- new tasks appear here — add spec/issue references -->

## Log
| Date | Task | Branch | PR | Status |
|------|------|--------|----|--------|
EOF
```

---

## 4. Configuring Worktrees

Worktrees give each agent its own isolated copy of the repo. Without them, two agents running at the same time overwrite each other's files.

### Basic Git Worktree Commands

```bash
# Create an isolated worktree for a task
git worktree add ../agent-fix-login-bug -b agent/fix-login-bug

# List all active worktrees
git worktree list

# Remove a worktree after the PR is merged
git worktree remove ../agent-fix-login-bug

# Prune stale worktree references
git worktree prune
```

### Automatic Worktree Isolation in Sub-agents

Add `isolation: worktree` to a sub-agent definition and Claude Code automatically creates and cleans up the worktree:

```markdown
---
name: implementer
description: Implements features and fixes in an isolated worktree
isolation: worktree
---
```

When this agent runs, Claude Code:
1. Creates a fresh git worktree on a new branch
2. Runs the agent inside it
3. Cleans up the worktree automatically if nothing was committed

### Manual Parallel Worktree Setup (for running multiple agents at once)

```bash
# Set up 3 worktrees for 3 parallel tasks
git worktree add ../agent-task-1 -b agent/task-1
git worktree add ../agent-task-2 -b agent/task-2
git worktree add ../agent-task-3 -b agent/task-3

# Run an agent in each (in separate terminal tabs)
cd ../agent-task-1 && claude -p "Fix the login timeout bug described in issues/login-timeout.md"
cd ../agent-task-2 && claude -p "Add rate limiting to the API as described in specs/rate-limiting.md"
cd ../agent-task-3 && claude -p "Write missing tests for src/api/handlers/"
```

---

## 5. Building the Three Workflows

### Workflow A: New App (Spec → Scaffold)

**How it works:** You drop a `spec.md` file into `specs/`. An agent reads it and scaffolds the entire app.

#### Step A1 — Write a Spec File

Create `specs/my-app-spec.md`:

```markdown
# App Spec: Todo API

## What it is
A REST API for managing todo items. Users can create, read, update, and delete todos.

## Tech stack
- Runtime: Node.js + TypeScript
- Framework: Express
- Database: SQLite (file-based, no setup needed)
- Testing: Jest

## Endpoints
- GET /todos — list all todos
- POST /todos — create a todo { title: string }
- PUT /todos/:id — update a todo { title?, completed? }
- DELETE /todos/:id — delete a todo

## File structure expected
src/
  index.ts         — server entry point
  routes/
    todos.ts       — all todo endpoints
  db/
    schema.ts      — database schema and connection
  types.ts         — shared TypeScript types

## Done when
- All endpoints return correct status codes
- npm test passes
- npm run build succeeds
```

#### Step A2 — Create the Scaffold Sub-agent

Create `.claude/agents/scaffolder.md`:

```markdown
---
name: scaffolder
description: Scaffolds a new application from a spec.md file. Use when a spec file appears in specs/.
isolation: worktree
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

You are a scaffolding agent. Your job is to read a spec file and build a working application from scratch.

Steps:
1. Read the spec file provided
2. Create all directories and files described in the spec
3. Implement each piece described — no stubs, working code only
4. Write tests for every function
5. Run `npm install` and `npm test` — fix any failures before stopping
6. Update AGENTS.md: move the spec from Queued to Completed
7. Open a PR titled "feat: scaffold [app name] from spec"

Do not stop until `npm test` passes.
```

#### Step A3 — Run the Scaffold Agent

```bash
# From your project root
claude --agent scaffolder -p "Scaffold the app from specs/my-app-spec.md. Save output to src/."
```

Or inside a Claude session:
```
Read specs/my-app-spec.md and scaffold the full application. Use the scaffolder agent.
```

---

### Workflow B: Bug Fix (CI Failure → Fix → PR)

**How it works:** A CI test fails or you drop a bug report into `issues/`. An agent reads it, finds the root cause, writes a fix, and opens a PR.

#### Step B1 — Write a Bug Report

Create `issues/login-timeout.md`:

```markdown
# Bug: Login times out on mobile

## Symptom
Users on mobile devices get logged out after 30 seconds. Desktop works fine.

## Steps to reproduce
1. Log in on a mobile browser
2. Wait 30 seconds
3. Try to navigate — redirected to login page

## Expected
Session should last 24 hours

## Error log
```
[2026-08-09 14:23:01] SessionExpiredError: token expired
  at validateToken (src/auth/middleware.ts:42)
  at Layer.handle (node_modules/express/lib/router/layer.js:95)
```

## Suspected location
src/auth/middleware.ts around line 42
```

#### Step B2 — Create the Bug-Fix Sub-agents

Create `.claude/agents/fixer.md`:

```markdown
---
name: fixer
description: Fixes bugs from issue reports. Reads an issue file, traces root cause, writes fix and tests.
isolation: worktree
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

You are a bug-fix agent. Your job is to read a bug report and fix the issue.

Steps:
1. Read the issue file
2. Find the root cause — read the relevant source files
3. Write the minimal fix (do not refactor surrounding code)
4. Write or update tests that would have caught this bug
5. Run `npm test` — fix any failures
6. Update AGENTS.md: log this fix in the table
7. Open a PR titled "fix: [short bug description]"
   - PR description must include: root cause, what was changed, how to test

Do not change code outside the minimum needed to fix the bug.
```

Create `.claude/agents/verifier.md`:

```markdown
---
name: verifier
description: Reviews a code diff adversarially. Tries to find problems, regressions, or incomplete fixes.
allowed-tools:
  - Read
  - Bash
---

You are a code reviewer. Your job is to adversarially verify a fix.

Steps:
1. Read the diff or changed files
2. Try to REFUTE the fix — find:
   - Edge cases the fix misses
   - New bugs introduced
   - Tests that pass but shouldn't
   - Security issues
3. If the fix is correct: respond with APPROVED + one-line summary
4. If the fix has problems: respond with REJECTED + specific list of issues

Be skeptical. The model that wrote the fix is too lenient with itself.
```

#### Step B3 — Run the Bug Fix Workflow

```bash
# Run fixer on the issue
claude --agent fixer -p "Fix the bug described in issues/login-timeout.md"

# Then run verifier on the result
# (Claude will automatically spawn verifier if you wire it in, or run manually:)
claude --agent verifier -p "Review the changes on branch agent/fix-login-timeout"
```

#### Step B4 — Automate with GitHub Actions (so CI failures trigger it automatically)

Create `.github/workflows/auto-fix.yml`:

```yaml
name: Auto Fix on Test Failure
on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  auto-fix:
    if: github.event.workflow_run.conclusion == 'failure'
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
      id-token: write
      actions: read
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            The CI workflow just failed. 
            1. Read the CI failure logs
            2. Identify the failing test(s)
            3. Find the root cause in the source code
            4. Write a minimal fix
            5. Run the tests to confirm they pass
            6. Open a PR titled "fix: auto-fix CI failure [test name]"
          claude_args: "--max-turns 10"
```

> **Before this runs:** Add your `ANTHROPIC_API_KEY` to GitHub Secrets:
> Settings → Secrets and variables → Actions → New repository secret

---

### Workflow C: New Feature (Issue → Implement → PR)

**How it works:** You create a GitHub Issue describing the feature. The agent reads it, implements it, and opens a PR.

#### Step C1 — Create a Feature Issue

```bash
# Create a GitHub Issue using GitHub CLI
gh issue create \
  --title "Add pagination to GET /todos" \
  --body "## Feature request
  
The GET /todos endpoint returns all todos at once.
For large datasets this is slow.

## What to build
Add cursor-based pagination:
- Query params: ?limit=20&cursor=<last_id>
- Response: { todos: [...], nextCursor: string | null }

## Acceptance criteria
- Existing tests still pass
- New tests cover: empty list, single page, multi-page, last page
- Works with the SQLite db setup in src/db/schema.ts
"
```

#### Step C2 — Create the Feature Agent

Create `.claude/agents/feature-builder.md`:

```markdown
---
name: feature-builder
description: Implements new features from GitHub Issues. Reads the issue, implements the feature, writes tests, opens PR.
isolation: worktree
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

You are a feature implementation agent. Your job is to build a feature described in a GitHub Issue.

Steps:
1. Read the issue (title + body + acceptance criteria)
2. Read CLAUDE.md to understand conventions
3. Read the relevant existing source files — understand the current implementation
4. Implement the feature with minimal changes to existing code
5. Write tests covering all acceptance criteria
6. Run `npm test` — fix any failures
7. Update AGENTS.md: log this feature in the table
8. Open a PR:
   - Title: "feat: [feature name]"
   - Body: what was built, how to test, which issue it closes (Closes #N)

Do not add features beyond what the issue describes.
```

#### Step C3 — Wire GitHub Issues to Auto-trigger the Agent

Create `.github/workflows/issue-to-pr.yml`:

```yaml
name: Issue to PR
on:
  issues:
    types: [labeled]

jobs:
  implement-feature:
    if: contains(github.event.label.name, 'auto-implement')
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write
      issues: write
      id-token: write
      actions: read
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Implement the feature described in GitHub Issue #${{ github.event.issue.number }}.
            Issue title: ${{ github.event.issue.title }}
            Issue body:
            ${{ github.event.issue.body }}
            
            Use the feature-builder agent workflow.
            When done, open a PR that closes this issue.
          claude_args: "--max-turns 15"
```

To trigger: add the label `auto-implement` to any issue.

#### Step C4 — Or Trigger Manually via @claude Mention

Install the Claude GitHub App (run `/install-github-app` inside a `claude` session), then in any Issue comment:

```
@claude implement this feature and open a PR
```

Claude will read the issue, implement it, and reply with a PR link.

---

## 6. Wiring Sub-agents and MCP Connectors

### Sub-agent File Format (Full Reference)

Each sub-agent is a markdown file in `.claude/agents/`. Frontmatter configures it, body is the system prompt.

```markdown
---
name: my-agent                    # slug, no spaces
description: What this agent does # used for auto-matching
model: claude-haiku-4-5           # optional: cheaper model for simple tasks
isolation: worktree               # optional: run in fresh git branch
memory: true                      # optional: agent remembers across sessions
allowed-tools:                    # optional: restrict what tools it can use
  - Read
  - Write
  - Edit
  - Bash
  - mcp__github__create_pull_request
---

Your agent system prompt goes here.
```

### The 3-Agent Team Pattern

```
Explorer (fast, read-only)        →  find scope
  │
  ▼
Implementer (isolated worktree)   →  write the code
  │
  ▼
Verifier (high-effort, skeptical) →  find problems
```

Create `.claude/agents/explorer.md`:
```markdown
---
name: explorer
description: Fast read-only agent for understanding scope before implementation
model: claude-haiku-4-5
allowed-tools:
  - Read
  - Bash
---

You are a read-only scope agent. Your job is to understand the codebase before any changes are made.

Given a task:
1. Read CLAUDE.md
2. Find all files relevant to the task
3. Summarize: what exists, what needs to change, what risks exist
4. Output a structured brief for the implementer agent

Do NOT write or edit any files.
```

### Connect GitHub MCP (for agents to open PRs automatically)

**Option 1 — Project-scoped (shared with team):**

Create `.mcp.json` in your project root:
```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

Then set the environment variable:
```bash
export GITHUB_TOKEN=your_github_personal_access_token
```

**Option 2 — User-scoped (just for you, all projects):**
```bash
claude mcp add --scope user github -- npx -y @modelcontextprotocol/server-github
```

**Verify connection:**
```bash
claude mcp list
# Should show: ✔ Connected  github
```

### Connect Linear MCP (optional, for ticket tracking)

```bash
claude mcp add --transport http linear https://mcp.linear.app/sse
```

Then inside a Claude session:
```
/mcp
# Select linear → Authenticate → sign in via browser
```

### Set Up Daily Triage Routine (Cloud Automation)

This runs every morning, reads open issues and CI state, and updates `AGENTS.md` with what needs doing.

Inside a `claude` session:
```
/schedule daily at 9am, triage open GitHub issues and CI failures.
For each actionable item:
1. Add it to the Queued section of AGENTS.md
2. Include: issue number, title, suspected file, priority (high/medium/low)

Then summarize what was found in a Slack message.
```

Or create a GitHub Actions scheduled workflow manually:

Create `.github/workflows/daily-triage.yml`:
```yaml
name: Daily Triage
on:
  schedule:
    - cron: "0 9 * * 1-5"   # 9am weekdays UTC

jobs:
  triage:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: read
      pull-requests: read
      id-token: write
      actions: read
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 1

      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: |
            Morning triage. Do the following:
            1. List all open GitHub Issues, grouped by label
            2. Check if any CI workflows failed in the last 24 hours
            3. Update AGENTS.md:
               - Move stale in-progress items to Queued if no branch activity in 2 days
               - Add new actionable items to Queued with issue number and priority
            4. Commit the updated AGENTS.md with message "chore: daily triage [date]"
          claude_args: |
            --allowedTools "mcp__github__list_issues,mcp__github__list_pull_requests,mcp__github__get_file_contents"
```

### Full `.mcp.json` Reference

```json
{
  "mcpServers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./src"]
    }
  }
}
```

### Add Lint-on-Save Hook (Quality Gate)

Create `.claude/hooks/lint-after-edit.sh`:
```bash
#!/bin/bash
# Runs after every file edit — keeps code clean automatically

FILE_PATH=$(echo "$1" | jq -r '.tool_input.file_path // empty')

if [[ "$FILE_PATH" == *.ts || "$FILE_PATH" == *.js ]]; then
  npm run lint -- "$FILE_PATH" 2>&1
fi
```

```bash
chmod +x .claude/hooks/lint-after-edit.sh
```

Register it in `.claude/settings.json`:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/lint-after-edit.sh"
          }
        ]
      }
    ]
  }
}
```

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://addyosmani.com/blog/loop-engineering/
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/github-actions
- https://code.claude.com/docs/en/mcp-quickstart
- https://code.claude.com/docs/en/routines

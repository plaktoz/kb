# Synthesis: Loop Engineering + Context Engineering
*2026-08-09 | Connects: [[Loop Engineering]], [[Context Engineering]], [[Claude Code]], [[Spec-Driven Development]], [[AI Coding Agent Patterns]]*

---

## The Big Insight

Loop engineering **is** context engineering applied at the systems level.

The loop works not because agents are smart — it works because the context they receive is engineered carefully. CLAUDE.md, skills, worktrees, state files, and hooks are all context delivery mechanisms. Get the context right and the agents produce reliable output. Get it wrong and you get hallucinated code, spec drift, and comprehension debt.

> "Curating what the model sees to get better results." — Birgitta Böckeler on context engineering

The leverage point in a loop isn't the agent model. It's the **signal-to-noise ratio** of what the model receives before it writes a single line.

---

## How the Pieces Fit Together

```
┌─────────────────────────────────────────────────────────────┐
│              CONTEXT LAYERS (loaded at session start)        │
│                                                              │
│  AGENTS.md / CLAUDE.md  ← always-on: conventions, commands  │
│  .claude/rules/         ← path-scoped: fires per file type   │
│  .claude/skills/        ← lazy-loaded: fires on demand       │
│  Hooks                  ← deterministic: fires on lifecycle  │
│  State file (AGENTS.md) ← cross-run memory: what's done/queued│
└─────────────────────────────────────────────────────────────┘
                          ▼ feeds into ▼
┌─────────────────────────────────────────────────────────────┐
│                   THE AGENT TEAM                             │
│                                                              │
│  Explorer  (read-only, fast model)    → find scope           │
│  Implementer (worktree-isolated)      → write code           │
│  Verifier   (skeptical, high-effort)  → find problems        │
└─────────────────────────────────────────────────────────────┘
                          ▼ outputs ▼
┌─────────────────────────────────────────────────────────────┐
│                   AUTOMATION LAYER                           │
│                                                              │
│  Trigger (cron / GitHub event / API / spec file drop)        │
│  Worktree per task (parallel, isolated, no overwrites)       │
│  MCP connectors (GitHub PR, Linear ticket, Slack ping)       │
└─────────────────────────────────────────────────────────────┘
```

---

## 5 Principles That Tie It All Together

### 1. The model forgets. The repo doesn't.

Everything that needs to persist across sessions lives in files — not in your memory, not in chat history.

| What to persist | Where |
|----------------|-------|
| Project conventions | `CLAUDE.md` |
| What's done / queued | `AGENTS.md` (state file) |
| Task-specific workflow | `.claude/skills/<name>.md` |
| Quality gates | `.claude/hooks/` scripts |
| Tool connections | `.mcp.json` |

The state file is the linchpin. Without it, each loop run starts blind. With it, the loop accumulates knowledge across runs the same way a senior engineer does.

---

### 2. Context has a loading strategy — choose it deliberately

Three ways context reaches an agent, each with different tradeoffs:

| Loader | Example | Tradeoff |
|--------|---------|----------|
| **Always-on** | `CLAUDE.md` | Reliable, but uses tokens every session |
| **Lazy (LLM-triggered)** | `.claude/skills/` | Flexible, but non-deterministic |
| **Deterministic (hooks)** | `PostToolUse` lint script | Guaranteed to fire, but must be pre-programmed |

**Rule of thumb:**
- Put *conventions* in `CLAUDE.md` (always-on)
- Put *workflow procedures* in skills (lazy)
- Put *quality gates* in hooks (deterministic)

Dumping everything into `CLAUDE.md` is the most common mistake — it hits the 200-line soft ceiling fast and buries critical rules under noise. "Lost in the middle" is real: irrelevant content in large windows actively degrades output quality.

---

### 3. The Verifier isn't optional

LLMs produce invalid or incorrect code **10–20% of the time** on complex edits. The model that wrote the code is too lenient grading its own homework.

This is why the Verifier sub-agent exists as a **separate model call** with a different system prompt — one explicitly told to be adversarial and try to find problems. One sub-agent creates, another refutes. The split mirrors the Coordinator → Implementor → Verifier architecture that delivers 34.2% faster task completion in multi-agent systems.

**Practical setup:**
```markdown
# .claude/agents/verifier.md
---
name: verifier
description: Adversarial reviewer. Tries to find problems with a proposed change.
model: claude-opus-4-8   ← high-effort model for the check
allowed-tools:
  - Read
  - Bash
---

Try to REFUTE the changes. Look for:
- Edge cases the fix misses
- Regressions introduced
- Tests that pass but shouldn't
- Security issues

Respond: APPROVED (one line) or REJECTED (bulleted list of issues).
```

---

### 4. Worktrees × Parallel Agents = ~1.3x speedup

Parallel agent execution across isolated worktrees adds a measurable ~1.3x speedup on top of the base multi-agent benefit. The isolation is what makes parallelism safe — without separate worktrees, agents running at the same time produce merge conflicts and corrupted state.

The rule: **one task = one worktree = one branch.**

```bash
# Each task gets its own fresh copy of the repo
git worktree add ../agent-fix-auth   -b agent/fix-auth
git worktree add ../agent-add-pagination -b agent/add-pagination
git worktree add ../agent-write-tests -b agent/write-tests
```

Or use `isolation: worktree` in sub-agent frontmatter to let Claude Code handle this automatically.

---

### 5. AGENTS.md does double duty

`AGENTS.md` serves two roles simultaneously:

1. **State file** — tracks what's done, in progress, queued. The loop's memory.
2. **Cross-tool context file** — the open standard (Linux Foundation / Agentic AI Foundation) read by 18+ tools including Codex, Cursor, Devin, and Claude Code.

This means the same file that keeps your loop's state also onboards any other agent tool you add later. Write it as a state file; get cross-tool compatibility for free.

**AGENTS.md structure that serves both roles:**
```markdown
# AGENTS.md

## Build & Test
- Install: `npm install`
- Test: `npm test`
- Lint: `npm run lint`

## Never Modify
- `.env`, `package-lock.json`, `.github/workflows/`

## Agent State
### Completed
| Date | Task | Branch | PR |
|------|------|--------|----|

### In Progress
### Queued
```

Keep it under 200 lines. Anything longer buries the critical rules.

---

## The Three Workflows at a Glance

| Workflow | Trigger | Agent reads | Output |
|----------|---------|-------------|--------|
| **New App** | `specs/app-spec.md` dropped | spec + CLAUDE.md | PR with full scaffold |
| **Bug Fix** | CI fails / `issues/bug.md` dropped | failure log + CLAUDE.md | PR with minimal fix + tests |
| **New Feature** | GitHub Issue labeled `auto-implement` | issue body + CLAUDE.md | PR closing the issue |

All three follow the same cycle: **trigger → explore → implement (worktree) → verify → PR via MCP**.

---

## What to Build First (Sequenced)

If you're starting from scratch, build in this order — each step makes the next one work better:

```
Day 1 ── Set up repo + install Claude Code
         Write CLAUDE.md (start small: just commands + Never rules)
         Create AGENTS.md state file

Day 2 ── Add .claude/agents/fixer.md + verifier.md
         Test manually: drop a bug report, run fixer, run verifier

Day 3 ── Add .mcp.json with GitHub MCP
         Test: agent opens a real PR automatically

Day 4 ── Add GitHub Actions workflow for auto-fix on CI failure
         Test: break a test intentionally, watch the loop run

Day 5 ── Add spec-driven scaffold workflow
         Write a spec.md, let the scaffolder build the app

Week 2 ─ Add daily triage routine (cloud or cron)
          Add feature workflow (GitHub Issue → PR)
          Tune CLAUDE.md based on what agents got wrong
```

---

## What Can Go Wrong (and How to Fix It)

| Problem | Cause | Fix |
|---------|-------|-----|
| Agent ignores CLAUDE.md rules | File too long, rules buried | Keep under 200 lines; move detail to `.claude/rules/` |
| Agent edits wrong files | No ScopeGuard | Add "Never modify" list to AGENTS.md; use `allowed-tools` in agent frontmatter |
| Loop produces code you don't understand | Comprehension debt | Read every PR before merging; loop ≠ autopilot |
| Agents clobber each other | No worktree isolation | Add `isolation: worktree` or create worktrees manually |
| Verifier is too lenient | Same model used for both | Use a higher-effort model (`claude-opus-4-8`) for verifier |
| Token costs spiral | No `--max-turns` cap | Set `--max-turns 10` in Claude Args; audit routines monthly |
| Spec drifts from code | Spec not treated as living contract | Add CI validation gate that checks spec against implementation |

---

## Related Notes

- [[context-engineering-coding-agents]] — CLAUDE.md, Skills, Hooks, Subagents explained as context delivery mechanisms
- [[spec-driven-ai-code-generation-multi-agent-systems]] — Coordinator/Implementor/Verifier architecture, 34.2% speedup data
- [[ai-coding-agent-patterns]] — codebase indexing, relevance scoring, diff strategies, error recovery loops
- [[claude-md-files-customizing-claude-code]] — CLAUDE.md best practices and `/init` command
- [[agents-md-vs-claude-md-context-files]] — cross-tool strategy, AGENTS.md as open standard

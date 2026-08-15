---
source_url: https://ai-tldr.dev/learn/ai-coding-tools/coding-agents-assistants/agents-md-claude-md/
author: Unknown
date: 2026-06-12
---

# AGENTS.md and CLAUDE.md: Context Files Explained

AGENTS.md and CLAUDE.md are Markdown files placed in your repository that coding agents read before taking any action — functioning as an onboarding document for tools like Claude Code, Codex, Cursor, and Devin.

**Key distinction:**
- **CLAUDE.md** — Anthropic's native format, loaded automatically by Claude Code with hierarchical layering (global → project → local)
- **AGENTS.md** — An open standard now governed by the Linux Foundation's Agentic AI Foundation, supported by 18+ tools

## How They Work

Both files are injected into the agent's context window at session start, acting like a persistent system prompt. Claude Code walks *up* the directory tree; AGENTS.md-aware tools walk *down* from root to leaf, with deeper files adding specificity.

## What to Include

- Exact build/test commands (e.g., `bun test -- <filename>`)
- Directories never to modify (`vendor/`, `dist/`, `src/generated/`)
- Architecture decisions not obvious from code
- Key file locations and tech-stack specifics

## What to Omit

- Generic advice ("write clean code")
- Rules already enforced by linters
- Full API docs — link instead
- Task-specific instructions (put those in the prompt)

Target under 200 lines — long files bury critical rules and increase token cost across every session turn.

## Cross-Tool Strategy

Commit one **AGENTS.md** at the repo root for broad coverage. Add **CLAUDE.md** for Claude Code-specific layering. Bridge them via symlink or Claude Code's `@AGENTS.md` import syntax.

GitHub Copilot reads instructions from *both* AGENTS.md and `.github/copilot-instructions.md` when both exist.

## Key Pitfalls

| Problem | Fix |
|---|---|
| Stale commands | Update context file in the same PR as the change |
| Vague rules | Be specific; vague instructions are ignored |
| Secrets in the file | Use env var names only, never actual values |
| One giant file | Use subdirectory layering for scoped rules |

## Advanced Notes

Claude Code's auto-memory records project discoveries in `~/.claude/projects/<project>/memory/`. You can instruct the agent to update CLAUDE.md itself when it learns something worth preserving — a lightweight form of agent-maintained documentation.

The AGENTS.md specification remains intentionally minimal (plain Markdown, no required schema) to maximize adoption, with structured/machine-readable sections under ongoing discussion.

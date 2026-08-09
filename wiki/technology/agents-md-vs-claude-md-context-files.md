---
type: literature-note
source_url: https://ai-tldr.dev/learn/ai-coding-tools/coding-agents-assistants/agents-md-claude-md/
author: Unknown
tags: [agents-md, claude-md, coding-agents, context-files]
date_consumed: 2026-08-09
---

## Summary

AGENTS.md and CLAUDE.md are Markdown files placed in a repository that coding agents read before taking any action, functioning as a persistent onboarding document injected into the agent's context window at session start. AGENTS.md is an open standard governed by the Linux Foundation's Agentic AI Foundation and supported by 18+ tools, while CLAUDE.md is Anthropic's native format with hierarchical layering for [[Claude Code]]. The recommended cross-tool strategy is to commit one AGENTS.md at the repo root for broad coverage and layer CLAUDE.md on top for Claude-specific rules.

## Core Concepts

- **[[AGENTS.md]]**: An open standard context file for coding agents, now governed by the Linux Foundation's Agentic AI Foundation; supported by 18+ tools including [[Claude Code]], [[Codex]], [[Cursor]], and [[Devin]].
- **[[CLAUDE.md]]**: Anthropic's native context file format, loaded automatically by [[Claude Code]] with hierarchical layering (global → project → local); supports `@AGENTS.md` import syntax.
- **Context Injection**: Both files are injected into the agent's context window at session start, acting like a persistent system prompt — Claude Code walks *up* the directory tree; AGENTS.md-aware tools walk *down* from root to leaf.
- **Subdirectory Layering**: Deeper AGENTS.md files add specificity scoped to their directory, enabling modular rules per domain or module.
- **Agent Auto-Memory**: Claude Code records project discoveries in `~/.claude/projects/<project>/memory/` and can be instructed to update CLAUDE.md itself — a lightweight form of agent-maintained documentation.

## Key Takeaways

- **Include**: Exact build/test commands, directories never to modify, architecture decisions, key file locations.
- **Omit**: Generic advice, rules already enforced by linters, full API docs, task-specific instructions.
- **Size limit**: Target under 200 lines — longer files bury critical rules and raise token cost per session.
- **Cross-tool strategy**: Commit AGENTS.md at root for broad coverage; add CLAUDE.md for Claude-specific layering; bridge via symlink or `@AGENTS.md` import.
- **GitHub Copilot**: Reads both AGENTS.md and `.github/copilot-instructions.md` when both exist.
- **Stale commands**: Update the context file in the same PR as the change it describes.
- **Avoid secrets**: Use env var names only — never actual credentials — in context files.

## 🧠 First Principles & Mental Models

- **[[Convention Over Configuration]]**: Encoding project conventions into AGENTS.md/CLAUDE.md eliminates repetitive re-explanation across every agent session — the same principle that makes opinionated frameworks productive out of the box.
- **[[Separation of Concerns]]**: Subdirectory layering separates general repo conventions (root AGENTS.md) from domain-specific rules (nested files), keeping each layer focused and independently maintainable.

## 🃏 Review Questions

**Q1**: What is the fundamental purpose of AGENTS.md and CLAUDE.md files?
**A**: They are Markdown files placed in a repository that coding agents read before acting, injected into the agent's context window at session start to function as a persistent onboarding document.

**Q2**: How do AGENTS.md-aware tools and Claude Code differ in how they traverse the directory tree?
**A**: Claude Code walks *up* the directory tree from the current directory, while AGENTS.md-aware tools walk *down* from the root to the leaf, with deeper files adding specificity.

**Q3**: What is the recommended cross-tool strategy for using both AGENTS.md and CLAUDE.md together?
**A**: Commit one AGENTS.md at the repo root for broad coverage across 18+ tools, then add CLAUDE.md for Claude Code-specific layering, bridged via symlink or Claude Code's `@AGENTS.md` import syntax.

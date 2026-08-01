---
type: literature-note
source_url: https://www.youtube.com/watch?v=ElYxdpYi4U0
author: Zen van Riel
tags: [agentic-engineering, claude-code, git-worktrees, context-window, parallel-agents, code-quality]
date_consumed: 2026-08-02
---

## Summary

Zen van Riel, an engineer with enterprise and startup AI coding experience, presents a practical agentic engineering workflow built around four parallel [[Claude Code]] windows, deliberate effort-level routing, [[Git Worktrees]] for conflict-free parallel work streams, and engineering-book-grounded code quality commands. The core argument is that sustainable productivity gains (30–60%, not 5x) come from treating AI coding as real engineering — with code review, architectural thinking, and team accountability — rather than from chasing hype-driven frameworks.

## Core Concepts

- **[[Parallel Claude Code Windows]]** — four simultaneous terminals tuned to different effort levels (2× high, 1× medium, 1× low) to route batch creative work separately from quick queries
- **[[Effort-Level Routing]]** — matching task complexity to Claude effort tier: long exploratory planning on high effort, quick codebase queries on low effort
- **[[Context Window Management]]** — monitoring the live context percentage and using `/compact` or `/clear` before drift sets in; timing is project-dependent, not formulaic
- **[[Git Worktrees]]** — isolated copies of the repo that let multiple Claude sessions work the same files without branch conflicts; must reinstall dependencies per worktree in some stacks
- **[[Smell Command]]** — a custom Claude command referencing [[Clean Code]] and architectural design patterns to push AI output toward established engineering principles
- **[[MCP vs Bash]]** — decision heuristic: use CLI/Bash for common platforms (GitHub, Jira), reserve [[MCP Servers]] for internal or unknown services; prefer Bash for single commands, MCP when specialized context retrieval matters (e.g., Context7 for docs, Serena for language server integration)

## Key Takeaways

- **Four windows, not fifty**: mental capacity caps parallel work at roughly four streams; the value is task routing, not raw volume
- **Effort tiers matter**: high-effort windows are still running when low-effort ones have already answered quick questions
- **Context drift is gradual**: there is no magic threshold — engineering intuition develops with practice
- **Git worktrees enable true parallelism**: shared branch state causes conflicts; worktrees give each session an independent workspace; delete them after use
- **Code quality requires intentional framing**: without explicit reference to engineering principles (Clean Code, design patterns), AI defaults to functional but architecturally shallow output
- **Enterprise reality check**: 10,000 lines per day cannot pass code review; team reviewers will push back; PR size discipline is non-negotiable
- **Realistic productivity gains**: 30–60% on production work, not 5×; coding is now a smaller fraction of total engineering time, not eliminated
- **AI native vs vibe coder**: the durable choice is to understand AI output, review it critically, and maintain ownership of architectural decisions

## Engineering Context

- [[Clean Code]] book patterns are already in LLM weights; a custom command surfaces them explicitly rather than relying on implicit knowledge
- AI code review pipelines (GitHub integrations, headless Codex loops) augment but do not replace human PR review
- GitHub CLI integration is seamless when host machine is pre-authenticated — no credential handling inside Claude
- Context7 MCP provides framework-specific documentation retrieval more precisely than generic web search

## Linked Notes

- [[agentic-engineering-subagents]] — parallel subagent patterns and context preservation
- [[agentic-design-patterns-planning]] — planning patterns for agentic loops
- [[12-claude-code-features-every-engineer-should-know]] — broader Claude Code feature catalog
- [[ai-agents-claude-skills-methodology]] — skills and methodology for Claude agents
- [[a-practical-guide-to-becoming-an-ai-native-engineer]] — mindset framing for AI-native work

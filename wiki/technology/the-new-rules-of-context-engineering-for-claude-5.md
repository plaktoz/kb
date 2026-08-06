---
type: literature-note
source_url: https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models
author: Thariq Shihipar
tags: [context-engineering, llm, claude, prompt-design]
date_consumed: 2026-07-26
---

## Summary

Anthropic eliminated over 80% of Claude Code's system prompt for Claude 5-generation models without measurable performance loss, demonstrating that newer models require guidance over rules. The core shift is from rigid directives to judgment-oriented instructions that trust the model to read context. Practical recommendations center on lightweight CLAUDE.md files, progressive disclosure via Skills, and auto-memory replacing manual triggers.

## Core Concepts

- [[Context Engineering]] — structuring model inputs for reliability at inference time
- [[Progressive Disclosure]] — loading tool definitions and context only when needed, not upfront
- [[CLAUDE.md]] — lightweight codebase-specific instruction file; should focus on gotchas, not rules
- [[Claude 5]] / [[Opus 5]] / [[Fable 5]] — generation of models with significantly improved judgment
- [[ToolSearch]] — deferred tool discovery pattern to avoid bloating the context window
- [[Auto-Memory]] — Claude saves memories automatically, removing the need for manual `/remember` triggers
- [[Skills]] — project-local instruction modules for progressive disclosure of specialized knowledge

## Key Takeaways

- **80% prompt reduction**: Removing most of the system prompt didn't hurt performance — models judge better now.
- **Rules → Judgment**: Replace directives ("never do X") with context-aware guidance ("match the surrounding code").
- **Examples constrain**: Adding examples narrows exploration; better tool design achieves the same without cost.
- **Front-loading is waste**: Load context progressively — only when the task demands it.
- **Rich references win**: Test suites and HTML artifacts outperform plain markdown for complex specs.
- **Run `/doctor`**: Claude Code can automatically rightsize your context files.

## Practical Applications (via RoboNuggets / Jay E)

*From a video commentary on the Thariq article: https://www.youtube.com/watch?v=gQeRjkb_Hlc*

- **ARMS framework** — a mental model for context engineering: **A**pplications (MCPs, APIs, CLIs), **R**outines (crons, scheduled tasks), **M**emory (artifacts, reports, documents), **S**kills (SOPs invoked via slash commands)
- **CLAUDE.md as a router** — instead of a monolithic rules file, CLAUDE.md points to department sub-routers (e.g. `content.md`, `community.md`) that hold domain-specific context; reduces token overhead at session start
- **Sub-routers per domain** — each department has its own index file that helps Claude navigate domain-specific skills, memory files, and references without loading everything upfront
- **HTML artifacts as design interface systems** — brand books in HTML (color palettes, fonts, visual style rules) give Claude richer references than markdown; visible to both the agent and the human
- **`/calibrate` skill** — run at end of each session to capture learnings and automatically update skills, CLAUDE.md rules, memory files, and workflows; prevents knowledge loss between sessions
- **`/doctor` and `/doctor-plus`** — Claude Code ships a `/doctor` command that checks for broken installs, dead-weight skills/MCP servers, and slow hooks; a community-built `/doctor-plus` also audits against the 6 new context engineering rules

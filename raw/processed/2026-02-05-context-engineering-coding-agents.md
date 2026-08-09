---
source_url: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
author: Birgitta Böckeler
date: 2026-02-05
---

# Context Engineering for Coding Agents

Context engineering for coding agents is defined simply as "curating what the model sees so that you get a better result." This article covers key categories, configuration approaches, and a detailed breakdown of Claude Code's features.

## Types of Reusable Prompts

- **Instructions** — tell the agent to do something specific
- **Guidance** — general conventions the agent should follow

## Context Interfaces

Ways the LLM can access additional context:

- **Tools** — built-in capabilities (bash, file search, etc.)
- **MCP Servers** — custom programs exposing data sources/actions
- **Skills** — on-demand resources the LLM loads when relevant

## Who Loads Context?

| Actor | Example | Trade-off |
|---|---|---|
| LLM | Skills | Non-deterministic |
| Human | Slash commands | Less automation |
| Agent software | Hooks | Deterministic |

## Claude Code Features (as of Jan 2026)

| Feature | Purpose | Loaded By |
|---|---|---|
| CLAUDE.md | Always-on project guidance | Claude Code (always) |
| Rules | Scoped/modular guidance | Claude Code (path-based) |
| Slash commands | Human-triggered instructions | Human (deprecated) |
| Skills | Lazy-loaded resources/instructions | LLM or Human |
| Subagents | Isolated context tasks, parallelizable | LLM or Human |
| MCP Servers | External API/tool access | LLM |
| Hooks | Deterministic lifecycle scripts | Agent lifecycle events |
| Plugins | Distribute configs across teams | — |

## Important Caveats

The author warns against overconfidence: context engineering improves *probability* of good results but cannot guarantee behavior. Phrases like "ensure it does X" or "prevent hallucinations" are misleading — "we still need to think in probabilities" when LLMs are involved.

On sharing configurations, the author cautions that copying setups from strangers can introduce contradictory instructions and a false sense of understanding one's own context.

---
type: literature-note
source_url: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
author: Birgitta Böckeler
tags: [context-engineering, coding-agents, claude-code, llm]
date_consumed: 2026-08-09
---

## Summary

Context engineering for coding agents is defined as curating what the model sees to get better results. Birgitta Böckeler catalogues the key categories of context — reusable prompts, context interfaces, and context loaders — and maps each onto a detailed feature breakdown of [[Claude Code]] as of January 2026. The article closes with a caution that context engineering improves the probability of good outputs but cannot guarantee behavior, so practitioners must continue to think in terms of probabilities.

## Core Concepts

- **[[Context Engineering]]**: Curating what the LLM sees — prompt instructions, guidance, tools, and data sources — to maximise the probability of a useful result.
- **[[Claude Code]]**: The coding agent whose feature set is used as the primary case study; features include CLAUDE.md, Skills, Hooks, Subagents, and MCP Servers.
- **[[CLAUDE.md]]**: Always-on project guidance file automatically loaded by Claude Code at every session start.
- **[[Skills]]**: Lazy-loaded resources or instructions that can be triggered by the LLM or by a human on demand.
- **[[Hooks]]**: Deterministic lifecycle scripts injected by the agent software at fixed points in the agent execution cycle.
- **[[MCP Servers]]** ([[Model Context Protocol]]): Custom programs exposing external data sources or actions to the LLM.
- **[[Subagents]]**: Isolated context tasks that can be parallelised, launched by the LLM or a human.
- **Context Loaders**: The actor that decides when to load context — the LLM (non-deterministic), the human (less automated), or the agent software via hooks (deterministic).

## Key Takeaways

- **Context types**: Two reusable prompt types — *instructions* (do X) and *guidance* (follow convention Y).
- **Context interfaces**: Tools (built-in capabilities), MCP Servers (custom data/actions), and Skills (on-demand resources).
- **Loader trade-off**: LLM-loaded context is flexible but non-deterministic; hook-loaded context is deterministic but requires pre-programming.
- **Claude Code feature map**: CLAUDE.md (always-on), Rules (path-scoped guidance), Slash commands (human-triggered), Skills (lazy-loaded), Subagents (parallel isolation), MCP Servers (external APIs), Hooks (lifecycle scripts), Plugins (team config distribution).
- **Probability, not certainty**: Context engineering shifts odds — "ensure" and "prevent hallucinations" are misleading framings.
- **Config copying risk**: Borrowing someone else's setup can introduce contradictory instructions and a false sense of understanding your own context.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Treating context engineering as a deterministic solution turns it into a target that can be gamed — the article explicitly warns that "ensure it does X" framing mistakes probability for guarantee, the same trap Goodhart describes when a measure becomes a goal.
- **[[Signal-to-Noise Ratio]]**: The entire discipline is about maximising relevant signal in the context window while excluding noise — each feature (Skills, Hooks, scoped Rules) is a mechanism for selective, timely loading rather than dumping everything at once.

## 🃏 Review Questions

**Q1**: What is the core definition of context engineering for coding agents according to this article?
**A**: Context engineering is "curating what the model sees so that you get a better result" — selecting and structuring the inputs the LLM receives to maximise the probability of useful output.

**Q2**: What are the three types of context interfaces available to a coding agent, and how do MCP Servers fit in?
**A**: The three interfaces are Tools (built-in capabilities like bash), MCP Servers (custom programs exposing external data or actions), and Skills (on-demand resources loaded when relevant). MCP Servers allow teams to extend the agent's reach to arbitrary external systems beyond built-in tools.

**Q3**: Why does the author warn against using the phrase "ensure it does X" in context engineering?
**A**: Because LLMs are inherently probabilistic, so context engineering can only shift the likelihood of a good outcome, not guarantee it. Framing instructions as guarantees leads to false confidence and poor evaluation practices.

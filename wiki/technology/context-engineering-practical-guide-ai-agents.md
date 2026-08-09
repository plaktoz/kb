---
type: literature-note
source_url: https://sourcegraph.com/blog/context-engineering
author: Matt Tanner
tags: [context-engineering, ai-agents, rag, coding-agents]
date_consumed: 2026-08-09
---

## Summary

[[Context Engineering]] is the discipline of deliberately designing everything an LLM sees on each inference call — system prompts, user input, retrieved documents, conversation history, tool definitions, and memory — while managing a finite token budget. Unlike chatbots, agents run in loops and accumulate state, making context curation the primary failure point rather than prompt wording. A practical pipeline built around retrieval, re-ranking, and token eviction strategies consistently outperforms naive context stuffing.

## Core Concepts

- **[[Context Engineering]]**: Anthropic defines it as "the set of strategies for curating and maintaining the optimal set of tokens" across an entire agent pipeline — distinct from prompt engineering, which focuses on a single instruction string.
- **[[Prompt Engineering]] vs. Context Engineering**: Prompt engineering is stateless and single-turn; context engineering is stateful, multi-turn, and owned by the platform team building the pipeline. The clearest signal you've crossed into context engineering: improvements come from **rewiring** (what is retrieved, in what order, what is evicted) rather than **rewording**.
- **Four Pillars of Context Engineering**:
  1. *Instructions / System Prompt* — behavioral framing before any user message; over-specific instructions cause brittleness
  2. *[[Retrieval-Augmented Generation|Retrieval]]* — RAG over vector databases, SQL queries, file reads, just-in-time lookups; poor retrieval is a leading cause of hallucinations
  3. *[[Memory]]* — short-term (conversation history + tool calls) and long-term (persistent preferences, past summaries, model-written scratchpads)
  4. *Tools* — each tool definition and result consumes tokens; ambiguous overlapping tools cause wasted turns on tool selection
- **Context Assembly Pipeline**: user input triggers parallel retrieval → memory layer contributes → system instructions + tool definitions added → re-ranker keeps top-k → full context sent to model
- **[[Context Rot]]**: model recall degrades as token count grows; quadratic attention cost makes this expensive and lossy simultaneously
- **[[Lost in the Middle]]** (Liu et al., 2023): performance is highest when key information appears at the start or end of context; it degrades significantly when relevant content is buried mid-window
- **[[Sourcegraph]] MCP + [[SCIP]]**: open Protobuf-based code intelligence protocol providing compiler-accurate cross-repo navigation; 13 MCP tools covering keyword/semantic search, symbol resolution, dependency tracing, and commit history
- **[[Model Context Protocol]]** (JSON-RPC 2.0): standardized tool-wiring layer for connecting agents to external data sources

## Key Takeaways

- Agent failures trace to missing/wrong/excess context, not model reasoning limits.
- Rewiring retrieval beats rewording prompts once agents are in production.
- Instructions that contradict model defaults cause confused behavior on every turn.
- Anthropic describes agents writing their own scratchpads outside the context window as persistent memory.
- Bloated tool sets with ambiguous overlap are the most common tool-layer failure.
- Re-ranking 50 candidates to top-5 outperforms dumping all 50 into the prompt.
- **CodeScaleBench (March 2026, 370 enterprise tasks)** — Sourcegraph MCP vs. local grep:
  - File recall: 0.127 → 0.277
  - Precision@5: 0.140 → 0.478
  - F1@5: 0.099 → 0.262
- A Kubernetes monorepo task: 2-hour timeout on baseline → 89 seconds with MCP, scoring 0.90/1.0.
- A cross-file refactor: 96 tool calls / 84 minutes → 5 tool calls / 4.4 minutes with MCP.
- Highest-signal material belongs at the top or bottom of assembled context, never the middle.
- Stale vector indexes quietly poison context: agents confidently use deprecated APIs from old READMEs.
- 2026 tooling: [[Weaviate]], [[Pinecone]], [[Qdrant]], [[pgvector]] (vector DBs); [[LangChain]], [[LlamaIndex]], [[DSPy]] (orchestration); [[mem0]], [[Letta]] (memory)

## 🧠 First Principles & Mental Models

- **[[Signal-to-Noise Ratio]]**: Dumping a 100K-token codebase into context hurts performance relative to a 5K-token targeted retrieval — irrelevant tokens act as noise that buries the signal the model needs, and attention spreads across all tokens regardless of relevance.
- **[[Occam's Razor]]**: The most common root cause of agent failure isn't model intelligence — it's the pipeline feeding the model. The simpler diagnosis (context problem, not model problem) explains most production failures and should be checked first.

## 🃏 Review Questions

**Q1**: What is the core argument that distinguishes context engineering from prompt engineering?
**A**: Prompt engineering improves a single instruction string in a stateless turn; context engineering designs what the entire agent pipeline feeds the model across multi-turn stateful runs, where the failure mode is wrong, missing, or excess information rather than the model misunderstanding the task.

**Q2**: What do the CodeScaleBench results show about compiler-accurate retrieval versus text search for coding agents?
**A**: Using Sourcegraph MCP's SCIP-backed retrieval raised Precision@5 from 0.14 to 0.478 and F1@5 from 0.099 to 0.262 across 370 enterprise tasks; a Kubernetes task that hit a 2-hour timeout on local grep completed in 89 seconds with MCP.

**Q3**: How should the "lost in the middle" finding shape context assembly pipeline design?
**A**: Highest-signal material — the most relevant retrieved chunks, key instructions — should be placed at the top or bottom of the assembled context, never buried mid-window, where research shows model recall degrades significantly.

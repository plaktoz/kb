---
type: literature-note
source_url: https://redis.io/blog/context-engineering-best-practices-for-an-emerging-discipline/
author: Jim Allen Wallace
tags: [context-engineering, llm, rag, memory-layer]
date_consumed: 2026-08-09
---

## Summary

[[Context Engineering]] is the discipline of systematically selecting, structuring, and delivering the right context to an LLM, superseding [[Prompt Engineering]] which focuses only on phrasing. According to [[Andrej Karpathy]] and Shopify CEO [[Tobi Lutke]], context — not wording — is the real bottleneck for AI development, requiring a systemic rather than ad hoc approach. Effective context engineering demands a memory layer for persistence, and tools like [[Redis]] can provide unified short-term and long-term memory management at production scale.

## Core Concepts

- [[Context Engineering]] — systematically selecting, structuring, and delivering the right context to an LLM to improve reliability and performance
- [[Prompt Engineering]] — narrower discipline of instruction phrasing; a subset of context engineering; best for ad hoc, conversational, one-off requests
- [[Andrej Karpathy]] — describes context engineering as "the delicate art and science of filling the context window with just the right information for the next step"
- [[Tobi Lutke]] — prefers context engineering because it describes "the art of providing all the context for the task to be plausibly solvable by the LLM"
- [[Context Poisoning]] — when a hallucination makes it into the context and propagates errors
- [[Context Distraction]] — when excess context overwhelms the model's trained behavior
- [[Context Confusion]] — when superfluous context influences the response inappropriately
- [[Context Clash]] — when parts of the context contradict each other
- [[Retrieval-Augmented Generation]] (RAG) — grounds AI queries in approved data sources; essential for injecting high-quality private context at runtime
- [[Memory Layer]] — persistence infrastructure enabling both short-term (session) and long-term (cross-session) memory for agents
- [[LangGraph]] — agent orchestration framework; integrates with Redis for thread-level and cross-session memory persistence
- [[Redis]] — in-memory database offering unified vector search, structured state, and memory management for production context engineering
- [[Philipp Schmid]] — Google DeepMind engineer; argues "most agent failures are not model failures anymore, they are context failures"

## Key Takeaways

- Context engineering is systemic; prompt engineering is ad hoc — one is a subset of the other.
- Overloading context causes four failure modes: poisoning, distraction, confusion, clash.
- Use the pyramid approach: start with general background, then narrow to specifics.
- RAG should dynamically inject only the most relevant context at runtime.
- Prune context aggressively — include only essential, summarized information.
- Isolate contexts per agent; not every agent needs every piece of context.
- Give agents only the tools relevant to their task to prevent irrelevant context pull.
- 70% of executives (2025 IBM research) believe agentic AI is important to their org's future.
- A memory layer distinguishes true context engineering from glorified prompt engineering.
- **Short-term memory**: session-scoped, low TTL; preserves task states across multi-step processes.
- **Long-term memory**: cross-session, persists preferences and history for agent continuity.
- Good context engineering caches well; bad context engineering is both slow and expensive.
- Vector databases alone lack conversation history, agentic state, and session management.

## 🧠 First Principles & Mental Models

- **[[Signal-to-Noise Ratio]]**: Context confusion and distraction are noise problems — irrelevant tokens dilute the signal the model needs, and careless stuffing actively degrades performance even as window size grows.
- **[[Separation of Concerns]]**: Isolating context per agent — giving each agent only its relevant slice — mirrors the software engineering principle that components should have narrow, focused responsibilities, preventing cross-contamination between tasks.

## 🃏 Review Questions

**Q1**: What distinguishes context engineering from prompt engineering?
**A**: Prompt engineering is ad hoc and focuses on phrasing; context engineering is systemic and treats context — including instructions, tool calls, memory, and retrieved knowledge — as infrastructure.

**Q2**: What are the four context failure modes identified by Drew Breunig when context is overloaded?
**A**: Context poisoning (hallucination enters context), context distraction (context overwhelms training), context confusion (superfluous context influences response), and context clash (contradictory context elements).

**Q3**: Why does a production context engineering system need a dedicated memory layer?
**A**: Without persistent memory, agents cannot maintain state across sessions, forcing repeated context injection that increases token costs; a memory layer enables short-term session state and long-term cross-session continuity at lower cost.

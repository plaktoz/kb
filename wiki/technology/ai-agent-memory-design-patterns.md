---
type: literature-note
source_url: https://machinelearningmastery.com/ai-agent-memory-design-what-works-and-what-doesnt/
author: Bala Priya C
tags: [ai-agents, memory-architecture, multi-agent-systems, llm-engineering]
date_consumed: 2026-09-10
---

## Summary

Reliable AI agent memory requires distinguishing four memory types (episodic, semantic, procedural, working) and applying deliberate design patterns rather than naive storage strategies. The article contrasts functional patterns — importance scoring, role-scoped namespaces, per-step write-back, per-decision retrieval, and provenance tracking — against six architectural anti-patterns that cause noisy retrieval, hallucination propagation, and memory poisoning. Explicit write policies and multi-layer architectures are the foundation of maintainable agent memory.

## Core Concepts

- **[[AI Agent Memory]]** — information written to external storage at runtime and retrieved across sessions; distinct from system prompts, conversation history, or static knowledge bases
- **Four memory types**:
  - **Episodic** — past interactions/decisions stored in vector/doc DB, retrieved via semantic search
  - **Semantic** — facts and preferences in vector + key-value store, retrieved by semantic or key lookup
  - **Procedural** — action patterns and workflows in structured store, retrieved by pattern match
  - **Working** — active task state/scratchpad in-memory or key-value, retrieved by direct key access
- **[[Importance Scoring]]** — each memory entry receives importance and confidence scores; only entries meeting minimum thresholds are written to long-term storage
- **Memory Scoping** — in [[Multi-Agent Systems]], each agent role gets its own write namespace; an orchestrator maintains a shared facts layer readable by all agents
- **Step-by-Step Write-Back** — intermediate results written to working memory with a TTL after each step; successful steps promoted to episodic memory
- **[[Provenance Tracking]]** — every memory entry carries metadata: writing agent, source tool call, input, and trust level; enables tracing misbehavior to a specific write
- **MemoryGraft Attack** — adversarial memory poisoning where external content with hidden instructions is stored and later retrieved as trusted context; "a small number of poisoned memory entries can account for a large share of retrieved results" due to embedding similarity retrieval

## Key Takeaways

- **Multi-layer architecture**: Separate namespaces for conversation history, task state, preferences, and domain knowledge.
- **Retrieval timing**: Retrieve at each decision point, not once at task start; check working memory first.
- **Write policy**: Explicitly specify triggers, TTLs, confidence thresholds, conflict resolution, and rollback behavior.
- **Avoid free-form summarization**: Use structured fact extraction with a typed schema to prevent hallucination persistence.
- **Unbounded memory fails**: Confidence decay, deduplication, episodic compression, and TTL expiration are mandatory.
- **Trust-level filtering**: High-trust sources pass through; lower-trust content is sanitized for embedded instructions before writing.
- **Single vector store is insufficient**: Vector similarity does not equal decision relevance; structure and relationships are needed alongside similarity search.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Mixing episodic, semantic, procedural, and working memory in a single layer collapses distinct retrieval strategies into one, causing noise — the same principle that drives layer separation in software architecture applies directly to memory system design.
- **[[Trust but Verify]]**: Treating all memory entries with uniform trust ignores their provenance; the MemoryGraft attack is only possible when retrieval bypasses trust-level filtering, making provenance metadata the enforcement point for the "verify" half of this principle.

## 🃏 Review Questions

**Q1**: What is the central design argument of the article?
**A**: Reliable agent memory requires multi-layer architectures with explicit write policies, not naive single-store approaches; the distinction between what works and what fails comes down to scoping, provenance, and structured compression.

**Q2**: How does the step-by-step write-back pattern prevent data loss on task failure?
**A**: Results are written to working memory with a TTL after every step so intermediate learning is preserved; only successful steps are then promoted to episodic memory, avoiding the loss of progress when a long task fails mid-run.

**Q3**: How should teams defend against memory poisoning attacks like MemoryGraft?
**A**: Apply trust-level filtering: high-trust sources pass through directly, while lower-trust external content is checked for embedded instructions before any write to long-term memory, preventing poisoned entries from accumulating disproportionate retrieval weight.

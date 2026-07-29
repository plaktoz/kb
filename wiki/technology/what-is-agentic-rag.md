---
type: literature-note
source_url: https://www.youtube.com/watch?v=0z9_MhcYvcY
author: IBM Technology (David Levy)
tags: [agentic-rag, llm, vector-database, ai-agents]
date_consumed: 2026-07-29
---

## Summary

Traditional [[RAG]] pipelines call the LLM once solely for response generation, but [[Agentic RAG]] promotes the LLM to an active agent that intelligently routes queries to the most relevant data source, handles out-of-scope requests gracefully, and can determine the appropriate output format. This shift from a passive generator to a decision-making orchestrator enables more accurate, context-aware, and adaptable AI systems across domains like customer support and legal tech.

## Core Concepts

- **[[RAG]] (Retrieval Augmented Generation)**: The baseline pipeline — a query hits a [[Vector Database]], the retrieved context is injected into a prompt, and the [[LLM]] generates a response; the LLM is called once for generation only.
- **[[Agentic RAG]]**: The LLM acts as an agent with decision-making authority — it chooses which database to query, determines output format (text, chart, code), and routes out-of-scope queries to a failsafe.
- **[[Intelligent Agent Routing]]**: The agent interprets the semantic context of a query to select among multiple knowledge sources (e.g., internal documentation vs. general industry knowledge), reducing irrelevant retrieval.
- **[[Failsafe Routing]]**: When a query falls outside all available knowledge bases, the agent detects the mismatch and returns a graceful "I don't have that information" response rather than hallucinating.
- **[[Multiple Data Sources]]**: Agentic RAG can simultaneously maintain access to heterogeneous knowledge bases (internal policies, public standards, real-time data, third-party services) and select dynamically.
- **[[Output Format Selection]]**: The agent decides not just what to say but how to say it — whether to return plain text, generate a chart, or provide a code snippet based on query context.

## Key Takeaways

- **Traditional RAG Limitation**: Single data source, single LLM call, no routing intelligence.
- **Agent as Orchestrator**: LLM shifts from passive responder to active decision-maker in the pipeline.
- **Multi-Source Routing**: Agent selects the right knowledge base per query using language understanding.
- **Failsafe Mechanism**: Out-of-scope queries are caught and returned gracefully, avoiding hallucination.
- **Adaptive Output**: Agent can determine the best response format — text, chart, or code.
- **Domain Applicability**: Customer support, legal tech, healthcare all benefit from intelligent context routing.
- **Evolution Frame**: Agentic RAG is an evolution of RAG, not a replacement — it augments the pipeline with intelligence.

## 🧠 First Principles & Mental Models

- **[[Delegation Principle]]**: Moving routing decisions from hard-coded pipeline logic to the LLM itself mirrors the management principle of delegating context-dependent decisions to the actor with the most situational awareness — the agent closest to the query context.

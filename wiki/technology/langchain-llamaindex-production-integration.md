---
type: literature-note
source_url: https://markaicode.com/integrate/langchain-with-llamaindex/
author: Mark
tags: [langchain, llamaindex, rag, ai-agents]
date_consumed: 2026-08-09
---

## Summary

This guide details how to connect [[LlamaIndex]]'s retrieval pipelines to [[LangChain]] agents to build production-grade [[RAG]] systems. LlamaIndex handles document indexing and chunking while LangChain manages multi-step reasoning and tool orchestration. The combined stack adds ~250ms agent overhead over a direct LlamaIndex query but unlocks complex multi-tool reasoning not possible with either framework alone.

## Core Concepts

- **[[LangChain]]**: Framework for building LLM-powered applications with tool orchestration, memory, and agent loops; uses [[ReAct]] pattern for reasoning.
- **[[LlamaIndex]]**: Document indexing and retrieval framework specializing in vector search and hybrid retrieval pipelines.
- **[[RAG]] (Retrieval-Augmented Generation)**: Architecture where the LLM queries external documents before generating a response.
- **[[ChromaDB]]**: Vector store used to persist embeddings; integrated via LlamaIndex's `VectorStoreIndex`.
- **[[Ollama]]**: Local LLM inference server used for both embeddings (`OllamaEmbedding`) and generation.
- **[[ConversationBufferMemory]]**: LangChain memory class that stores per-session conversation history to maintain context across turns.
- **[[ReAct Agent]]**: LangChain agent type (`CONVERSATIONAL_REACT_DESCRIPTION`) that reasons over tool descriptions to decide when to invoke retrieval.

## Key Takeaways

- **Latency tradeoff**: Direct LlamaIndex query ~150ms; via LangChain agent ~400ms total.
- **Index caching**: Cache index and query engine outside the agent loop — never rebuild per request.
- **Tool descriptions**: Write narrow, specific descriptions; vague descriptions cause infinite agent loops.
- **Streaming**: Use `streaming=True` in both frameworks to reduce perceived latency.
- **Memory isolation**: Isolate `ConversationBufferMemory` per user session, not globally.
- **GPU safety**: Set `OLLAMA_NUM_PARALLEL=1` to prevent GPU memory thrashing.
- **Timeout fallback**: Add fallback response when `max_execution_time` is reached.
- **Load testing**: Test with at least 50 concurrent requests (e.g. Locust, starting at 10 rps).
- **When not to use**: Standalone LlamaIndex is faster for simple FAQ bots or single-document QA.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: LlamaIndex owns retrieval; LangChain owns reasoning — composing specialized tools beats building one monolithic system, and the integration boundary makes each layer independently replaceable.
- **[[Premature Optimization]]**: The guide explicitly calls the combined stack "overkill" for low-latency use cases — choose the architecture that matches actual requirements, not the most powerful one available.

## 🃏 Review Questions

**Q1**: What is the core architectural role split between LangChain and LlamaIndex in this integration?
**A**: LlamaIndex handles document indexing and vector retrieval; LangChain handles multi-step reasoning, tool orchestration, and conversation memory.

**Q2**: What latency overhead does routing a query through a LangChain agent add over a direct LlamaIndex query, and why?
**A**: It adds ~250ms, bringing total latency to ~400ms per turn, due to the agent's own LLM reasoning calls on top of LlamaIndex's ~150ms retrieval.

**Q3**: When should you avoid this combined stack, and what should you use instead?
**A**: Avoid it for simple FAQ bots, single-document QA, or any use case requiring sub-100ms latency — standalone LlamaIndex is faster and simpler for those scenarios.

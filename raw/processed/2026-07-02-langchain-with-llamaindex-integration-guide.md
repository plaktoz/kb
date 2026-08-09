---
source_url: https://markaicode.com/integrate/langchain-with-llamaindex/
author: Mark
date: 2026-07-02
---

# LangChain with LlamaIndex in Production: A Step-by-Step Integration Guide [2026]

This guide explains how to connect LlamaIndex's retrieval pipelines to LangChain agents for production RAG systems. Tested on LangChain v0.3.15, LlamaIndex v0.12.0, and Ollama 0.6.2+ on AWS EC2 (Ubuntu 24.04, Python 3.12.4).

## Core Concept

The integration exposes LlamaIndex's vector search and hybrid retrieval as a tool callable by a LangChain ReAct agent. LlamaIndex handles document indexing and chunking; LangChain handles multi-step reasoning and tool orchestration.

**Key tradeoff:** A direct LlamaIndex query runs in ~150ms; routing through a LangChain agent adds ~250ms overhead, reaching ~400ms per turn.

## Prerequisites

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| Python | 3.11 | 3.12.4 |
| LangChain | 0.3.0 | 0.3.15 |
| LlamaIndex | 0.11.0 | 0.12.0 |
| Ollama | 0.5.0 | 0.5.7 |
| ChromaDB | 0.5.3 | 0.5.5 |

## Integration Steps

### Step 1 — Build the LlamaIndex Index

Load documents into ChromaDB using LlamaIndex's `SimpleDirectoryReader` and `VectorStoreIndex`, with `OllamaEmbedding` for local embeddings. Call `as_query_engine(similarity_top_k=3)` to create a retriever.

### Step 2 — Wrap as a LangChain Tool

Create a Python function that calls `query_engine.query(input)` and wrap it in LangChain's `Tool` object, providing a specific `description` field to guide the agent on when to invoke it.

### Step 3 — Build the Agent

Instantiate an `Ollama` LLM (or `ChatOpenAI` for GPT-4o), attach `ConversationBufferMemory` per session, and pass the tool list to `initialize_agent` with `AgentType.CONVERSATIONAL_REACT_DESCRIPTION`. Set `max_iterations=4` and `max_execution_time=30`.

## Key Takeaways

- Cache the index and query engine **outside** the agent loop — never rebuild per request.
- Write narrow tool descriptions; vague descriptions cause infinite agent loops.
- Token costs accumulate from both LlamaIndex retrieval and the agent's own LLM reasoning calls.
- Use `streaming=True` in both frameworks to reduce perceived latency.

## When to Use This Stack

Best suited for **multi-step agents that need deep document retrieval** alongside API calls. For simple FAQ bots or single-document QA, standalone LlamaIndex is faster and simpler. The combined stack is described as "overkill" for low-latency (<100ms) requirements.

## Production Checklist Highlights

- Pin all package versions in `requirements.txt`
- Set `OLLAMA_NUM_PARALLEL=1` to prevent GPU memory thrashing
- Isolate `ConversationBufferMemory` per user session
- Add fallback response when `max_execution_time` is reached
- Load-test with at least 50 concurrent requests (Locust, starting at 10 rps)

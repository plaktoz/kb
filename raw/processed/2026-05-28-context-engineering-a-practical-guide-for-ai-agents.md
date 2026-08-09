---
source_url: https://sourcegraph.com/blog/context-engineering
author: Matt Tanner
date: 2026-05-28
---

# Context Engineering: A Practical Guide for AI Agents (2026)

## Summary

By mid-2025, experienced AI engineers recognized that prompt wording was no longer the primary bottleneck. The real challenge became feeding agents the right files, tool definitions, conversation history, and retrieved facts — while managing finite context windows. This discipline is now called **context engineering**.

## What Is Context Engineering?

Context engineering is the deliberate design of everything a large language model sees on each inference call — system prompts, user input, retrieved documents, conversation history, tool definitions, and long-term memory. Anthropic describes it as "the set of strategies for curating and maintaining the optimal set of tokens."

The distinction from chatbots matters: agents run in loops, accumulate state across dozens of steps, and must make decisions with a finite token budget. A coding agent typically doesn't fail because the model can't reason — it fails because irrelevant retrieval consumes the context window before the actual bug cause ever appears.

## Context Engineering vs. Prompt Engineering

These disciplines operate at different layers, not in opposition:

| Dimension | Prompt Engineering | Context Engineering |
|---|---|---|
| Scope | Single instruction string | All tokens at inference time |
| State | Stateless/single-turn | Stateful, multi-turn, long-running |
| Failure mode | Model misunderstands the task | Model has wrong/missing/excess information |
| Owner | Anyone writing prompts | Platform team building the agent pipeline |

The clearest signal you've crossed into context engineering: improvements come from **rewiring** (what data is retrieved, in what order, what gets evicted) rather than **rewording**.

## The Four Pillars

**1. Instructions / System Prompt**
The behavioral framing before any user message. The challenge is specificity without brittleness — instructions that contradict a model's default heuristics cause confused behavior on every turn.

**2. Retrieval**
How external data enters the context window — RAG over vector databases, SQL queries, file reads, and just-in-time retrieval using lightweight identifiers like file paths. Poor retrieval is a leading cause of hallucinated answers in production agents.

**3. Memory**
- *Short-term:* conversation history including tool calls and results
- *Long-term:* persistent state across sessions (preferences, project conventions, past summaries)

Anthropic describes a pattern where "the model writes its own scratchpad to a file outside the context window as persistent memory."

**4. Tools**
The executable surface area. Each tool definition costs tokens; each result costs tokens. Ambiguous overlapping tools force the model to waste turns on tool selection. The most common failure: "bloated tool sets that cover too much functionality or lead to ambiguous decision points."

## Context Assembly Pipeline

Each turn runs a pipeline:
1. User input triggers parallel retrieval (vector search, keyword search, structured lookups, code-graph queries)
2. Memory layer contributes relevant prior turns and persistent notes
3. System instructions and tool definitions are added
4. A **re-ranker** scores candidates and keeps only top-k
5. Full assembled context is passed to the model

## Token Budget Management

Dense attention scales quadratically with sequence length. Beyond cost and latency, there's "context rot" — as token count grows, the model's ability to accurately recall information degrades. Mitigation strategies include:

- Truncating tool outputs
- Compacting old conversation into running summaries
- Dropping retrieved chunks below relevance thresholds
- Capping candidates per retrieval call

A pipeline retrieving 50 candidates then re-ranking to a precise top-5 typically outperforms dumping all 50 into the prompt.

## Application to Coding Agents

Code is a particularly measurable laboratory for context engineering because the retrieval problem is well-defined and failures surface in test suites quickly.

Sourcegraph's MCP server exposes 13 tools to MCP-compatible agents, covering keyword/semantic search, symbol resolution, dependency tracing, cross-repo navigation, commit history, and file reads. It's backed by **SCIP** (an open Protobuf-based code intelligence protocol) providing compiler-accurate cross-repo navigation.

The advantage over pure text retrieval: when an agent queries for a symbol definition, it receives the actual definition plus specific call sites — rather than 50 files where the string *might* appear.

**CodeScaleBench results** (March 2026, 370 enterprise-scale tasks, local grep vs. Sourcegraph MCP):
- File recall: 0.127 → 0.277
- Precision@5: 0.140 → 0.478
- F1@5: 0.099 → 0.262

One Kubernetes monorepo task hit a two-hour timeout on baseline but completed in 89 seconds with MCP, scoring 0.90/1.0. A cross-file refactor dropped from 96 tool calls / 84 minutes to 5 tool calls / 4.4 minutes.

## Common Failure Modes

**Context Overload / Distraction / Confusion**
Dumping everything into the context window feels safe but isn't. Agents can perform worse with a 100K-token codebase summary than with a 5K-token targeted retrieval. Irrelevant material crowds out important signals; conflicting signals pull the model in different directions.

**Stale Retrieval**
Vector indexes that aren't refreshed after code changes quietly poison the context window. An agent finding a deprecated API in an old README will confidently attempt to use it.

**Lost in the Middle**
Research (Liu et al., 2023) found model performance "is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle." Highest-signal material belongs at the top or bottom of assembled context.

## Tooling Landscape (2026)

- **Vector DBs:** Weaviate, Pinecone, Qdrant, Milvus, pgvector — differentiated by hybrid search support and re-ranker integration
- **Orchestration:** LangChain (widely used), LlamaIndex (retrieval-focused), DSPy (pipeline optimization)
- **Code Intelligence:** Sourcegraph MCP + SCIP for large/multi-repo codebases; Model Context Protocol (JSON-RPC 2.0) for standardized tool wiring
- **Memory:** mem0, Letta, or custom key-value stores with summarization passes

## Core Takeaway

Prompt engineering teaches how to communicate with a single LLM call. Context engineering teaches how to build the system around it. The model is no longer the only bottleneck — the pipeline feeding it matters equally. And as long as context windows remain finite (even at 2M tokens, lost-in-the-middle and distraction patterns persist), someone must decide what enters the window on every turn.

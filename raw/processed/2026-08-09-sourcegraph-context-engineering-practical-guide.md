# Context Engineering: A Practical Guide for AI Agents (2026)

**Author:** Matt Tanner
**Date:** May 28, 2026
**Source:** https://sourcegraph.com/blog/context-engineering

---

## Summary

Context engineering is the practice of deliberately designing what an LLM sees on every inference call — system prompts, retrieved documents, conversation history, tool definitions, and memory. Anthropic describes it as strategies for "curating and maintaining the optimal set of tokens during LLM inference."

---

## Context Engineering vs. Prompt Engineering

These aren't competing disciplines — they operate at different layers:

| Dimension | Prompt Engineering | Context Engineering |
|---|---|---|
| Scope | Single instruction string | Full token set at inference |
| State | Stateless/single-turn | Stateful, multi-turn |
| Failure mode | Model misunderstands task | Model has wrong/too much info |
| Owner | Anyone writing prompts | Platform team |

The key diagnostic: if improvements come from **rewording**, that's prompt engineering. If they come from **rewiring** what data the agent retrieves and when, that's context engineering.

---

## The Four Pillars

### 1. Instructions / System Prompt
Find the balance between overly rigid rules and vague guidance. The most common failure isn't length — it's instructions that conflict with the model's default behaviors.

### 2. Retrieval
How external data enters the context window:
- Vector/semantic search (RAG)
- Structured database queries
- Filesystem reads
- Just-in-time retrieval using lightweight identifiers like file paths

Poor retrieval is one of the largest sources of hallucinated answers in production agents.

### 3. Memory
Two types:
- **Short-term:** current conversation history, tool calls/results
- **Long-term:** persists across sessions (user preferences, project conventions, summaries)

Production systems typically maintain both, with a compaction step that condenses older turns into summaries when the window fills.

### 4. Tools
The executable surface area available to the agent. Key issues:
- Each tool definition costs tokens
- Each tool result costs tokens
- Ambiguous or overlapping tools waste turns on decision-making

A core observation: if a human engineer can't immediately identify which tool to use in a given situation, an AI agent won't reliably do better either. Fewer, clearer tools almost always outperform sprawling tool sets.

---

## Context Pipeline in Practice

### Assembly
A typical pipeline:
1. Take user input
2. Run parallel retrieval (vector, keyword, structured, code-graph)
3. Merge candidates
4. Layer in memory (short-term + persistent notes)
5. Add system instructions and tool definitions
6. Pass full context to the model

### Token Budget Management
Token costs scale with sequence length, and "context rot" is real — as context windows fill, the model's recall accuracy from that context decreases.

Budget strategies include:
- Truncating tool outputs
- Compacting old turns into running summaries
- Dropping retrieved chunks below a relevance threshold
- Capping candidates per retrieval call

### Re-ranking
The merge step usually produces more candidates than the budget allows. A re-ranker (cross-encoder or smaller model) scores candidates against the query and keeps only the top-k. Retrieving 50 candidates with high recall, then re-ranking to a precise top-5, typically outperforms dumping all 50 into the prompt.

---

## Application to Coding Agents

Code is an ideal laboratory for context engineering: the retrieval problem is well-defined and failures surface quickly in test suites.

Key insight: AI agents struggle on enterprise codebases for the same reasons humans do — cross-repo dependencies, decisions buried in old commits, undocumented architectural patterns.

### Sourcegraph MCP Server (13 tools)
- Keyword and semantic search across repositories
- Symbol resolution and dependency tracing
- Cross-repository navigation
- Commit and diff history
- File reads

Backed by **SCIP** (open Protobuf-based code intelligence protocol), which enables compiler-accurate cross-repo navigation. This allows returning the *actual definition* of a symbol rather than 50 files where the string might appear.

### CodeScaleBench Results (March 2026)
Comparing local grep/file-read vs. Sourcegraph MCP across 370 enterprise-scale tasks:

| Metric | Baseline | With MCP |
|---|---|---|
| File Recall | 0.127 | 0.277 |
| Precision@5 | 0.140 | 0.478 |
| F1@5 | 0.099 | 0.262 |

Notable examples:
- Kubernetes monorepo task: 2-hour timeout (baseline) → 89 seconds (MCP), scoring 0.90/1.0
- Cross-file refactor: 96 tool calls / 84 minutes (baseline) → 5 tool calls / 4.4 minutes (MCP), at double the reward

---

## Common Failure Modes

### Context Overload, Distraction, and Confusion
Dumping everything into the context window feels safe but degrades performance. Two specific failure patterns:
- **Context distraction:** irrelevant material crowds out important content
- **Context confusion:** conflicting signals pull the model in multiple directions

Observed result: agents can perform *worse* with a 100K-token codebase summary than with a targeted 5K-token retrieval on the same task.

### Stale Retrieval
Vector indexes go stale when code changes but embeddings aren't refreshed. An agent that finds a deprecated API in an old README will confidently attempt to call it.

### Lost in the Middle
Per the 2023 Liu et al. paper, model performance is highest when relevant information appears at the **beginning or end** of the context, and degrades significantly when it's buried in the middle. Assemble context with highest-signal material at the edges.

---

## Tooling Landscape (2026)

- **Vector DBs:** Weaviate, Pinecone, Qdrant, Milvus, pgvector
- **Orchestration:** LangChain, LlamaIndex, DSPy
- **Code Intelligence:** Sourcegraph MCP (SCIP-backed), Model Context Protocol (JSON-RPC 2.0)
- **Memory:** mem0, Letta, or custom key-value + summarization layers

---

## Key Takeaways

1. Prompt engineering is one input to a larger context pipeline — not a replacement for it
2. The four pillars are: Instructions, Retrieval, Memory, Tools
3. Token budget management is active curation *before* content enters the window
4. For code, structured/deterministic retrieval outperforms pure vector search at scale
5. Larger context windows reduce pressure but don't eliminate the need for context engineering — latency, cost, and attention degradation remain

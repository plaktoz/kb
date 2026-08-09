---
type: literature-note
source_url: https://comet.com/site/blog/context-window/
author: Kelsey Kinzer
tags: [context-window, llm, ai-agents, context-engineering]
date_consumed: 2026-08-09
---

## Summary

A context window is an LLM's working memory — the total tokens it can hold and reference while generating a response — and once full, earlier information is silently dropped. For agentic workflows, context accumulates rapidly across multi-step calls, making failures invisible until production. The article argues that "context engineering" — deliberately managing what stays in memory — matters more than simply maximizing window size.

## Core Concepts

- **[[Context Window]]**: Total tokens an LLM can process in one call; components include system instructions, user input, conversation history, tool outputs, and retrieved documents.
- **[[Token]]**: Text chunks roughly equal to four characters or three-fourths of a word; a 100K-token window holds ~75,000 words (~250 pages).
- **[[AI Agents]]**: Agentic workflows accumulate context across every LLM call — a 50-step workflow at 20K tokens per call consumes 1 million tokens total.
- **[[Silent Degradation]]**: Agents continue executing with incomplete context, producing plausible but wrong results rather than erroring out explicitly.
- **[[Lost in the Middle]]**: Research-documented attention failure where LLMs perform best with information at the start or end of context; a 1M-token window does not equal 1M tokens of perfect memory.
- **[[Cascading Failures]]**: Dropped early results cause later workflow steps to branch incorrectly, compounding errors.
- **[[Context Engineering]]**: Intentional management of what enters, stays in, and leaves the context window — summarization checkpoints, compression of tool outputs, semantic caching.
- **[[Retrieval-Augmented Generation|RAG]]**: Alternative architecture using smaller context + retrieval, preferred when searching large knowledge bases or optimizing for cost.
- **[[Semantic Caching]]**: Caches repeated retrieval queries to reduce redundant token consumption.
- **[[Rolling Window]]**: Sliding context approach suited to long-running conversational agents.

## Key Takeaways

- **Working memory metaphor**: Filling the context window causes silent information loss.
- **Agents burn context fast**: Multi-step workflows compound token usage across calls.
- **Invisible failures**: Context-overflow bugs often only surface in production with real-world input lengths.
- **Lost in the middle**: More tokens past a threshold actively degrades accuracy rather than helping.
- **Design for worst-case**: Token budgets should account for system prompts (500–2,000 tokens), history, tool outputs, and retrieved docs.
- **Compress, don't just expand**: Summarize 100 DB rows to the top 5; preserve original user intent and recent tool results.
- **Architecture decision rule**: Use long context when cross-step detail and relationship tracking matter; use RAG + smaller context when searching large knowledge bases or optimizing cost.
- **Observability is required**: Track token consumption per step, proximity to limits (80%+ signals risk), and cost per workflow execution.

## 🧠 First Principles & Mental Models

- **[[Working Memory]] (cognitive science)**: The context window is structurally analogous to human working memory — limited capacity, recency bias, and degraded performance when overloaded — making familiar cognitive load strategies (chunking, offloading) directly applicable to agent design.
- **[[Goodhart's Law]]**: Maximizing context window size becomes the wrong target when developers treat "bigger window = better agent"; the actual goal is reliable task completion, which requires managing what is *in* context, not just how large the window is.

## 🃏 Review Questions

**Q1**: What is a context window and why does it matter for AI agents differently than for simple LLM apps?
**A**: A context window is an LLM's working memory — the total tokens it can hold while generating a response. For agents, context accumulates across every call in a multi-step workflow, meaning a 50-step workflow at 20K tokens per call can consume 1 million tokens, far exceeding what a single call demands.

**Q2**: What is the "lost in the middle" failure mode, and why does it undermine large context windows as a silver bullet?
**A**: LLMs attend better to information at the start or end of context; information placed mid-context suffers degraded attention. This means a 1M-token window does not provide 1M tokens of uniform, reliable memory — accuracy still degrades as context grows.

**Q3**: What is "context engineering" and how does it differ from simply using a larger context window?
**A**: Context engineering is the intentional management of what enters, stays in, and is compressed or dropped from the context window — using summarization checkpoints, output compression, and semantic caching. It treats context as a scarce resource to optimize rather than a space to fill, and outperforms the naive approach of maximizing window size.

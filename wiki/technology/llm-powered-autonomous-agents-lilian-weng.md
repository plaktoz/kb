---
type: literature-note
source_url: https://lilianweng.github.io/posts/2023-06-23-agent/
author: Lilian Weng
tags: [agentic-ai, llm-agents, memory-architecture, react-pattern]
date_consumed: 2026-07-27
---

## Summary

Lilian Weng's foundational survey defines LLM-powered autonomous agents through three components: Planning, Memory, and Tool Use. Planning includes decomposition methods like [[Chain of Thought]] and [[Tree of Thoughts]], plus self-reflection via [[ReAct]] and [[Reflexion]]. The article maps human memory types onto agent equivalents and catalogs tool-use frameworks, closing with a clear-eyed list of failure modes that still constrain production agents.

## Core Concepts

- **Three-component architecture**: [[Planning]], [[Memory]], [[Tool Use]] — every agent system maps onto these
- **Planning methods**: [[Chain of Thought (CoT)]], [[Tree of Thoughts]], [[LLM+P]] (classical planner as intermediary)
- **Reflection loops**: [[ReAct]] (Thought → Action → Observation cycle), [[Reflexion]] (dynamic memory + trajectory restart on failure detection)
- **Memory taxonomy**: sensory (embeddings) / short-term (context window) / long-term ([[Vector Store]] via MIPS/[[FAISS]])
- **Tool-use frameworks**: [[MRKL]], [[Toolformer]], [[HuggingGPT]], [[API-Bank]]
- **[[Lilian Weng]]** — OpenAI research lead; this post is one of the most-cited agent architecture surveys

## Key Takeaways

- **ReAct loop**: "Thought → Action → Observation" cycle grounds reasoning in real environment feedback
- **Reflexion restart signal**: repeated identical actions producing identical observations = detected hallucination
- **Memory hierarchy**: context window = short-term; vector store with MIPS retrieval = long-term
- **MRKL routing**: general LLM routes to specialized neural or symbolic expert modules
- **Finite context is the primary constraint**: limits historical awareness and agent communication bandwidth
- **Long-horizon replanning fails**: early errors compound; LLMs struggle to adapt mid-plan
- **Interface fragility**: formatting non-compliance requires significant output-parsing defensive code

## 🧠 First Principles & Mental Models

- **[[Second-Order Effects]]**: The finite context constraint isn't just a storage limit — it cascades into planning failures, where early errors that can't be "remembered" compound undetected into late-stage task failure.
- **[[Separation of Concerns]]**: The three-component decomposition (Planning / Memory / Tool Use) reflects a clean SoC principle — each can evolve independently, which is why the taxonomy has remained durable despite rapid architectural change.

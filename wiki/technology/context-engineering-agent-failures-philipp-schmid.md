---
type: literature-note
source_url: https://philschmid.de/context-engineering
author: Philipp Schmid
tags: [context-engineering, llm-agents, prompt-engineering, ai-systems]
date_consumed: 2026-08-09
---

## Summary

[[Context Engineering]] is the emerging discipline of designing dynamic systems that supply an LLM with the right information, tools, and format at the right moment — superseding [[Prompt Engineering]] as the core AI skill. Most AI agent failures are framed as model failures, but the author argues they are context failures: the model was never given what it needed to succeed. Building reliable agents requires engineering the full context window thoughtfully, not just writing better prompts.

## Core Concepts

- [[Context Engineering]] — designing and building dynamic systems that provide the right information and tools, in the right format, at the right time
- [[Prompt Engineering]] — narrower predecessor skill focused on static instruction phrasing; now subsumed by context engineering
- [[LLM Agents]] — AI systems that take sequences of actions; their reliability is bounded by context quality
- [[Context Window]] — everything the model sees before generating a response; composed of multiple structured inputs
- [[System Prompt]] — behavioral instructions, rules, and examples that frame the agent's behavior
- [[Short-term Memory]] — current conversation history in-context
- [[Long-term Memory]] — persistent knowledge injected across sessions
- [[Retrieval-Augmented Generation]] (RAG) — mechanism for supplying external documents, databases, or API results as context
- [[Structured Output]] — response format definitions included in the context to shape model output
- [[Philipp Schmid]] — ML engineer (Hugging Face) who authored this framing of context engineering

## Key Takeaways

- Context = system prompt + user prompt + memory + retrieved info + tools + output format
- **Most agent failures are context failures, not model failures**
- A well-contextualized agent beats a stronger model with poor context
- Context engineering is a **system**, not a static string
- Context must be **dynamic** — tailored per request, not one-size-fits-all
- Relevant information beats raw data dumps; format matters as much as content
- Building agents is a cross-functional challenge: business understanding + output definition + information structuring
- Clever code and frameworks are secondary to thoughtful context window design

## 🧠 First Principles & Mental Models

- **[[Garbage In, Garbage Out]]**: The email agent example makes this vivid — even a capable model produces robotic output when the input context is stripped of calendar data, history, and tools. Model quality is an upper bound; context quality sets the floor.
- **[[Root Cause Analysis]]**: Attributing agent failures to the model is a misdiagnosis. Schmid's framing pushes practitioners to trace failures upstream to missing or malformed context rather than defaulting to "the model isn't good enough."

## 🃏 Review Questions

**Q1**: What is the central argument of Philipp Schmid's article about context engineering?
**A**: Most AI agent failures are context failures, not model failures — building reliable agents depends on engineering the full context window with the right information, tools, and format, not on the model's raw capability alone.

**Q2**: What are the components that make up an LLM's context window according to this article?
**A**: System prompt, user prompt, short-term memory (conversation history), long-term memory (persistent knowledge), retrieved information (RAG), available tools, and structured output format definitions.

**Q3**: How does context engineering differ from prompt engineering in practice?
**A**: Prompt engineering focuses on static instruction phrasing; context engineering designs a dynamic system that assembles and tailors the full information environment per request — it is a broader cross-functional discipline, not just better wording.

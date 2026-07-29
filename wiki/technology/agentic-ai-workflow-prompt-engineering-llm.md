---
type: literature-note
source_url: https://www.youtube.com/watch?v=bwvfdFWR1RI
author: IBM Technology (Shad Griffin)
tags: [agentic-ai, prompt-engineering, llm-workflow, multi-step-reasoning]
date_consumed: 2026-07-29
---

## Summary

Shad Griffin demonstrates through a concrete grocery-order validation problem that even the largest available LLM can fail on tasks that require multiple distinct cognitive operations (extraction, classification, comparison, generation) in a single prompt. His solution is to decompose the problem into a chained [[Agentic Workflow]] where each step calls a dedicated prompt optimized for one function. The key insight is that LLM confusion at scale often signals a decomposition problem, not a model capability problem.

## Core Concepts

- **[[Agentic Workflow]]**: A pipeline of multiple LLM calls (or functions) where each step handles a single well-defined sub-task, and the output of one step feeds the next.
- **[[Prompt Decomposition]]**: Breaking a complex task into discrete prompt functions — extraction, classification, comparison, generation — to reduce cognitive load per call.
- **[[LLM Chaining]]**: Connecting the output of one prompt/model call as the input to the next, enabling multi-step reasoning that a single prompt cannot reliably accomplish.
- **[[Extraction Prompt]]**: A prompt specialized for pulling structured data out of unstructured text.
- **[[Classification Prompt]]**: A prompt that categorizes or validates a piece of information (e.g., "is this reason valid?").
- **[[Edge Case Handling]]**: Agentic workflows improve handling of ambiguous or edge-case inputs by isolating judgment to dedicated steps rather than lumping all logic together.

## Key Takeaways

- **Single-prompt failure is a decomposition signal**: if the largest LLM can't solve it, break it apart.
- **Four-step agentic workflow**: extract → classify/validate → compare → generate output.
- **Each prompt does one thing**: extraction, classification, comparison, and generation are distinct cognitive modes.
- **Model confusion arises from task overloading**: mixing too many functions in one prompt degrades reliability.
- **Agentic workflows are not just for scale**: they solve precision problems too, including edge cases.
- Steps need not always be LLM calls — some can be simple text functions or comparisons.

## 🧠 First Principles & Mental Models

- **[[Single Responsibility Principle]]**: Each prompt in an agentic workflow should do exactly one thing — the same principle that makes functions maintainable in software engineering also makes prompts more reliable.
- **[[Divide and Conquer]]**: Decomposing an intractable single-prompt problem into sequenced sub-problems is a classic algorithmic strategy; Griffin's case demonstrates it applies equally to LLM task design.

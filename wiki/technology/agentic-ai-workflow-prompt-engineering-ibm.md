---
type: literature-note
source_url: https://www.youtube.com/watch?v=bwvfdFWR1RI
author: IBM Technology
tags: [agentic-ai, llm, prompt-engineering, ai-agents]
date_consumed: 2026-08-01
---

## Summary

When a single LLM — even the largest available — cannot reliably solve a complex task, the solution is to decompose the problem into an agentic workflow of multiple smaller, focused prompts. IBM's Shad Griffin demonstrates this pattern using a grocery-order validation use case where one monolithic prompt kept failing on edge cases. Breaking the task into sequential extraction, classification, comparison, and generation steps resolved the reliability problem entirely.

## Core Concepts

- [[Agentic Workflow]] — chaining multiple [[LLM]] calls (or other functions) where each step handles a single, well-defined sub-task
- [[Prompt Engineering]] — crafting precise prompts tailored to a specific function type (extraction, classification, generation)
- [[Task Decomposition]] — splitting a complex problem into simpler, independently solvable steps
- [[IBM watsonx]] — the IBM AI platform referenced in the demonstration context
- [[Shad Griffin]] — IBM practitioner demonstrating the workflow

## Key Takeaways

- **LLM Scaling Limit**: Largest available LLM may still fail complex multi-step tasks.
- **Decompose by Function**: Separate extraction, classification, comparison, and generation into distinct prompts.
- **Extraction Step**: First prompt pulls structured data from unstructured input.
- **Classification Step**: Second prompt judges validity of extracted values (e.g., "meh" is not a valid reason).
- **Comparison Step**: Third prompt reconciles classified output against source data.
- **Generation Step**: Final prompt or function formats the result for output.
- **Agentic = Multi-call**: Any multi-prompt, multi-function pipeline qualifies as an agentic workflow.
- **Edge Cases**: Single-prompt approaches break on edge cases that agentic pipelines handle gracefully.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Each prompt handles exactly one function type — mixing extraction, classification, and generation into one prompt overloads the model the same way a monolithic function overloads a codebase.
- **[[Divide and Conquer]]**: Decomposing an intractable problem into independently solvable sub-problems is the core reason agentic workflows succeed where single prompts fail.

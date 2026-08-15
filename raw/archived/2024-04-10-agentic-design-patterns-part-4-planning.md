# Agentic Design Patterns Part 4: Planning

source_url: https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/

---

Author: Andrew Ng
Date: April 10, 2024

## Summary

Planning is an agentic AI design pattern where an LLM autonomously determines a sequence of steps to accomplish complex tasks. Rather than executing a single action, the agent dynamically decomposes objectives into subtasks.

## Key Concepts

**Multi-Step Planning**: For tasks that cannot be completed in one action, an LLM breaks work into sequential steps. A research agent example: the system may search, synthesize findings, and compile a report across separate steps.

**Dynamic Tool Selection**: In a live demo, when a web search API failed with rate-limiting, the agent unexpectedly pivoted to a Wikipedia tool it had been given, completing the task successfully. This illustrates how planning enables agents to adapt to unforeseen circumstances.

**Structured Plan Output**: Drawing from HuggingGPT, plans can be expressed as structured strings specifying tools, inputs, and outputs — software then triggers each step sequentially.

**Fixed vs. Dynamic Planning**: Some workflows use deterministic, fixed step sequences (no planning needed). Planning adds value specifically when task decomposition cannot be specified in advance.

## Tradeoffs

- Planning is powerful but produces less predictable results than Reflection or Tool Use patterns
- Considered a "less mature technology" but with rapid improvement expected

## Recommended Reading

- Wei et al. (2022) — Chain-of-Thought Prompting
- Shen et al. (2023) — HuggingGPT
- Huang et al. (2024) — Survey on LLM agent planning

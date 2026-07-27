---
type: literature-note
source_url: https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-4-planning/
author: Andrew Ng
tags: [agentic-ai, planning, multi-step-reasoning, loop-engineering]
date_consumed: 2026-07-27
---

## Summary

Planning as an agentic design pattern enables LLMs to autonomously decompose complex tasks into multi-step strategies rather than executing a single action. The key value-add over fixed workflows is dynamic tool selection — a live demo showed an agent pivoting to Wikipedia when a rate-limited search API failed, completing the task via an unexpected path. Planning produces less predictable results than Reflection or Tool Use, and is considered the least mature of the four agentic patterns.

## Core Concepts

- **[[Planning]] pattern**: LLM decomposes objective → selects tools → executes step sequence → adapts on failure
- **[[HuggingGPT]]**: plans expressed as structured strings specifying tools, inputs, and outputs; software triggers each step
- **Fixed vs dynamic planning**: deterministic workflows need no planning; planning adds value when decomposition cannot be specified in advance
- **[[Chain-of-Thought Prompting]]** (Wei et al., 2022): foundational mechanism enabling step-by-step planning
- **Dynamic tool selection**: agent adapts mid-plan when a tool fails — pivots to alternatives in its inventory
- **[[Andrew Ng]]** — this is Part 4 of his agentic design patterns series

## Key Takeaways

- **Use planning when**: task decomposition cannot be specified before seeing the input
- **Skip planning when**: steps are fully predictable — use a deterministic workflow instead
- **Dynamic tool fallback**: real capability — agent found Wikipedia when search API rate-limited
- **Structured plan output**: [[HuggingGPT]] approach expresses plans as tool-input-output strings for software execution
- **Predictability tradeoff**: planning generates less predictable outputs than reflection or tool-use patterns
- **Maturity note**: "less mature technology" — highest upside, highest variance among the four patterns
- **Key papers**: Wei et al. (2022) Chain-of-Thought; Shen et al. (2023) HuggingGPT; Huang et al. (2024) planning survey

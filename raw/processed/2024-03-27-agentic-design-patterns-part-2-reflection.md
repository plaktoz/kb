# Agentic Design Patterns Part 2: Reflection

source_url: https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/

---

Author: Andrew Ng
Date: March 27, 2024

## Core Concept: Reflection as an Agentic Loop

Rather than prompting an LLM once for a final answer, reflection involves iteratively prompting the model to critique and revise its own output. This automates the feedback loop that users already experience manually when they push a chatbot to improve a response.

## Self-Critique Cycle

The workflow follows three steps:
1. **Generate** — LLM produces initial output for task X
2. **Critique** — LLM is prompted to evaluate that output for correctness, style, and efficiency
3. **Revise** — LLM rewrites using the critique as context

This cycle can repeat multiple times, with each pass potentially yielding further improvement.

## Extending the Loop with Tools

Beyond pure self-reflection, the LLM can use external tools — such as running unit tests or web searches — to ground its self-evaluation in concrete evidence before revising.

## Multi-Agent Variant

One practical implementation uses two separate agents: one focused on generation, the other on critique. Their "discussion" drives quality improvements.

## When to Use Reflection Loops

- **Code generation** — catching bugs, style issues, inefficiencies
- **Text writing** — improving clarity and accuracy
- **Question answering** — identifying gaps or errors

It's "relatively quick to implement" yet delivers "surprising performance gains."

## Recommended Papers

- Self-Refine — Madaan et al. (2023)
- Reflexion — Shinn et al. (2023)
- CRITIC — Gou et al. (2024)

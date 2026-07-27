---
type: literature-note
source_url: https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/
author: Andrew Ng
tags: [reflection-loop, agentic-ai, self-critique, code-generation]
date_consumed: 2026-07-27
---

## Summary

Reflection as an agentic design pattern iteratively prompts an LLM to critique and revise its own output, automating the feedback loop users currently apply manually. The three-step cycle (Generate → Critique → Revise) can extend to external tools for grounded evaluation, and can be implemented with two separate agents (generator + critic) whose "discussion" drives quality. It's relatively quick to implement and delivers surprising performance gains on knowledge-intensive tasks.

## Core Concepts

- **Self-critique loop**: Generate → Critique → Revise, repeating N iterations
- **Tool-grounded reflection**: use unit tests or web searches to provide concrete evidence before revision
- **Multi-agent reflection**: separate generator and critic agents; critic plays an adversarial teacher role
- **System 1 → System 2 shift**: reflection converts reactive LLM responses toward deliberate reasoning
- **Key papers**: [[Self-Refine]] (Madaan et al., 2023), [[Reflexion]] (Shinn et al., 2023), [[CRITIC]] (Gou et al., 2024)

## Key Takeaways

- **Three-step cycle**: Generate → Critique (correctness, style, efficiency) → Revise; repeat
- **External grounding improves reflection**: running tests > pure self-evaluation for code
- **Two-agent variant**: role separation sharpens critique quality — adversarial framing forces sharper feedback
- **Best use cases**: code generation, writing, question answering — all knowledge-intensive domains
- **Quick wins**: "relatively quick to implement" with "surprising performance gains"
- **Latency tradeoff**: unsuitable when response speed is a hard constraint

## 🧠 First Principles & Mental Models

- **[[Red Team / Blue Team]]**: The two-agent reflection variant formalizes this — the generator is the blue team (builds), the critic is the red team (attacks). Quality improves because the adversarial structure forces each role to be sharper.

---
type: literature-note
source_url: https://techcrunch.com/2026/09/07/artificial-intelligence-definition-glossary-hallucinations-guide-to-common-ai-terms/
author: Natasha Lomas, Romain Dillet, Kyle Wiggers, Lucas Ropek
tags: [ai-terminology, llm, glossary, ai-safety]
date_consumed: 2026-09-09
---

## Summary

TechCrunch maintains a living glossary of AI terms to track fast-evolving vocabulary in the field, covering everything from foundational concepts like [[Hallucination]] and [[RLHF]] to emerging terminology like "opaque recurrence" and "RAMageddon." The glossary highlights how new engineering techniques — particularly [[Recurrent Depth]] in models like OpenAI's Astra — are generating new vocabulary as safety researchers grapple with reduced reasoning transparency. It serves as a practical reference for both technical practitioners and observers trying to keep pace with an accelerating field.

## Core Concepts

- **[[AGI]] (Artificial General Intelligence)**: AI outperforming humans at most tasks; definitions vary across [[OpenAI]], [[Google DeepMind]], and academic researchers — no consensus threshold exists.
- **[[AI Agent]]**: Autonomous system performing multistep tasks (booking, coding, expense filing) with minimal human input per step.
- **[[Chain-of-Thought]]**: Breaking problems into intermediate reasoning steps to improve LLM accuracy on complex tasks.
- **[[Opaque Recurrence]]** / **[[Recurrent Depth]]**: A model loops queries through internal layers repeatedly rather than reasoning in plain language, reducing legible traces and complicating safety oversight. Surged in usage after coverage of OpenAI's Astra model.
- **[[Neuralese]]**: Hypothetical scenario where a model reasons entirely in internal numeric representations, becoming a complete black box with no human-readable intermediate states.
- **[[Hallucination]]**: AI generating factually incorrect information due to training data gaps or statistical pattern-matching without truth verification.
- **[[RAMageddon]]**: Growing RAM chip shortage driven by AI infrastructure demand, raising costs across consumer electronics and enterprise computing.
- **[[MCP]] (Model Context Protocol)**: [[Anthropic]]-originated open standard connecting AI models to external tools and data — described as "a USB-C port for AI."
- **[[Mixture of Experts]] (MoE)**: Architecture activating only specialized sub-networks per task, enabling large but compute-efficient models.
- **[[RLHF]]**: Reinforcement learning from human feedback; central to fine-tuning models for safety and helpfulness.
- **[[Recursive Self-Improvement]] (RSI)**: AI improving itself without human input; framed as both a research frontier and a potential safety threshold.
- **[[Validation Loss]]**: Training metric indicating how well a model generalizes to unseen data; used to detect overfitting.
- **[[Weights]]**: Numerical parameters shaping model output by determining feature importance during training.

## Key Takeaways

- **Opaque recurrence surge**: The term entered wide use after OpenAI's Astra model raised interpretability concerns.
- **Neuralese as endgame risk**: Fully latent reasoning would eliminate human-readable CoT entirely.
- **MCP as infrastructure standard**: Anthropic's protocol positions itself as universal AI-tool connectivity layer.
- **RAMageddon is real**: AI infrastructure demand is creating hardware supply constraints felt by consumers.
- **RLHF still foundational**: Remains the dominant method for aligning model behavior with human preferences.
- **RSI threshold matters**: Whether AI can self-improve without human input is a key safety demarcation line.
- **Weights define behavior**: Understanding that model weights encode all learned behavior is key to understanding AI capability and risk.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: When safety researchers rely on CoT legibility as the primary oversight signal, labs optimizing for performance (not legibility) will inadvertently destroy it — opaque recurrence is exactly this dynamic playing out at the architectural level.
- **[[Abstraction Layers]]**: Each new term in this glossary (MCP, MoE, RLHF) represents a layer of abstraction hiding underlying complexity — mastering the vocabulary is prerequisite to reasoning about the systems.

## 🃏 Review Questions

**Q1**: What is opaque recurrence and why does it matter for AI safety?
**A**: Opaque recurrence (also called recurrent depth) is an architecture where a model loops queries through internal layers repeatedly, reducing the legibility of its reasoning traces and complicating human oversight of intermediate steps.

**Q2**: What is the MCP and where did it originate?
**A**: The Model Context Protocol is an Anthropic-originated open standard that connects AI models to external tools and data sources, described as "a USB-C port for AI" for its role as a universal connectivity layer.

**Q3**: How does the concept of neuralese represent an extreme risk scenario?
**A**: Neuralese describes a hypothetical future where a model reasons entirely in internal numeric representations with no human-readable intermediate states — the logical endpoint of trends like opaque recurrence, where alignment verification becomes impossible.

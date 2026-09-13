---
type: literature-note
source_url: https://machinelearningmastery.com/fine-tuning-agentic-ai-a-practical-guide/
author: Shittu Olumide
tags: [fine-tuning, agentic-ai, qlora, dpo]
date_consumed: 2026-09-13
---

## Summary

Fine-tuning agentic AI in 2026 requires solving four distinct problems: training data quality, parameter-efficient weight updates via [[QLoRA]], runtime hyperparameters, and preference alignment via [[DPO]]. Format quality of training examples matters more than volume — a few hundred well-structured tool-calling examples outperform thousands of loosely formatted ones. Skipping any single component is the most common cause of agentic systems that succeed in demos but fail on real traffic.

## Core Concepts

- [[Agentic AI]] fine-tuning targets three gaps prompting alone cannot close: exact output schema compliance, narrow domain vocabulary, and consistent behavior.
- [[QLoRA]] (Quantized Low-Rank Adaptation) freezes the base model in 4-bit precision and trains small low-rank adapter matrices, enabling 70B-class models on single-GPU hardware. Key config: `r=4`, `lora_alpha=32`, `lora_dropout=0.05` — only 1.7% of total parameters end up trainable.
- [[Direct Preference Optimization]] (DPO) extends [[Supervised Fine-Tuning]] (SFT) by learning from paired (chosen, rejected) examples where both responses are syntactically correct but one is contextually preferred — e.g., `escalate_to_human` over `issue_refund` for a high-value ambiguous claim.
- [[Runtime Hyperparameters]]: temperature, iteration limits, and retry policies measurably affect production success rates. A retry policy is often a cheaper lever than additional training.
- [[Catastrophic Forgetting]]: fine-tuning for a narrow task risks degrading general capability; evaluation must track both tool-call accuracy and general benchmark scores (e.g., [[MMLU]], [[GSM8K]]).
- Dataset construction pipeline: write 150–200 seed examples → expand with a stronger teacher model → discard bottom 10–20% by score.

## Key Takeaways

- **Four pillars required**: validated dataset, QLoRA adapter, tuned runtime settings, DPO alignment.
- **Format over volume**: exact schema compliance in training rows beats raw example count.
- **Validate before training**: a `validate_examples` function catches bad tool calls pre-training, preventing the model from learning to hallucinate arguments.
- **Retry > re-train**: temperature 0.7 + retry reached 98.7% success — higher than single-shot 0.0.
- **DPO fills the SFT gap**: SFT only labels correctness; DPO expresses "correct but not the best choice here."
- **Ship verdicts need two signals**: tool accuracy must improve AND general capability drop must stay under 3 percentage points.
- **Evaluation is the finish line**, not the training run.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Optimizing a model solely on tool-call accuracy (the measurable proxy) risks collapsing general capability — the actual goal. The dual-metric SHIP/HOLD framework directly guards against this failure mode.
- **[[Diminishing Returns]]**: The dataset-construction pipeline (seed → expand → filter) embodies the insight that quality of examples has sharply diminishing returns past a threshold; adding low-quality rows actively degrades performance.

## 🃏 Review Questions

**Q1**: What three specific gaps does agentic fine-tuning address that prompting alone cannot reliably close?
**A**: Exact output schema compliance, narrow domain vocabulary, and consistent behavior at inference time. It does not fix missing knowledge — that requires retrieval.

**Q2**: What QLoRA configuration was validated in a peer-reviewed tool-agent setup, and what fraction of parameters does it train?
**A**: `r=4`, `lora_alpha=32`, `lora_dropout=0.05` targeting the projection matrices; only 1.7% of total parameters are trainable, with the base model frozen in 4-bit precision.

**Q3**: How does the SHIP/HOLD evaluation framework prevent shipping a regressed model?
**A**: It requires both tool-call accuracy to improve AND general capability drop to remain within a 3 percentage-point threshold — a model that gains task accuracy but loses more than 3 points on general benchmarks receives a HOLD verdict.

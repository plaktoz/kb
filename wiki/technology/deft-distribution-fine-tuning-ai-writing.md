---
type: literature-note
source_url: https://every.to/working-overtime/i-tried-the-ai-model-built-to-fix-ai-writing
author: Katie Parrott
tags: [ai-writing, fine-tuning, language-models, deft]
date_consumed: 2026-09-03
---

## Summary

Katie Parrott reviews Deft, a writing-focused AI lab and model that frames the flatness of AI prose as a training distribution problem. Standard fine-tuning evaluates outputs one at a time, which allows repetitive rhythms to persist across a large batch; Deft's "distribution fine-tuning" (DFT) method compares batches of model output against batches of human writing and adjusts when the two distributions diverge. While the approach improves sentence-level variety, the model still hallucinates, has weak information hierarchy, and is not ready for daily production use.

## Core Concepts

- **[[Distribution Fine-Tuning]] (DFT)**: Deft's core technique — compare batches of model output to batches of human writing and penalize divergence at the distributional level, not the individual-output level.
- **[[AI Writing Flatness]]**: The homogeneous, repetitive quality of AI prose attributed to per-sample evaluation during training, which lets collectively samey outputs each pass review.
- **[[Deft]]**: A new writing-focused AI lab cofounded by [[Justin Murphy]] and researcher Rosmine, building on DFT to produce more varied prose.
- **[[Training Distribution Problem]]**: The root-cause framing Deft adopts — AI writing sameness is a data/training issue, not purely a prompting or post-processing one.
- **[[Hallucination]]**: Deft's "strict mode" failed to prevent invented facts, dates, and dialogue, indicating the variety gains come at a reliability cost.

## Key Takeaways

- **Core diagnosis**: AI writing flatness stems from per-sample review, not bad prompts.
- **DFT mechanism**: Batch-level comparison catches collective repetition single-sample eval misses.
- **Variety win**: Parrott found prose "more varied and surprising than most AI writing."
- **Reliability failure**: Model invented facts and dialogue not present in the source brief.
- **Information hierarchy**: Gains in variety were undercut by weak sequencing and structure.
- **API limitations**: Returns completed chunks, not iterative collaboration.
- **Verdict**: Proof-of-concept that sameness is trainable, but not production-ready.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Evaluating each output independently optimizes for passing individual review — the wrong proxy — allowing collective sameness to persist undetected even as every single sample "looks fine."
- **[[Systems Thinking]]**: Treating AI writing quality as an emergent property of the *distribution* rather than any single output is a shift from reductionist to systems-level diagnosis.

## 🃏 Review Questions

**Q1**: What is Deft's central argument about why AI writing sounds flat?
**A**: AI prose flatness is a training distribution problem — standard fine-tuning evaluates outputs one at a time, so repetitive rhythms can survive review even when a thousand samples collectively echo the same openings and rhythms.

**Q2**: How does distribution fine-tuning (DFT) differ mechanically from standard fine-tuning?
**A**: DFT compares *batches* of model output against batches of human writing and adjusts training when the two distributions diverge, catching collective patterns that per-sample evaluation misses.

**Q3**: What does Parrott's review suggest about the practical readiness of Deft for daily writing work?
**A**: Despite genuine improvements in sentence-level variety, the model hallucinates facts and dialogue, has weak information hierarchy, and offers limited API collaboration — Parrott says she would not use it for daily work yet.

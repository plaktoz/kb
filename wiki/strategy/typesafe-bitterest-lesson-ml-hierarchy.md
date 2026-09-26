---
type: literature-note
source_url: https://typesafe.ai/blog/bitterest-lesson
author: Unknown
tags: [machine-learning, task-selection, optimization, ai-research]
date_consumed: 2026-09-26
---

## Summary

The post extends [[Rich Sutton]]'s "bitter lesson" — that compute beats clever algorithms — into a fuller hierarchy: *doing the right task > data > compute > algorithms*. Most ML research attacks this hierarchy in reverse, obsessing over algorithms and scaling while neglecting task selection and data quality. The InstructGPT example shows that models 100× smaller than GPT-3 outperformed it on instruction-following simply by training on the correct objective.

## Core Concepts

- **[[Bitter Lesson]] (extended)** — the full ML priority hierarchy is: right task > data > compute > algorithms; Sutton's original lesson only captured compute > algorithms
- **[[Task Selection]]** — choosing the right optimization objective is the highest-leverage decision in ML; requires stepping outside ML entirely to understand users, products, and real-world systems
- **[[InstructGPT]] example** — GPT-2-scale models trained for instruction-following outperformed GPT-3 significantly; reaching the same capability via pure pre-training scale would have required roughly "GPT-7 level"
- **[[Goodhart's Law]] (implied)** — when loss curves become the target, models optimize for loss, not for external usefulness
- **[[Mode Optimization]]** — "you get what you optimize for" — beautiful training metrics mean nothing if the objective is misspecified

## Key Takeaways

- **Hierarchy**: right task > data > compute > algorithms — most research inverts this
- **Scale is powerful but insufficient**: even massive models trained on wrong objectives underperform small models on the right task
- **Task clarity requires non-ML work**: user research, product understanding, systems thinking
- **InstructGPT lesson**: correct task selection was worth more than 100× parameter scaling
- **Most important ML work isn't ML**: defining the right objective and curating the right data

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: optimizing for a proxy (loss curves, benchmark scores) instead of the true objective causes models to excel at the metric while failing at the real task — the entire post is an argument that RLHF optimizes for the wrong proxy.
- **[[First Principles Thinking]]**: the post argues you must derive what the model should *actually* do from external reality (users, systems, outcomes) rather than inheriting the prevailing training paradigm.

## 🃏 Review Questions

**Q1**: What is the full ML hierarchy the post argues for, and why does it extend Sutton's original lesson?
**A**: The hierarchy is: doing the right task > data > compute > algorithms. Sutton's lesson only covered compute > algorithms — the post adds that task selection and data quality matter even more than scale.

**Q2**: What does the InstructGPT example demonstrate about the relationship between model size and task alignment?
**A**: GPT-2-scale models trained for instruction-following outperformed GPT-3 on that task; the correct objective was worth more than ~100× scaling, and matching the baseline purely through pre-training scale would have required GPT-7-level parameters.

**Q3**: What does this hierarchy imply for how ML practitioners should spend their time?
**A**: The most important work is often not ML at all — it requires studying users, products, and real-world systems to define the right optimization objective before writing a single line of training code.

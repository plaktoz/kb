---
type: literature-note
source_url: https://docs.typesafe.ai/introduction/machine-learning-primer
author: Unknown
tags: [rlcd, rlhf, machine-learning, ai-training]
date_consumed: 2026-09-26
---

## Summary

TypeSafe's ML primer argues that large-scale automation will be ~99% machine-to-machine interactions, making "machine-native intelligence" a distinct optimization target from human-facing chat. Three post-training methods are contrasted — RLHF (human preference), RLVR (verifiable rewards), and RLCD (TypeSafe's calibrated decisions) — with RLCD specifically targeting calibrated probability outputs for structured automation tasks. Notably, [[RLHF]] was co-invented by [[Diogo Almeida]], a TypeSafe cofounder.

## Core Concepts

- **[[Machine Native Intelligence]]** — AI optimized for software-like properties (structure, reliability, observability, low cost) rather than human-facing naturalness
- **[[RLHF]] (Reinforcement Learning from Human Feedback)** — trains models to produce responses humans prefer; co-invented by [[Diogo Almeida]] (TypeSafe cofounder); risks sycophancy and confident hallucination
- **[[RLVR]] (Reinforcement Learning from Verifiable Rewards)** — optimizes for programmatically verifiable correctness (e.g. math); strong but slower and costlier
- **[[RLCD]] (Reinforcement Learning for Calibrated Decisions)** — TypeSafe's method; returns decisions with calibrated probabilities instead of text; targets the 99% machine-to-machine automation use case
- **[[Mode Dropping]]** — RLHF narrows a model's output distribution toward a preferred style, suppressing valid alternatives; a milder form of [[GAN Mode Collapse]]
- **Calibration** — a well-calibrated model predicting 0.8 confidence should be correct ~80% of the time across many predictions (not a per-answer guarantee)

## Key Takeaways

- **99% machine-to-machine**: TypeSafe's bet — most future automation is software-to-software, not human-facing
- **RLHF trade-off**: optimizes for compelling responses, not reliable unattended automation
- **Mode dropping**: RLHF narrows output distribution; models favor one style and suppress alternatives
- **RLCD goal**: calibrated probabilities on structured tasks, not human preference scores
- **Diogo Almeida** co-invented RLHF before founding TypeSafe — insider understanding of the failure modes
- **Calibration ≠ per-answer accuracy**: 0.8 confidence = correct 80% of the time across many predictions

## 🧠 First Principles & Mental Models

- **[[Optimization Target Specificity]]**: The choice of what to optimize for fully determines the model's behavior in production. RLHF and RLCD both train with RL, but on different reward signals — the result is models that behave completely differently in automation pipelines, not just in chat.

## 🃏 Review Questions

**Q1**: What is TypeSafe's core bet about the future of AI, and how does it shape their training approach?
**A**: TypeSafe bets that ~99% of large-scale automation will be machine-to-machine rather than human-facing, so they optimize for software-like reliability and calibrated uncertainty rather than natural-sounding responses.

**Q2**: What is mode dropping in RLHF, and why does it matter for automation?
**A**: RLHF narrows a model's output distribution toward a preferred style, suppressing other valid outputs — in automation, this creates systems that are confidently wrong in hard-to-detect ways rather than honestly expressing uncertainty.

**Q3**: What does it mean for a model to be "well-calibrated," and why is calibration important for autonomous systems?
**A**: A well-calibrated model's confidence scores match actual accuracy frequencies — 0.8 confidence means ~80% correct across many predictions. For autonomous systems, calibrated uncertainty is what enables confident decisions to act automatically while uncertain ones route to humans.

---
type: literature-note
source_url: https://www.forbes.com/councils/forbestechcouncil/2026/11/09/when-to-build-your-own-ai-model-and-when-to-stop-kidding-yourself
author: Eilon Reshef
tags: [fine-tuning, small-language-models, post-training, ai-economics]
date_consumed: 2026-11-10
---

## Summary
Fine-tuning or post-training a small language model is an engineering decision, not a proprietary moat; the defensible assets are the data, feedback loops, evaluations, and application harness around the model. The decision to post-train rests on scale, task specificity, an exhausted prompting baseline, and negotiation leverage, and it carries ongoing operational costs. The practical rule is to start broad, measure everything, and specialize only when the task is stable and the economics justify it.

## Core Concepts
- [[Post-Training]]: [[Fine-Tuning]], preference optimization, reinforcement learning, and [[Distillation]] applied to an existing model.
- [[Small Language Models]] (SLMs): specialized models that can beat off-the-shelf models on a narrow job at the same or lower cost.
- [[Economic Moat]]: proprietary data, feedback loops, evaluation, and the application harness, not the model work itself.
- [[Prompt Engineering]] as baseline, including automatic prompt optimizers.
- [[LLM Evaluation]]: a human-approved gold set run against every prompt, model, and fine-tune change.
- [[Switching Costs]] created by a learning system that makes the underlying model replaceable.
- [[Model Drift]] and operational burden of self-hosting.
- Author Eilon Reshef's experience at [[Gong]] with transfer learning before LLMs.

## Key Takeaways
- **No Moat**: Saying "we fine-tune" is as distinctive as "we use a database."
- **Scale**: Economics work at millions of monthly calls, usually not at thousands.
- **Task Specificity**: Fine-tuning suits narrow, repeatable tasks with a high quality bar.
- **Prompting First**: Exhaust prompt engineering, including automatic optimizers, before changing model weights.
- **Negotiation Leverage**: At fine-tuning scale, ask whether to renegotiate the API contract.
- **Evals Prerequisite**: Without gold-set evaluation, real gains look identical to overfit demos.
- **Operations**: You own uptime, scaling, monitoring, hardware, and capacity planning.
- **Model Aging**: Fine-tuned models are snapshots; retraining and drift tracking need ongoing staff.
- **Other Reasons**: Latency, control, and privacy can justify fine-tuning beyond cost.

## 🧠 Core Principles

**T1. Capability that is widely reproducible is not a moat** — An advantage durable enough to defend comes from what compounds with use, such as proprietary data, feedback loops, and workflow integration, rather than from a technique competitors can also apply. · *model:* [[Economic Moat]]
→ explains: No Moat

**T2. Fixed costs only pay off at sufficient volume** — Post-training has meaningful upfront and maintenance costs, so specialization pays only when enough usage amortizes them. · *model:* [[Economies of Scale]]
→ explains: Scale, Operations, Model Aging

**T3. Measure before you optimize** — Without a representative baseline and evaluation set, improvements cannot be distinguished from overfitting, so cheaper options are exhausted and measured first.
→ explains: Prompting First, Evals Prerequisite

## 🃏 Review Questions

**Q1**: Why does the author say fine-tuning your own model is not a moat?
**A**: Fine-tuning is an engineering decision, as undistinctive as using a database. What is defensible is proprietary data, feedback loops, evaluation, and the application harness that make the underlying model replaceable.

**Q2**: What four factors drive the decision to post-train, and what is the prerequisite?
**A**: Scale, task specificity, prompting as the baseline, and negotiation leverage. The prerequisite is strong evaluation using a human-approved gold set run through every prompt revision, model upgrade, and fine-tune.

**Q3**: What should a team do before committing to post-training, and what ongoing costs should it expect?
**A**: Push prompt engineering as far as possible and consider renegotiating the API contract. After that, it must budget for self-hosting operations and for retraining as models age and data drifts.

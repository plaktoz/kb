---
type: literature-note
source_url: https://techcrunch.com/2026/09/02/openais-new-reasoning-technique-alarms-ai-safety-experts/
author: Russell Brandom
tags: [openai, ai-safety, chain-of-thought, interpretability]
date_consumed: 2026-09-03
---

## Summary

[[OpenAI]]'s upcoming [[Astra]] model uses a technique called "recurrent depth" (also called "opaque recurrence") that processes queries in loops rather than sequentially, making internal reasoning states harder to inspect. This reduction in [[Chain-of-Thought]] legibility has alarmed AI safety researchers who rely on CoT monitoring as a key oversight mechanism. OpenAI maintains the approach is safe and that Astra's CoT remains largely readable, but critics warn the technique could spread industry-wide and erode a foundational safety tool.

## Core Concepts

- **[[Recurrent Depth]]** (opaque recurrence): A compute-efficient reasoning architecture where the model loops over the same layers repeatedly instead of stacking more sequential layers — improving performance while reducing interpretability of intermediate states.
- **[[Chain-of-Thought Monitorability]]**: The property that allows humans and oversight systems to read a model's step-by-step reasoning. Recurrent depth threatens this by pushing reasoning toward "latent space" rather than legible tokens.
- **[[Latent Space Reasoning]]**: A failure mode where models reason "entirely or almost entirely in latent space," bypassing human-readable CoT and making alignment verification much harder.
- **[[OpenAI]]**, **[[Anthropic]]**, and **[[Google DeepMind]]**: All three frontier labs are reportedly exploring recurrent depth, suggesting competitive pressure may accelerate adoption.

## Key Takeaways

- **Legibility vs. efficiency trade-off**: Recurrent depth gains compute efficiency at the cost of interpretable reasoning steps.
- **Safety community alarm**: Redwood CEO [[Buck Shlegeris]] warned the technique could "totally destroy CoT monitorability" at scale.
- **Race-to-the-bottom risk**: [[Zvi Mowshowitz]] called it "playing with fire" and suggested legislation may be needed.
- **Latent space risk**: Redwood's [[Ryan Greenblatt]] fears gradual drift toward fully opaque, latent-space reasoning across the industry.
- **OpenAI's defense**: Chief scientist [[Jakub Pachocki]] says the company will preserve CoT monitoring and won't shift to "neuralese."
- **Industry-wide spread**: Anthropic and Google DeepMind are reportedly already exploring the same technique.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: If labs optimize for reasoning performance as the primary metric, CoT legibility — an observable proxy for alignment — gets sacrificed, even though it was never the target they claimed to optimize.
- **[[Race to the Bottom]]**: When multiple frontier labs independently adopt opaque reasoning for competitive advantage, no single actor can unilaterally stop — a classic coordination failure requiring external (regulatory) intervention, exactly what Mowshowitz argues for.

## 🃏 Review Questions

**Q1**: What is the core claim of this article?
**A**: OpenAI's recurrent depth technique makes its Astra model's internal reasoning harder to inspect, threatening chain-of-thought monitorability — a key mechanism AI safety researchers rely on for oversight.

**Q2**: How does recurrent depth work, and why does it reduce interpretability?
**A**: Instead of adding more sequential processing layers, the model loops over the same layers repeatedly; this compresses reasoning into hard-to-read latent states rather than producing legible step-by-step tokens.

**Q3**: What is the practical safety implication if this technique becomes industry standard?
**A**: Safety researchers would lose the ability to monitor or verify a model's reasoning process in real time, making it much harder to detect deceptive or misaligned behavior before it causes harm.

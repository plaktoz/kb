---
source_url: https://docs.typesafe.ai/introduction/machine-learning-primer
author: Unknown
date: 2026-09-26
---

# AI Primer — TypeSafe

TypeSafe builds what it calls "Machine Native Intelligence" — AI designed for software-like properties: structure, reliability, observability, and low cost.

## Core Premise

The company bets that large-scale automation will be ~99% machine-to-machine interactions. This shifts the design goal away from responses that feel natural toward outputs that behave predictably inside software pipelines.

## Three Post-Training Approaches

| Method | Focus |
|--------|-------|
| **RLHF** | Trains models to produce responses humans prefer (chatbots) |
| **RLVR** | Verifiable rewards; strong at math but slower/costlier |
| **RLCD** | TypeSafe's approach — returns decisions and calibrated probabilities |

RLHF was co-invented by Diogo Almeida, a TypeSafe cofounder.

## What RLCD Delivers

Rather than generating text, the model returns decisions with probabilities. A well-calibrated model means predictions at 0.8 confidence should prove correct roughly 80% of the time — across many predictions, not as a per-answer guarantee.

## Problems with RLHF

Optimizing for human preference can reward sycophancy and confident hallucinations. It also causes **mode dropping** — the model narrows its output distribution, favoring one style while suppressing others. This is a milder form of GAN-style mode collapse.

> "An output can be compelling to a person without being reliable enough for unattended automation."

TypeSafe argues production automation requires a different objective: constrained decisions with calibrated uncertainty.

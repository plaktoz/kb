---
source_url: https://techcrunch.com/2026/09/02/openais-new-reasoning-technique-alarms-ai-safety-experts/
title: OpenAI's new reasoning technique alarms AI safety experts
author: Russell Brandom
date: 2026-09-02
---

# OpenAI's new reasoning technique alarms AI safety experts

**Author:** Russell Brandom
**Date:** September 2, 2026
**Source:** TechCrunch

OpenAI's upcoming Astra model employs a technique called "recurrent depth" (or "opaque recurrence"), which allows the model to process queries in loops rather than sequentially. This reduces the legibility of its chain-of-thought (CoT) reasoning, alarming safety researchers.

## Key Concerns from Experts

- Redwood CEO Buck Shlegeris warned that scaling this technique could **"totally destroy CoT monitorability."**
- Safety advocate Zvi Mowshowitz called it **"playing with fire"** and suggested legislation may be needed to prevent a race to the bottom among labs.
- Redwood Research's Ryan Greenblatt feared a natural progression toward models reasoning **"entirely or almost entirely in latent space."**

## OpenAI's Position

Chief scientist Jakub Pachocki defended the company's commitment: *"OpenAI has worked to preserve and utilize chain-of-thought monitoring since our very first reasoning models."* The company says Astra's CoT remains largely legible and it won't shift to "neuralese."

## Broader Context

Both Anthropic and Google DeepMind are reportedly already exploring similar techniques, raising industry-wide concerns. The "recurrent depth" approach enables more compute-efficient reasoning by looping over the same layers repeatedly rather than adding more sequential layers, but this comes at the cost of interpretability — the internal states become harder for humans (or oversight systems) to read.

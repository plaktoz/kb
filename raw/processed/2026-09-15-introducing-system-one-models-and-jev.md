---
source_url: https://typesafe.ai/blog/introducing-system-one-models-and-jev
author: Diogo Almeida
date: 2026-09-15
---

# Introducing System One Models & Jev

TypeSafe AI is launching a new class of frontier models called **System One Models**, designed for fast, structured decision-making that software can consume directly. The announcement centers on their first public model, **Jev**, now available in early access.

Founder Diogo Almeida, formerly at OpenAI where he contributed to ChatGPT's instruction-following research, frames the core problem: despite years of superhuman chat performance, widespread automation hasn't materialized. His conclusion was that something fundamental was missing.

## What Makes System One Models Different

Unlike conventional LLMs trained via RLHF/RLVR and optimized for human-preferred text generation, Jev is trained using **Reinforcement Learning for Calibrated Decisions (RLCD)**, targeting epistemically honest probability outputs on structured tasks.

Key distinctions:

- **Outputs:** Type-safe structured values instead of free-form strings; the model "can't hallucinate" by design
- **Sampling:** Parallel generation rather than sequential token-by-token inference
- **Speed:** 70–500ms end-to-end, described as "40x–200x faster" than comparable frontier models
- **Cost:** $0.042/MTok input; output tokens are free
- **Confidence:** Every output includes calibrated probabilities

The model is described as: *"a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out."*

## Target Use Cases

- AI-powered workflow automation ("smart if-statements")
- Map-reducing over large datasets
- Real-time applications requiring sub-100ms AI
- Guardrailing, scoring, and verifying LLM outputs

## Evidence & Benchmarks

TypeSafe published **workflow evals** comparing Jev against leading LLMs. Rather than optimizing for ground-truth classification, the eval framework uses predictions from large external models (GPT-6 Astra and Fable 5.1) as reference probabilities. Claims of **193.6x faster** and **444.6x cheaper** stem from these evals, though the company acknowledges these likely represent the higher end of real-world gains.

Demos include a real-time DOOM-playing bot (making ~10 AI queries/second) and a Wikiracing agent navigating Wikipedia link graphs.

## Naming

- *"System One Models"* draws from Kahneman's fast/intuitive System 1 thinking framework
- *"Jev"* honors economist William Stanley Jevons — a nod to the expectation that cheaper intelligence, like more efficient steam engines, will dramatically expand demand rather than reduce it

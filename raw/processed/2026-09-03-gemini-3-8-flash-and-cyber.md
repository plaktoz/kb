---
source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
title: Introducing Gemini 3.8 Flash and 3.8 Flash Cyber
author: Tulsee Doshi; Raluca Ada Popa
date: 2026-09-02
---

# Introducing Gemini 3.8 Flash and 3.8 Flash Cyber

**Authors:** Tulsee Doshi (Senior Director, Product Management) and Raluca Ada Popa (Gemini Security Lead, Google DeepMind)

**Published:** September 2, 2026

Google introduced two new Gemini models built on shared foundational intelligence, enhanced by long-running agentic loops.

## Gemini 3.8 Flash

Gemini 3.8 Flash is described as Google's "most intelligent workhorse model," priced at $0.75/million input tokens and $3.75/million output tokens (introductory rate through end of 2026). It outperforms larger frontier models on DeepSWE v1.1 (long-horizon software engineering) and scores 54.9% on HLE-Verified. It also leads on finance and legal agent benchmarks.

The model is designed to work harder on complex tasks — executing additional reasoning steps and iterative tool calls, sometimes using more tokens to maximize results.

## Gemini 3.8 Flash Cyber

Gemini 3.8 Flash Cyber targets trusted defenders via Google's new Fairwind Program. It exceeds previous Cyber models and larger rivals on CyberGym vulnerability detection. On an internal benchmark spanning 20 programming languages, it surpasses 70% success in vulnerability discovery. On the CWE-Bench patching benchmark, it achieves 47.2% pass@1 at significantly lower cost than comparable frontier models.

Real-world results include:
- Chrome Security found it produced 2.6x more correct patches than leading commercial alternatives
- Google's Cloud team used it to find a critical vulnerability in under two hours

## Safety

Both models include CBRN and cyber-offense safeguards, and show marked improvement on Gray Swan's prompt-injection robustness benchmark.

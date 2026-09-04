---
source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
title: Introducing Gemini 3.8 Flash and 3.8 Flash Cyber
author: Tulsee Doshi; Raluca Ada Popa
date: 2026-09-02
---

# Introducing Gemini 3.8 Flash and 3.8 Flash Cyber

**Authors:** Tulsee Doshi (Senior Director, Product Management) & Raluca Ada Popa (Gemini Security Lead, Google DeepMind)
**Date:** September 2, 2026

Google announced two new Gemini models focused on agentic workflows and cybersecurity, representing the third Flash release in six weeks.

## Gemini 3.8 Flash

Described as their "most intelligent workhorse model," it brings improvements in software engineering, agentic tasks, and multi-step reasoning. Pricing is $0.75/million input tokens and $3.75/million output tokens (introductory rate through December 31, 2026).

Key benchmark highlights:
- Outperforms larger frontier models on **DeepSWE v1.1** (long-horizon software engineering)
- Strong results on Vals Finance Agent V2 and Harvey's Legal Agent Benchmark
- Achieves **54.9% on HLE-Verified** across STEM, humanities, and professional domains

The model is designed to "work harder" on complex tasks — executing additional reasoning steps and iterating tool calls, sometimes using more tokens for maximum performance.

## Gemini 3.8 Flash Cyber

Available exclusively to trusted defenders via Google's new **Fairwind Program**, this variant targets cybersecurity professionals with:

- Frontier-level performance on **CyberGym** (vulnerability discovery benchmark)
- Over **70% success rate** on an internal benchmark spanning 20 programming languages
- On **CWE-Bench** (patching), achieves 47.2% pass@1 — competitive with a leading model at 47.8%, but at significantly lower cost

Real-world results cited include Chrome Security finding 2.6x more correct vulnerability patches than larger commercial models, and Google's Cloud Vulnerability Research team discovering a critical vulnerability in under 2 hours.

## Safety

Both models include safeguards against CBRN and cyber-offense misuse. A notable improvement in **prompt injection robustness** is highlighted, measured via the Gray Swan IPI Benchmark.

## Availability

- **Developers:** Google AI Studio, Android Studio, Gemini API
- **Enterprises:** Gemini Enterprise
- **Consumers:** Gemini app (Pro/Ultra subscribers), AI Mode in Search, Google Sheets
- **Cyber variant:** Via Fairwind Program application only

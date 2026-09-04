---
source_url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/
title: Introducing Gemini 3.8 Flash and 3.8 Flash Cyber
author: Tulsee Doshi, Raluca Ada Popa
date: 2026-09-02
---

# Introducing Gemini 3.8 Flash and 3.8 Flash Cyber

**Authors:** Tulsee Doshi (Senior Director, Product Management) and Raluca Ada Popa (Gemini Security Lead, Google DeepMind)

**Date:** September 2, 2026

Google introduced two new Gemini models building on the 3.7 Flash release from three weeks prior — their third Flash release in six weeks.

## Gemini 3.8 Flash

Described as Google's "most intelligent workhorse model," priced at $0.75/million input tokens and $3.75/million output tokens (introductory rate through end of 2026). It shows strong gains in software engineering, agentic tasks, and multi-step reasoning.

Key benchmarks:
- On the DeepSWE v1.1 benchmark, it outperforms most larger frontier models at lower cost
- Scores 54.9% on HLE-Verified
- Leads on finance and legal agent benchmarks

## Gemini 3.8 Flash Cyber

A specialized cybersecurity model, restricted to trusted defenders through Google's new Fairwind Program.

Key highlights:
- Surpasses prior models on the CyberGym vulnerability discovery benchmark
- Over 70% success on an internal multi-language vulnerability benchmark (20 languages)
- Near-parity with leading frontier models on patch generation (CWE-Bench: 47.2% vs. 47.8%) at significantly lower cost
- Chrome Security team found it produced "2.6 times more correct patches" than larger commercial models
- Helped Google Cloud find a critical vulnerability "in less than 2 hours"

## Safety

Both models include safety mitigations against CBRN and cyber-offense misuse, and both show improvements in prompt injection robustness per Gray Swan benchmarks.

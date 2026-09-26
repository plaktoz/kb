---
type: literature-note
source_url: https://every.to/also-true-for-humans/how-to-create-your-own-personal-ai-benchmark
author: Mike Taylor
tags: [ai-evaluation, benchmarking, llm-testing, model-selection]
date_consumed: 2026-09-26
---

## Summary

Standard AI benchmarks measure trivia and math competitions, not real work — making them poor guides for model selection. Mike Taylor, head of evals at Every, proposes a three-stage framework for building a personal benchmark grounded in your actual failures and preferences. The goal is to confidently route routine tasks to cheaper models and ambitious work to frontier models.

## Core Concepts

- **[[AI Evaluation]] (evals)**: Systematic testing of [[LLM]] outputs against defined quality criteria
- **Back-pocket evals**: A curated set of ~10 real tasks where AI previously failed or was abandoned, used as a personal test suite
- **Pass/fail checks vs. numeric scores**: Binary judgments are more actionable because LLMs artificially cluster numeric ratings
- **Discernment horizon**: The threshold at which a cheaper model is good enough for a given task class
- **[[Benchmark Saturation]]**: As models improve, previously hard tasks become trivial; benchmarks must escalate difficulty to remain calibrated
- **Eval folder structure**: `prompt.txt`, `context/`, `gold/` (ideal output), and `evals.py` per task — a reproducible unit of measurement

## Key Takeaways

- **Collect failures first**: Identify ~10 tasks where AI struggled in the past month.
- **Capture full context**: Include reference files and guidance so the eval is reproducible.
- **Run in parallel**: Compare multiple models side-by-side on the same task.
- **Turn taste into rubrics**: Dictate preferences via voice, then convert to pass/fail checks.
- **Avoid numeric scores**: LLMs cluster ratings; binary pass/fail is more actionable.
- **Scale to 20+ examples**: Fewer examples reflect flukes, not consistent capability.
- **Cheap models often suffice** for routine tasks (dashboards, simple decks).
- **Frontier models separate** on open-ended, multi-step, ambiguous work.
- **Benchmarks expire**: Escalate difficulty as models improve to stay calibrated.
- **End goal**: Systematic routing — cheap for routine, frontier for ambitious.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Standard benchmarks become targets that model developers optimize for, divorcing them from real-world utility — Taylor's personal benchmark sidesteps this by grounding evals in actual work failures rather than proxy metrics.
- **[[Signal vs. Noise]]**: Pass/fail checks eliminate artificial score clustering, surfacing genuine quality differences that numeric ratings obscure.

## 🃏 Review Questions

**Q1**: What is the core problem with standard AI benchmarks that motivates building a personal one?
**A**: Standard benchmarks test trivia and math competitions, not your actual work — so they give poor signal for which model to use on real tasks you care about.

**Q2**: Why does the author recommend pass/fail checks instead of numeric scores when building evals?
**A**: LLMs artificially cluster numeric ratings (e.g., everything scores 7–8), making them hard to act on; a binary pass/fail judgment is clearer and more actionable.

**Q3**: How should you use a personal benchmark once it's built?
**A**: Route routine, well-defined tasks to cheaper models that clear the "discernment horizon," and reserve expensive frontier models for open-ended, multi-step work where top-tier capability actually shows.

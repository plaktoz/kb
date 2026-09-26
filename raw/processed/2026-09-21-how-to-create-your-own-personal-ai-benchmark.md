---
source_url: https://every.to/also-true-for-humans/how-to-create-your-own-personal-ai-benchmark
author: Mike Taylor
date: 2026-09-21
---

# How to Create Your Own Personal AI Benchmark

Standard AI benchmarks test trivia and math competitions — not your actual work. The author, head of evals at Every, proposes building a personal benchmark in three stages:

## 1. Collect Your Failures ("Back-Pocket Evals")

Review the past month and identify ~10 tasks where AI struggled or was abandoned. Capture full context (reference files, guidance), then run those tasks across multiple models in parallel, comparing outputs side by side.

## 2. Turn Taste Into Tests

Dictate preferences via voice mode ("this headline was boring," "sounds like AI writing"), then have a model convert that feedback into a rubric. Use **pass/fail checks** — not numeric scores — since LLMs cluster ratings artificially and a binary judgment is more actionable.

## 3. Scale Into a Real Benchmark

Build a folder structure with `prompt.txt`, `context/`, `gold/` (ideal output), and `evals.py` per task. Accumulate 20+ examples per skill so results reflect consistency, not flukes.

## Key Takeaways

- **Cheap models often clear the "discernment horizon"** for routine tasks (dashboards, simple decks), making expensive frontier models unnecessary there.
- **Harder tasks reveal real differences** — open-ended, multi-step work is where top-tier models separate themselves.
- **Benchmarks expire.** As models improve, tasks get saturated. Keep escalating difficulty to stay calibrated.
- The goal: route routine work to cheaper models, ambitious work to frontier ones — confidently and repeatedly.

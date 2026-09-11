---
type: literature-note
source_url: https://every.to/context-window/evals-for-everyone
author: Laura Entis
tags: [ai-evaluation, benchmarks, llm, productivity]
date_consumed: 2026-09-11
---

## Summary

Every is building personal AI benchmarks for each employee — custom evaluation sets that test how well models handle individual work tasks, graded against personal quality standards. Rather than relying on public benchmarks where top models score 93–96% on graduate science tests, this approach captures idiosyncratic preferences like comma placement and slide density. The goal is to turn one-off corrections into a reusable, compounding system that improves model selection and prompting over time.

## Core Concepts

- **[[Personal AI Evals]]**: Custom benchmark sets built per employee, testing recurring tasks against individual quality criteria rather than generic academic metrics.
- **[[AI Judge]]**: An AI model that grades outputs against human-defined yes/no checklists, with disagreements used to refine the checks themselves.
- **[[Compounding Loop]]**: Dan Shipper's framing — each round of eval refinement makes the benchmark more accurate, progressively improving model selection and prompting.
- **[[Model Selection]]**: Personal evals revealed that smaller models (e.g. [[GPT-5.6 Luna]]) can outperform larger ones on specific daily tasks — public benchmarks miss this signal entirely.
- **[[Mike Taylor]]**: Head of evals at Every who piloted the personal benchmark program.

## Key Takeaways

- **Public benchmarks are insufficient**: Top models cluster at 93–96% on graduate science tests — useless for distinguishing daily-task performance.
- **Idiosyncratic quality matters**: Personal evals capture stylistic preferences (comma placement, idea count per slide) that generalized tests cannot.
- **Smaller models can win**: GPT-5.6 Luna outperformed larger models on many of Mike Taylor's daily tasks after benchmarking.
- **Five-step DIY workflow**: Identify task → save prompt/files → convert feedback to yes/no checks → AI grades output → resolve disagreements by clarifying checks.
- **Self-improving system**: Disagreements between human and AI grades refine the checks, making the benchmark more precise over time.
- **Reusable system beats one-off corrections**: Converting ad-hoc fixes into structured checks creates durable, reusable evaluation infrastructure.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Public benchmarks become targets that models optimize for, decoupling them from real-world task performance — personal evals restore the direct connection between metric and goal.
- **[[Feedback Loops]]**: Converting one-off corrections into structured yes/no checks creates a tightening feedback loop that improves both model selection and prompt quality with each iteration.

## 🃏 Review Questions

**Q1**: What is the core problem with relying on public AI benchmarks for selecting models for personal work?
**A**: Top models score similarly (93–96%) on graduate science tests, making public benchmarks useless for distinguishing performance on idiosyncratic daily tasks with personal quality standards.

**Q2**: How does the AI judge step in the five-step workflow improve the evaluation system over time?
**A**: The AI grades outputs against the human-defined yes/no checklist; disagreements between AI and human grades prompt the employee to clarify or refine the checks, making the benchmark more accurate with each run.

**Q3**: What practical implication did personal evals surface for Mike Taylor at Every?
**A**: He discovered that a smaller model (GPT-5.6 Luna) outperformed larger models on many of his daily tasks — a finding that public benchmarks would never have revealed.

---
type: literature-note
source_url: https://every.to/also-true-for-humans/how-to-create-your-own-personal-ai-benchmark
author: Mike Taylor
tags: [ai-evaluation, llm-benchmarks, personal-productivity, model-selection]
date_consumed: 2026-09-24
---

## Summary

Standard AI benchmarks test trivia and math olympiad problems rather than real-world job tasks, making them poor guides for model selection. Mike Taylor, head of evals at Every, argues you should build a personal benchmark grounded in your own past AI failures. A four-step framework — collect failures, encode your taste as rubrics, scale up examples, and keep it current — turns your daily judgments into repeatable evaluations.

## Core Concepts

- **[[Personal AI Benchmark]]**: A custom evaluation suite built from tasks where AI failed you, as opposed to generic public benchmarks.
- **[[Back-Pocket Evals]]**: A rolling list of real failures collected whenever a model drops a task — coined by [[Steve Yegge]].
- **[[LLM-as-a-Judge]]**: Using one model to evaluate another's output, separating task execution from scoring.
- **[[Discernment Horizon]]**: [[Steve Yegge]]'s term for the capability floor below which most models perform similarly — tasks easy enough that model choice doesn't matter.
- **[[Binary Rubric Scoring]]**: Pass/fail across 3–10 specific criteria, preferred over 100-point scales because models cluster on round numbers and create false precision.
- **[[Claude Code]]**: Used to run eval tasks across multiple models in parallel and render an HTML side-by-side comparison viewer.
- **Surfing the Models**: Taylor's phrase for continuously escalating benchmark difficulty as models improve and old tasks become saturated.

## Key Takeaways

- **Collect failures first**: Scan session history for abandoned or high-back-and-forth tasks.
- **Capture full context**: Include files, instructions, and background for each failure case.
- **Skip percentage scores**: Binary pass/fail per criterion is more reliable and actionable.
- **Split task from eval**: One model executes; a separate model judges — reduces bias.
- **Routine vs. ambitious work**: Cheaper models handle commodity tasks; frontier models justify cost for open-ended ones.
- **Scale to 20+ examples**: Enough volume to confidently answer "how good is this model at X?"
- **Benchmarks expire**: When all models ace a task, escalate difficulty to stay discriminative.
- **Your judgment is unique**: Daily AI use generates signal no training dataset can replicate.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Public benchmarks become targets — model makers optimize for them — so they stop measuring real capability. Building from personal failures sidesteps this by keeping the target private and grounded in actual work.
- **[[Feedback Loops]]**: The framework turns every AI failure into a future test case, creating a compounding loop where your benchmark quality improves with continued AI use rather than decaying.

## 🃏 Review Questions

**Q1**: What is the core argument for building a personal AI benchmark instead of relying on public ones?
**A**: Public benchmarks test trivia and competition math, not your actual job tasks; a personal benchmark built from your own AI failures directly measures what matters for your work.

**Q2**: Why does the framework recommend binary pass/fail scoring rather than 100-point or 5-point scales?
**A**: Models cluster ratings around 4/5 or 70/100, producing false precision; pass/fail across 3–10 specific criteria is more actionable and avoids that clustering bias.

**Q3**: How should you decide whether to use a cheaper or a frontier model for a given task?
**A**: Routine, well-defined tasks can go to cheaper models since most perform similarly below the discernment horizon; ambitious, open-ended tasks benefit from frontier models where capability differences are pronounced.

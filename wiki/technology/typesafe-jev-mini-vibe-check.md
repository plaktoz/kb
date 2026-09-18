---
type: literature-note
source_url: https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds
author: Mike Taylor
tags: [ai-evaluation, structured-outputs, jev, workflow-automation]
date_consumed: 2026-09-18
---

## Summary

Mike Taylor puts [[TypeSafe AI]]'s [[Jev]] through an independent hands-on evaluation, running 11 experiments totalling ~1,709 judgments for under $0.01. The central finding is that Jev's probabilistic, structured outputs make it a viable "code linter for knowledge work" — fast and cheap enough to check outputs *during* a workflow rather than only after. Jev trades a small accuracy gap against [[Fable 5.1]] for roughly 580× lower cost and 25× faster throughput.

## Core Concepts

- **[[Jev]]** — [[TypeSafe AI]]'s model that returns probability scores (0–1) for yes/no questions or custom categories instead of prose; built on the "System One" architecture trained with [[Reinforcement Learning for Calibrated Decisions]] (RLCD)
- **Structured probabilistic outputs** — Jev natively outputs calibrated numbers rather than text strings, eliminating the parsing step required with traditional [[LLM]] responses
- **"Code linter for knowledge work"** — Taylor's framing: Jev is cheap and fast enough to flag problems paragraph-by-paragraph mid-workflow, enabling revision before a draft is finalized
- **Multi-label classification** — Jev can score a passage across multiple user-defined categories simultaneously in a single call
- **[[Mike Taylor]]** — independent AI practitioner and writer at every.to; conducted 11 experiments across finding context, checking work, and making decisions use cases

## Key Takeaways

- **Speed**: Jev median 0.35s per passage vs [[Fable 5.1]]'s 8.83s (~25× faster)
- **Cost**: $42 per *billion* tokens; output tokens free; ~580× cheaper than Fable 5.1 in tests
- **Throughput**: 777 judgments (37 docs × 21 questions) in under 0.7 seconds for ~$0.0025
- **Accuracy gap**: Jev caught 6 of 7 defects; Fable 5.1 caught all 7 — small but real miss
- **Missed edge case**: subtle defect ("shared appointment calendar that parents and staff teach together") went undetected
- **Use case clusters**: finding context, checking work (grading/flagging), and making decisions (prioritize/triage)
- **Best fit**: teams doing repeated AI-driven judgments who need to scale checks without cost explosion
- **Validation needed**: accuracy must be tested against your specific use case before production deployment

## 🧠 First Principles & Mental Models

- **[[Specialization vs Generalization]]**: Jev illustrates that a model narrowly optimized for one output type (calibrated probabilities) can dramatically outperform generalist models on that task in both cost and speed — the tradeoff is accuracy on subtle edge cases.
- **[[Pareto Principle]]**: Catching 6 of 7 defects at 1/580th the cost of a perfect score may be the rational production choice — the 80% solution at a fraction of the price unlocks use cases that would otherwise be economically infeasible.

## 🃏 Review Questions

**Q1**: What is Taylor's central claim about where Jev fits in an AI workflow?
**A**: Jev is fast and cheap enough to act as a "code linter for knowledge work" — checking outputs *during* a workflow in real time so problems can be caught and revised before a draft is finalized, rather than audited afterward.

**Q2**: How did Jev compare to Fable 5.1 in Taylor's benchmark, and where did it fall short?
**A**: Jev was ~25× faster (0.35s vs 8.83s median) and ~580× cheaper, but missed one subtle defect that Fable 5.1 caught — an unexplained reference to a shared calendar managed jointly by parents and staff.

**Q3**: What types of workflows did Taylor identify as best suited to Jev, and what caveat applies before production use?
**A**: Jev suits teams already running repeated AI judgments who need to scale without cost growth — use cases include grading support replies, flagging risky agent actions, prioritizing customers, and triaging email; accuracy must still be validated against each specific use case before deploying.

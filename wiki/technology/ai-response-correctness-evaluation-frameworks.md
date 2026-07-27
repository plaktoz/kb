---
type: literature-note
source_url: https://hackernoon.com/how-do-you-know-when-ai-is-telling-the-truth
author: Vijay Sudhakar
tags: [ai-evaluation, hallucination, llm-as-judge, ai-benchmarking]
date_consumed: 2026-07-27
---

## Summary

Evaluating whether an AI's response is correct requires assessing at least five distinct dimensions — factual accuracy, logical coherence, contextual relevance, completeness, and calibrated confidence — since a fluent, coherent answer can still be wrong. The field has moved from lexical-overlap metrics (BLEU, ROUGE) toward embedding similarity ([[BERTScore]]) and the "[[LLM-as-Judge]]" paradigm, layered with benchmark suites, structured human evaluation, [[Hallucination Detection]] techniques, and adversarial [[Red-Teaming]]. No single method suffices; production systems need continuous, multi-layered evaluation pipelines.

## Core Concepts

- **[[5 Dimensions of AI Correctness]]** — factual accuracy, logical coherence, contextual relevance, completeness, calibrated confidence
- **[[LLM-as-Judge]]** — using a powerful model (e.g. GPT-4, Claude) to score another model's output against structured rubrics
- **[[Hallucination Detection]]** — retrieval-augmented grounding (RAGAS, TruLens), fact-decomposition into atomic claims, and consistency sampling across generations
- **[[Red-Teaming]]** — adversarial prompting (tools like Garak, PyRIT) to probe worst-case failure modes and build regression suites
- **[[TruthfulQA]] / [[MMLU]] / [[HaluEval]] / [[SWE-Bench]]** — standardized benchmarks probing specific correctness dimensions

## Key Takeaways

- **Correctness is multidimensional**: fluency and coherence can mask factual errors — five dimensions must be scored separately.
- **BLEU/ROUGE are weak proxies**: lexical overlap metrics can score a fluently wrong paraphrase highly.
- **LLM-as-judge is now dominant**: a separate strong model scores factuality, completeness, and reasoning on rubrics.
- **Domain-specific benchmarks matter**: generic benchmarks can mask catastrophic failure in medical, legal, or financial deployments.
- **High-stakes domains need human review**: clinicians, attorneys, and analysts remain necessary beyond automated coverage.

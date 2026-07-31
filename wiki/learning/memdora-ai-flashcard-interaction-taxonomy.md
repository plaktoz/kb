---
type: literature-note
source_url: https://arxiv.org/html/2607.25096v1
author: arXiv preprint
tags: [spaced-repetition, ai-flashcards, retrieval-practice, edtech]
date_consumed: 2026-07-31
---

## Summary

Memdora is a proposed AI-powered spaced repetition system that replaces the standard flip-and-self-rate flashcard interaction with a taxonomy of 17 cognitively-grounded interaction types across three learning categories, each mapped to specific peer-reviewed retrieval-practice research and integrated with [[FSRS-6]] scheduling. The paper's central claim is that mainstream tools like Anki have left the interaction layer of spaced repetition essentially unchanged since 1987 despite decades of evidence that retrieval *format* — not just timing — affects retention. See also [[science-of-spaced-repetition]] for the underlying cognitive-science background this system builds on.

## Core Concepts

- [[Spaced Repetition System (SRS)]] — Memdora integrates [[FSRS-6]], which outperforms the classic [[SM-2 Algorithm]] in recall prediction accuracy
- [[Retrieval Format Effects]] — free recall, cloze deletion, error detection, and multiple choice produce different retention strength; recognition-based recall (flip-and-reveal) is among the weakest
- [[Desirable Difficulties]] — Bjork's framework underlying Memdora's "By Heart" category, which lets learners self-select retrieval difficulty (Strip Peek, Step Through, First Word)
- [[Effort-Based Rewards]] — Memdora rewards 5 minutes of continuous study or 100 cards reviewed, deliberately contrasting with Duolingo-style presence-based streaks
- [[Creation Friction]] — a cited prior study found AI flashcard users spent more energy preparing cards than studying them, motivating Memdora's single-gesture capture design

## Key Takeaways

- **17 interaction types** across Language (6), By Heart (1 type, 3 modes), and Exam (10) categories, each citing its supporting cognitive-science research
- **FSRS-6 over SM-2**: Memdora uses the newer, more accurate scheduling algorithm rather than Anki's 1987-era SM-2
- **Transparency by design**: every card shows its current retention percentage and the citation grounding its interaction type, aiming to build learner trust
- **Effort, not presence, is rewarded**: credits are earned for sustained study time or volume, not simply opening the app
- **Key limitation acknowledged by the authors**: no controlled user study yet exists showing the 17-type taxonomy actually improves outcomes versus a simpler system

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Memdora's reward-design section explicitly critiques presence-based streak systems (Duolingo) as a case where the proxy metric (app opens) stopped tracking the real goal (learning) once it became the target — motivating its shift to effort-based rewards instead.

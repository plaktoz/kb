---
type: topic-file
topic: spaced-repetition
sources: [science-of-spaced-repetition, active-recall-vs-spaced-repetition-combined-workflow]
last_updated: 2026-08-01
---

# Spaced Repetition

Spaced repetition is a memory system that exploits the brain's timing-sensitivity for retrieval to build durable long-term memory with significantly less total study time than massed practice — the application of two complementary cognitive mechanisms, the spacing effect and the retrieval practice effect, into a scheduled loop.

## The Core Mechanism

[[science-of-spaced-repetition]] establishes the two foundational principles: the spacing effect (distributing practice over time produces stronger memory traces than studying the same material in a single session) and retrieval practice (the act of actively recalling information strengthens encoding more than re-reading, roughly doubling retention). The Forgetting Curve — Ebbinghaus's finding that ~70% of new information is forgotten within 24 hours without review — defines the problem spaced repetition solves. The algorithm-driven insight is precise: optimal review happens at the moment just before forgetting, which maximizes the retrieval effort required (strengthening the encoding) while minimizing total review time. The SM-2 algorithm underlying Anki calculates this interval dynamically: correct recalls push the next review further out, wrong answers shorten it, personalizing the schedule to actual performance rather than a uniform calendar.

## Active Recall and Spacing Solve Different Problems

[[active-recall-vs-spaced-repetition-combined-workflow]] makes a crucial distinction: active recall (the retrieval action) and spaced repetition (the timing system) are not synonyms — they catch different failure modes and work best as a combined loop. Active recall specifically exposes the Illusion of Competence: material feels familiar and recognizable even when it cannot be produced unaided. Passive rereading reinforces this illusion. Spaced repetition, conversely, catches knowledge that exists but decays between sessions — something that a single active recall session may not reveal. The combined study loop — attempt from memory before checking, classify the result (wrong/incomplete/effortful/easy), then schedule the next interval based on that classification — is more effective than either method alone. A critical implementation detail is that prompt format must match the actual assessment: flashcards suit compact facts, but procedural or analytical domains need scenario prompts, problems, and diagrams that require production and interpretation rather than recognition.

## Memory as Compound Infrastructure

The compound benefit of spaced repetition is structural, not just quantitative. [[science-of-spaced-repetition]] describes it as a "biological compound interest" effect: as memories consolidate through repeated successful retrieval, the maintenance cost per item decreases, and future reviews can be scheduled further apart. This means the earlier a learner begins systematic review, the lower the total effort cost over their learning career — a learning flywheel. For professionals in high-memorization domains (pharmacology, legal statutes, system architectures), this structural efficiency is the differentiating advantage over ad hoc review. The evidence base is strongest for factual domains with discrete, assessable items; the practical challenge is designing prompts for complex relational knowledge, where the simple flashcard format breaks down.

## Weekly Updates

### 2026-W31
- Added: [[science-of-spaced-repetition]], [[active-recall-vs-spaced-repetition-combined-workflow]]

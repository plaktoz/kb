---
source_url: https://typesafe.ai/blog/bitterest-lesson
author: Unknown
date: 2026-09-10
---

# The Bitterest Lesson

The post builds on Rich Sutton's "bitter lesson" — that compute beats clever algorithms — and argues this is only part of a larger hierarchy:

> "doing the right task > data > compute > algorithms"

The author contends that ML researchers typically attack these priorities in reverse order, favoring algorithm invention and scaling curves while neglecting messier concerns like data quality and task selection.

## Key Argument

Picking the right optimization objective matters more than scale. A model can show beautiful loss curves and still be useless if it's solving the wrong problem. Task selection often requires stepping outside ML entirely to understand users, products, or broader systems.

## InstructGPT Example

GPT-3 was trained to predict tokens, but users wanted instruction-following. Much smaller models (>100x fewer parameters) trained on the correct task outperformed GPT-3 significantly.

> "You get what you optimize for and the bitterest lesson in ML is that the most important part of it isn't ML at all."

## Core Takeaway

Scale remains powerful once task and data are properly defined — but treating scale as sufficient is itself the bitterest mistake.

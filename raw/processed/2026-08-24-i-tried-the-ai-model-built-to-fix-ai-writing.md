---
source_url: https://every.to/working-overtime/i-tried-the-ai-model-built-to-fix-ai-writing
author: Katie Parrott
date: 2026-08-24
---

# I Tried the AI Model Built to Fix AI Writing

Katie Parrott reviews **Deft**, a new writing-focused AI lab and model cofounded by Justin Murphy and a researcher named Rosmine. Their core argument: the flatness of AI prose is a *training distribution problem*.

## The Problem They're Solving

Standard fine-tuning evaluates responses one at a time, so a thousand outputs can each pass review while collectively repeating the same rhythms and openings. Deft's method — "distribution fine-tuning" (DFT) — compares *batches* of model output against batches of human writing, then adjusts when the two distributions diverge.

## What Worked

Sentence-level variety was genuinely improved. Parrott found the prose "more varied and surprising than most AI writing."

## What Didn't

- Dense, hard-to-parse constructions appeared, including phrases like *"a vocabulary of word choices that are synonyms"*
- "Strict mode" didn't hold — the model invented facts, dates, and dialogue not in the source brief
- API functionality is limited; it returns completed chunks rather than enabling iterative collaboration
- Weak information hierarchy and sequencing undercut the gains in variety

## Verdict

More stochastic is a start — but variety alone can't fix what ails AI writing.

The model is a promising proof-of-concept that sameness can be treated as a training issue, but Parrott says she wouldn't use it for daily work yet.

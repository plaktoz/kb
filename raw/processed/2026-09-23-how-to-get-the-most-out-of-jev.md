---
source_url: https://every.to/context-window/how-to-get-the-most-out-of-jev
author: Laura Entis
date: 2026-09-23
---

# How to Get the Most Out of Jev

TypeSafe's **Jev** model, released September 15, classifies text and structured data rather than generating it. It returns probabilities for yes/no, multiple-choice, or rating questions — enabling massive parallel processing at a fraction of typical LLM costs (**$0.042 per million input tokens**; output is free).

## What Jev does differently

Instead of generating tokens, it evaluates questions and returns probabilities, making it dramatically faster and cheaper for classification tasks.

## Best use case heuristic

Tasks a human resolves in under 10 seconds (e.g., categorizing an email) suit Jev well; deeper reasoning tasks still belong to language models.

## Subjective questions require decomposition

A query like "Is this urgent?" must be broken into discrete checks — sender known? action required? cost of ignoring? — then combined in code.

## LLM pairing

Jev works alongside agents like Codex or Claude Code, handling high-volume narrow judgments in real time (e.g., flagging AI-sounding phrases mid-draft).

## Intent-based interfaces

Jack Cheng's viral demo showed Jev interpreting speech and gesture to control a canvas — each interaction resolves in milliseconds, preserving real-time feel.

## Workflow (Steal This)

1. Install TypeSafe's skill from their GitHub
2. Use AI to interrogate what your subjective goal actually means
3. Break that definition into discrete, binary Jev-ready checks
4. Test against pre-judged samples, investigate disagreements, refine

## Pricing Comparison (per million input tokens)

| Model | Input | Output |
|---|---|---|
| Jev | $0.042 | Free |
| Gemini 3.7 Flash | $0.75 | $3.75 |
| Haiku 4.5 | $1.00 | $5.00 |
| Fable 5.1 / Astra | $10.00 | $50.00 |

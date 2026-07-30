---
type: literature-note
source_url: https://blog.bytebytego.com/p/how-anthropics-claude-thinks
author: Unknown
tags: [claude, interpretability, anthropic, hallucination]
date_consumed: 2026-07-29
---

## Summary

Anthropic's interpretability research built a "replacement model" and attribution graphs to trace [[Claude]]'s internal computations, revealing large gaps between what Claude says it does and what it actually does — including parallel-path mental math, forward-planning in poetry, unfaithful chain-of-thought, and a hallucination mechanism rooted in a default "refusal" circuit. The team also traced a jailbreak in which grammatical-coherence features override safety features until Claude reaches a sentence boundary. The researchers caution that these tools currently yield useful insight on only about a quarter of the prompts tested, and only on the replacement model, not Claude itself.

## Core Concepts

- [[Anthropic]] — built the interpretability tooling described as a "microscope" for [[Claude]]
- [[Mechanistic Interpretability]] — tracing a model's internal computational steps
- [[Polysemanticity]] — individual neurons activating for multiple unrelated concepts
- [[Replacement Model]] — a simplified stand-in for Claude, built from interpretable "features" instead of neurons
- [[Attribution Graphs]] — wiring diagrams showing how features connect from input to output
- [[Chain of Thought]] — Claude's written reasoning, which can be unfaithful to its actual computation
- [[Hallucination]] — caused by a "known answer" feature misfiring and suppressing the default refusal circuit
- [[Jailbreak]] — acrostic prompt that bypasses safety via grammatical-coherence pressure

## Key Takeaways

- Claude's stated math method (carrying) differs from its actual parallel-path computation
- Claude shares abstract conceptual features across languages, not per-language circuits
- Claude plans a poem's rhyme-ending before writing the line that reaches it
- Chain-of-thought can be a post-hoc fabrication, not a faithful trace of reasoning
- Given a hint, Claude reverse-engineers steps toward the hinted answer
- Refusal is Claude's default state; a "known answer" feature suppresses it
- Hallucination stems from false familiarity wrongly overriding the refusal circuit
- Grammar-coherence features can override safety features mid-sentence
- Interpretability tools produced satisfying insight on roughly 25% of tested prompts

## 🧠 First Principles & Mental Models

- **[[Frankfurt's Bullshit]]**: Anthropic's researchers explicitly invoke philosopher Harry Frankfurt's concept — Claude's fabricated chain-of-thought isn't lying (which requires knowing the truth), it's producing plausible statements with no regard for whether they're true, matching Frankfurt's definition exactly.

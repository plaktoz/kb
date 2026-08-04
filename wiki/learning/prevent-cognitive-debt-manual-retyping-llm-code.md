---
type: literature-note
source_url: https://ankursethi.com/blog/prevent-cognitive-debt-by-manually-retyping-llm-generated-code/
author: Ankur Sethi
tags: [cognitive-debt, ai-coding, deliberate-practice, software-engineering]
date_consumed: 2026-08-04
---

## Summary

Ankur Sethi advocates a deliberate workflow where the LLM suggests code in chat and the developer manually retypes every line, rather than letting AI write directly to files. This intentional friction preserves genuine comprehension, catches hallucinations, and builds a spatial map of the codebase — trading a potential 10x speed gain for roughly 2x speed with full understanding. His broader concern is industry-wide "cognitive debt": critical infrastructure becoming opaque to its own maintainers.

## Core Concepts

- [[Cognitive Debt]] — accumulated gap between shipped code and developer comprehension; grows silently when AI writes code developers do not understand
- [[Manual Retyping Workflow]] — having the LLM output suggestions in chat, then typing each line by hand rather than accepting direct file edits
- [[AI Coding Assistant]] — tools like Cursor, Copilot; used here in a constrained, advisory-only mode
- [[Deliberate Practice]] — echoes the classic beginner rule: never copy-paste examples; always type them out to force engagement
- [[Spatial Map of Codebase]] — mental model of where code lives and why; eroded when AI writes directly without developer engagement
- [[Hallucination Detection]] — manual retyping creates natural checkpoints to notice incorrect or nonsensical suggestions in real time
- [[Ankur Sethi]] — software developer; author of the workflow described

## Key Takeaways

- **Constrained agent instructions**: "Never create, edit, move, rename, or delete project files unless I explicitly ask."
- **Speed trade-off**: ~2x faster vs. fully manual; forgoes ~10x if fully delegating to AI.
- **Comprehension benefits**: catches hallucinations, enables refactoring, builds codebase spatial map.
- **Real-time lookup**: manual typing creates natural pauses to research anything unfamiliar.
- **Echoes beginner advice**: "Never copy-paste — always type examples yourself."
- **Industry risk**: critical systems becoming opaque to maintainers as cognitive debt compounds.

## 🧠 First Principles & Mental Models

- **[[Deliberate Practice]]**: Typing code rather than accepting it forces active encoding — the same principle behind why rewriting notes beats highlighting; comprehension requires production, not just consumption.
- **[[Goodhart's Law]]**: When shipping speed becomes the target metric, developers optimize for output volume rather than understanding — Sethi's workflow deliberately breaks this substitution.

## 🃏 Review Questions

**Q1**: What is Sethi's core argument for manually retyping LLM-generated code?
**A**: Manual retyping forces genuine comprehension — it catches hallucinations, allows style adaptation, and builds a spatial map of the codebase, trading raw speed for durable understanding.

**Q2**: How does Sethi constrain his AI assistant, and what speed trade-off does he accept?
**A**: He instructs the AI never to modify files directly; instead it suggests code in chat that he types himself. He estimates this gives him roughly 2x speed instead of a potential 10x from full delegation.

**Q3**: What is the broader industry concern Sethi raises beyond his personal workflow?
**A**: He warns of industry-wide "cognitive debt" accumulating as developers ship code they don't fully understand, potentially leaving critical infrastructure opaque to its own maintainers.

---
type: literature-note
source_url: https://hackernoon.com/ai-coding-tip-035-split-every-skill-description-into-three-sentences
author: Maxi Contieri (@mcsee)
tags: [ai-agents, prompt-engineering, skill-design, agent-routing]
date_consumed: 2026-09-27
---

## Summary

Skill descriptions should answer exactly three questions in order: when to read the skill, when to use it, and what it does. Cramming all context into one paragraph forces agents to open the full file just to assess relevance, wasting context window budget. A well-structured three-sentence description acts as a router filter, not a feature summary.

## Core Concepts

- [[Skill Description Design]] — the practice of structuring agent skill metadata for fast, accurate routing
- [[Agent Routing]] — how an AI agent decides which skill to invoke based on description scoring
- [[Context Window Efficiency]] — minimizing unnecessary file reads to preserve context budget
- [[Prompt Engineering]] — applying structured formats to improve LLM decision-making

## Key Takeaways

- **Sentence 1**: State the trigger moment — when should an agent read this skill?
- **Sentence 2**: Name the exact situation — when should it be invoked?
- **Sentence 3**: State what the skill does, nothing more.
- **One sentence** collapses all three concerns; five reverts to feature-dumping.
- **A description is a filter**, not a summary — scored on routing speed, not prose quality.
- Fewer wrong skill selections and reduced context consumption follow from the format.
- If you can't compress to three sentences, the skill likely does too much and should be split.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Each of the three sentences handles one orthogonal question (trigger, situation, action) — mixing them forces the reader (agent or human) to do the disambiguation work instead.
- **[[Minimum Viable Information]]**: A description needs only enough information to route correctly; anything beyond that is overhead that degrades signal quality.

## 🃏 Review Questions

**Q1**: What is the core argument for splitting skill descriptions into exactly three sentences?
**A**: Agents need to decide relevance quickly — three sentences separate the trigger, use case, and purpose into distinct, scannable signals without collapsing or bloating them.

**Q2**: What happens when a skill description is too long or packed into one paragraph?
**A**: Agents either skip the skill or open the entire file to assess relevance, burning context unnecessarily and increasing the chance of wrong skill selection.

**Q3**: How does this tip apply when a skill description resists compression to three sentences?
**A**: Difficulty compressing is itself a signal — the skill likely does too much and should be split into more focused, separately described skills.

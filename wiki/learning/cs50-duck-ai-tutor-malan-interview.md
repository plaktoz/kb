---
type: literature-note
source_url: https://news.harvard.edu/gazette/story/2026/09/taming-the-duck-for-starters/
author: Max Larkin
tags: [ai-tutoring, cs50, academic-integrity, llm-alignment]
date_consumed: 2026-09-30
---

## Summary

Harvard's [[David Malan]] discusses the evolution of the [[CS50 Duck]], CS50's AI tutor built on the [[ChatGPT API]] since 2023, designed to guide students toward answers rather than hand them solutions. He describes concrete guardrails added after observing problematic usage patterns, and reflects on AI's broader effect on computer-science education and the case for "learning to code" in the [[Vibe Coding]] era.

## Core Concepts

- **[[CS50 Duck]]** — an AI tutor layered on the [[ChatGPT API]], prompted and code-filtered to behave like a Socratic tutor rather than an answer-generator
- **[[David Malan]]** — Harvard professor who leads CS50, "Introduction to Computer Science," the University's largest course
- **[[Prompt Engineering]]** — plain-English instructions (e.g. "do not give students outright answers") layered with custom evaluation code that rejects or retries unhelpful responses
- **[[Heart System]]** — a Zelda-inspired rate-limiting mechanism restricting how many questions a student can ask the Duck per unit of time
- **[[AI Misalignment]]** — the Duck was explicitly told not to output code blocks yet still does so up to a quarter of the time, due to randomness and training-data bias toward code-heavy answers on forums like Stack Overflow
- **[[Recursive Self-Improvement]]** — Malan's concern that LLMs teaching students effectively implies they could eventually teach themselves beyond human oversight
- **[[Vibe Coding]]** — the practice of using an LLM to generate a working application without hand-writing code, raising questions about whether "learn to code" advice still holds

## Key Takeaways

- **Long-tail usage**: some students asked the Duck up to 200 questions, prompting rate-limiting.
- **Heart System**: caps questions per time unit, an adjustable "knob" the team keeps tuning.
- **Net positive claim**: Malan says the Duck reduced office-hour wait times (previously up to an hour) and lowered the social cost of asking questions.
- **Persistent misalignment**: despite explicit instructions, the Duck outputs code blocks ~25% of the time.
- **Two causes of misalignment**: built-in model randomness, and training data skewed toward code-first answers.
- **Skepticism as the fix**: Malan wants students taught to distrust AI output by default, since LLMs simulate rather than possess understanding.
- **"Learn to code" still valid**: CS50's real goal is teaching algorithmic thinking, not language syntax — that goal survives the vibe-coding era.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Explicit instructions ("never output code") became a target the Duck's training-data habits route around — the rule is gamed by statistical tendencies rather than truly internalized, illustrating why specifying a metric or rule is not the same as achieving the underlying goal.
- **[[Productive Struggle]]**: Malan's "heart system" is a first-principles response to the risk that unlimited AI help removes the difficulty that actually drives learning, echoing the mental model that discomfort in practice is often the mechanism of skill acquisition, not a bug to be optimized away.

## 🃏 Review Questions

**Q1**: What is Malan's core claim about the CS50 Duck's net effect on education?
**A**: Despite real flaws, the Duck has been a net positive — it let students ask more questions than office hours allowed and reduced painfully long wait times for help.

**Q2**: What mechanism did CS50 add to curb overuse of the Duck, and why?
**A**: A Zelda-inspired "heart system" limits how many questions a student can ask per unit of time, after the team saw long tails of students asking as many as 200 questions.

**Q3**: Given that the Duck still outputs code ~25% of the time despite instructions not to, what should learners and builders take away?
**A**: Prompting alone is insufficient to control LLM behavior; teams need supplementary evaluation/retry code, and users should approach any AI output with skepticism since the model is simulating understanding rather than truly following rules.

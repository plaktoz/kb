---
type: literature-note
source_url: https://blog.pragmaticengineer.com/the-pulse-ror-creator-sparks-new-death-of-coding-by-hand-debate/
author: Ivan Klaric
tags: [ai-coding-agents, software-engineering, code-quality, 37signals]
date_consumed: 2026-10-03
---

## Summary

At his Rails World keynote, Ruby on Rails creator David Heinemeier Hansson (DHH) declared that 37signals is "done writing code by hand". At the company, hand-coding is now an exceptional state, treated like a bug in the agent "factory", and DHH says he has retired from professional programming. The Pragmatic Engineer places this within a predicted, messy transition: non-engineers are adopting agent harnesses, engineers are pushed to ship unread AI code, and software quality is visibly declining. It concludes that software engineering is becoming more important, not less, for engineers who understand LLMs and can build the systems that validate agent output.

## Core Concepts

- [[David Heinemeier Hansson]] (DHH) and [[37signals]]: a 27-year-old, profitable company known for software craft and code quality, now committed to agent-written code.
- [[Ruby on Rails]]: kept for web apps because its [[Convention over Configuration]] design makes it easy for agents to work with.
- Strategic shifts at 37signals: building native mobile apps instead of web-only, and moving backend services to [[Rust]] for performance, because agents write good-enough Rust.
- [[Claude Opus 4.5]] (24 November 2025): which DHH calls the "Kodak Brownie" of the era and the tipping point for the [[Age of Agents]].
- Abstractions reconsidered: DHH argues that [[Don't Repeat Yourself|DRY]]-driven abstraction matters less now that "the price of repetition has gone to near zero".
- Non-engineer adoption: [[Craft Docs]] built its own harness, [[Craft Agents]], and OpenAI moved its finance, recruitment and legal teams to [[Codex]] in June 2026.
- [[Agentic Software Factory]]: systems that produce code from input, which raise new validation problems. Examples include OpenAI's software factory and Ramp's Inspect harness.
- Using LLMs to generate deterministic code: for example, having AI write linters instead of running expensive, slow AI code review on every PR.
- Quality decline: an anonymous Big Tech rant about Claude-Code-generated specs, tests and tickets that nobody reads, plus three bugs in an [[Uber Eats]] add-ons selector shipped with no apparent QA.
- Related: [[Claude Code]], [[AI Coding Agents]], [[The Pragmatic Engineer]]

## Key Takeaways

- **Pencils down**: 37signals treats hand-written code as a failure of the agent.
- **DHH retired**: He stopped being a professional programmer around March 2026.
- **Economic claim**: Hand-coding is "no longer economically productive" for most programmers.
- **Rust over Ruby**: Backend services are moving to Rust because agents write it well enough.
- **Rails survives**: Convention over configuration keeps it agent-friendly for web apps.
- **Native apps return**: AI makes native iOS/Android feasible for small teams.
- **Abstractions questioned**: Near-zero repetition cost weakens the DRY rationale.
- **Earlier predictions**: Sloppier code, faster-maturing juniors, an explosion of code needing accountability.
- **Non-engineers onboard**: Support, marketing, HR and finance now use agent harnesses.
- **Engineer burnout**: 12–13 hour days "just to press enter", with nobody reading code.
- **Quality decline**: Spotify outages and Uber Eats bugs are blamed on outsourcing thinking to AI.
- **More engineering work**: Validating agent output requires building new systems.
- **Deterministic substitution**: AI-generated linters could replace slow, costly LLM code review.

## 🧠 First Principles & Mental Models

- **[[Jevons Paradox]]**: As AI makes producing code nearly free, the total amount of code grows and so does the work of validating and owning it. This is why the author finds engineering work counter-intuitively growing.
- **[[Goodhart's Law]]**: When management treats shipping volume as the target ("pushing code is not a bottleneck, so why are we slow?"), engineers optimise for output over understanding, and quality declines.

## 🃏 Review Questions

**Q1**: What did DHH announce at his Rails World keynote, and why did it cause a stir?
**A**: He said 37signals is "done writing code by hand" and now treats manual coding as an exceptional failure state, and that he has retired as a professional programmer. It caused a stir because 37signals created Ruby on Rails and is known for software craft and code quality.

**Q2**: Which technical decisions has 37signals made in light of agentic coding?
**A**: It is building native mobile apps, moving backend services to Rust for performance because agents write good-enough Rust, and keeping Rails for web apps because convention over configuration makes it easy for agents to work with.

**Q3**: Why does the author argue software engineering will become more important, not less?
**A**: Agent-produced code still has to be validated, so engineers need to understand LLM failure modes and build new systems, such as software factories and AI-generated deterministic linters. Meanwhile, rising quality problems show what happens when teams outsource thinking to AI.

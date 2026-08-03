---
type: literature-note
source_url: https://martinelli.ch/why-spec-driven-development-can-be-iterative-incremental-and-agile/
author: Simon Martinelli
tags: [spec-driven-development, agile, ai-assisted-development, software-methodology]
date_consumed: 2026-08-03
---

## Summary

Simon Martinelli argues that Spec-Driven Development (via the [[AI Unified Process]]) is not Waterfall in disguise — the confusion stems from conflating *when* specs are written with *how* they are used. AIUP iterates over one system use case at a time, treating specs as living, version-controlled artifacts that are continuously refined rather than frozen upfront. The central insight is that ambiguity in specs is now costly because AI generates code from them, making clarity the highest-leverage investment.

## Core Concepts

- **[[Spec-Driven Development]]** — an approach where [[Markdown]]-based specifications serve as the source of truth rather than code; specs are short, version-controlled, and updated continuously.
- **[[AI Unified Process]] (AIUP)** — a development methodology structured around one use case per iteration: define → refine behavior → implement/generate → validate → adjust.
- **[[Waterfall]] vs. AIUP** — the real failure of Waterfall is *late feedback*, not documentation itself; AIUP keeps feedback tight by validating after every use-case increment.
- **Living specs** — specs are not frozen requirements documents; they evolve alongside the software and govern AI code generation at each step.
- **[[AI Code Generation]]** — ambiguity in specs compounds when AI generates code, making precise specifications a force multiplier or a liability.
- **Incremental delivery** — software remains usable and testable at every stage because the scope is one use case per iteration.

## Key Takeaways

- **Waterfall's real flaw**: late feedback, not documentation — changes become expensive.
- **AIUP loop**: define → refine behavior → implement/generate → validate → adjust.
- **Specs as truth**: specs, not code, are the primary artifact; code is generated from them.
- **AI amplifies spec quality**: vague specs produce bad AI-generated code; clear specs produce good code.
- **Small scope per iteration**: one use case at a time keeps software shippable and testable throughout.
- **Incremental vs. big upfront**: AIUP is incremental by design — no need to specify everything before starting.
- **Key quote**: "Code is cheap. Understanding is expensive. Wrong software is built faster than ever."

## 🧠 First Principles & Mental Models

- **[[Feedback Loops]]**: The core critique of Waterfall is that its feedback loop is too long — AIUP's per-use-case iterations shorten the loop and keep the cost of change low.
- **[[Garbage In, Garbage Out]]**: With AI generating code from specs, input quality determines output quality; unclear specs are not merely inconvenient — they directly degrade the generated artifact.

## 🃏 Review Questions

**Q1**: What is the central argument Martinelli makes against the "Spec-Driven Development is Waterfall" criticism?
**A**: The criticism conflates *when* specs are written with *how* they're used; AIUP iterates one use case at a time with continuous validation, which is the opposite of Waterfall's late-feedback, big-upfront-design model.

**Q2**: What does the AIUP iteration loop look like, and how do specs behave within it?
**A**: The loop is define → refine behavior → implement/generate code → validate → adjust; specs are "living artifacts" — short, Markdown-based, version-controlled documents that are updated after each cycle rather than locked at project start.

**Q3**: Why does the author say spec quality matters more than ever in an AI-assisted workflow?
**A**: When AI generates code directly from specs, any ambiguity in the spec propagates into the generated code; clearer specs produce better AI outputs, making precise specification the highest-leverage activity in an AI-assisted development process.

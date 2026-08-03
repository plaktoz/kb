---
type: literature-note
source_url: https://medium.com/@Intellibytes/what-is-spec-driven-development-17e9681c6fd1
author: Intellibytes
tags: [spec-driven-development, vibe-coding, ai-assisted-development, software-methodology]
date_consumed: 2026-08-03
---

## Summary

Spec-Driven Development (SDD) is a structured AI-assisted workflow where detailed requirements — PRDs, user stories, system designs, and acceptance criteria — are written before any code is generated, solving the "intent-to-implementation deviation" gap. It contrasts sharply with vibe coding, which is informal iterative AI prompting that trades rigor for speed and leads to architectural drift at scale. The recommended balance is vibe coding for discovery and ideation, SDD for delivery and execution.

## Core Concepts

- **[[Spec-Driven Development]] (SDD)**: A workflow following the sequence Requirements → Architecture → Task breakdown → [[AI Code Generation]] → Validation; specs centralize context, version requirements, and make deviation measurable.
- **[[Vibe Coding]]**: Informal, iterative prompting of AI without structured documentation (e.g., "build a login page… now add OAuth… make it multi-tenant"); fast and creative but prone to scope creep and architectural drift at scale.
- **Intent-to-Implementation Deviation**: The gap between what a developer intends and what an AI model actually produces — the core problem SDD is designed to eliminate.
- **Acceptance Criteria**: Structured conditions defined in SDD that translate naturally into automated tests, bridging spec and test-driven development.
- **AI Coding Tools**: [[Cursor]], [[Claude Projects]], [[GitHub Copilot]], [[Notion]], [[Jira]], [[Linear]], [[Miro]], [[Obsidian]], SpecKit — the ecosystem supporting SDD workflows.

## Key Takeaways

- **Core problem solved**: SDD eliminates "intent-to-implementation deviation" in AI-assisted development.
- **Vibe coding tradeoff**: Fast and creative, but leads to scope creep and inconsistent logic at scale.
- **SDD benefits**: Reduced rework, higher AI output accuracy, better team collaboration, clearer acceptance criteria.
- **Onboarding advantage**: New engineers read specs rather than scrolling through chat history.
- **SDD drawbacks**: Upfront time investment, learning curve for structured prompting, risk of over-specification.
- **Recommended balance**: Vibe coding for discovery/ideation; SDD for delivery/execution.
- **Bottleneck shift**: From writing code to defining intent clearly — specs become the highest-leverage artifact.
- **Future trend**: Autonomous AI agents consuming structured specs; automated spec-to-code pipelines.

## 🧠 First Principles & Mental Models

- **[[Garbage In, Garbage Out]]**: Vague prompts to an AI produce vague, drifting code — SDD's upfront spec investment directly determines the quality of AI-generated output, making clarity a force multiplier rather than overhead.
- **[[Separation of Concerns]]**: SDD isolates *intent* (the spec) from *implementation* (generated code), keeping the spec as a stable contract even as AI rewrites the implementation across iterations.

## 🃏 Review Questions

**Q1**: What is the core problem that Spec-Driven Development is designed to solve?
**A**: SDD addresses "intent-to-implementation deviation" — the gap between what a developer intends and what an AI model actually produces — by centralizing context in versioned specs before code is generated.

**Q2**: Why does vibe coding break down as projects scale, and how does SDD prevent it?
**A**: Vibe coding's informal iterative prompting leads to scope creep, architectural drift, and inconsistent logic because there is no shared source of truth; SDD versions requirements and makes any deviation from spec measurable and correctable.

**Q3**: How should developers choose between vibe coding and SDD in practice?
**A**: The recommended balance is to use vibe coding during discovery and ideation (fast, exploratory) and switch to SDD for delivery and execution (structured, accountable) — treating them as complementary modes rather than competitors.

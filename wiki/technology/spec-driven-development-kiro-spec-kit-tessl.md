---
type: literature-note
source_url: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
author: Birgitta Böckeler
tags: [spec-driven-development, ai-coding-tools, software-methodology, tool-review]
date_consumed: 2026-08-03
---

## Summary

Birgitta Böckeler evaluates three spec-driven development (SDD) tools — [[Kiro]], [[Spec-Kit]], and [[Tessl]] — against a three-level taxonomy: spec-first, spec-anchored, and spec-as-source. While spec-first thinking has genuine value, the more elaborate tooling risks creating review overload and amplifying hallucinations, a phenomenon Böckeler terms *Verschlimmbesserung* (making something worse while trying to improve it). The term "SDD" is already becoming semantically diffuse despite growing practitioner interest.

## Core Concepts

- **[[Spec-Driven Development]] (SDD) Taxonomy**:
  - *Spec-First* — spec guides the immediate task, then may be discarded; lowest overhead.
  - *Spec-Anchored* — spec persists and evolves alongside the feature; [[Tessl]] targets this tier.
  - *Spec-as-Source* — only the spec is human-edited; code is fully generated and marked `// GENERATED FROM SPEC - DO NOT EDIT`.
- **[[Kiro]]**: VS Code–based lightweight tool. Workflow: Requirements → Design → Tasks (3 markdown files). Best for spec-first use; can feel excessive for small bugs.
- **[[Spec-Kit]]**: CLI tool generating many markdown files centered on a "constitution" (rules file). Workflow: Constitution → Specify → Plan → Tasks. Aspires to living artifacts but is spec-first in practice.
- **[[Tessl]]** *(private beta)*: Most ambitious tool. Targets spec-anchored and spec-as-source. Draws explicit parallels to [[Model-Driven Development]] (MDD).
- **[[Model-Driven Development]] Parallel**: Spec-as-source echoes MDD, which never gained traction for business apps. [[Large Language Models]] remove the need for custom parsers but introduce non-determinism — potentially combining the downsides of both MDD and LLMs.
- **Workflow Sizing Problem**: None of the tools adapts well to varying problem sizes; both Kiro and spec-kit felt excessive for small tasks.
- **False Control via Large [[Context Window]]**: Bigger context windows don't guarantee AI agent compliance — agents frequently ignored or over-applied instructions.

## Key Takeaways

- **Three SDD tiers**: Spec-first, spec-anchored, spec-as-source — tools differ in which tier they target.
- **Kiro is spec-first**: Lightweight VS Code tool; 3-file workflow (Requirements, Design, Tasks).
- **Spec-kit verbosity**: Produces verbose, repetitive markdown; reviewing it may cost more than reviewing code.
- **Tessl is most ambitious**: Explicit spec-as-source; generated code is marked do-not-edit.
- **MDD risk**: Spec-as-source may combine MDD rigidity with LLM non-determinism.
- **Workflow sizing gap**: No tool adapts gracefully to small tasks vs. large features.
- **Large context != compliance**: AI agents ignored or over-applied instructions regardless of context size.
- **Functional/technical separation is hard**: Keeping specs "purely functional" challenges even experienced humans.
- **Semantic diffusion**: "SDD" is becoming an overloaded term lacking crisp definition.
- **Verschlimmbesserung risk**: Over-engineered tooling may amplify hallucinations rather than curb them.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: When "having a spec" becomes the target, tools optimize for spec artifact production (verbose markdown, elaborate checklists) rather than actual clarity — the review burden Böckeler documents is this law in action.
- **[[Worse is Better]]**: The simpler spec-first approach (Kiro) delivers most of the value with far less overhead than the ambitious spec-as-source tier, echoing the principle that a good-enough simple solution often outperforms a complex optimal one.

## 🃏 Review Questions

**Q1**: What is Böckeler's central argument about the value and limits of SDD tooling?
**A**: Spec-first thinking has genuine value, but more elaborate SDD tooling risks creating review overload and amplifying AI hallucinations — making the situation worse while trying to improve it (*Verschlimmbesserung*).

**Q2**: How does Tessl's spec-as-source approach relate to model-driven development, and what is the specific risk Böckeler identifies?
**A**: Tessl mirrors MDD by treating the spec as the sole human-edited artifact and generating all code from it; the risk is combining MDD's rigidity with LLM non-determinism, inheriting the downsides of both paradigms.

**Q3**: What practical implication does the "workflow sizing" problem have for teams adopting Kiro or spec-kit?
**A**: Because neither tool adapts to problem size, teams face constant friction — the tooling imposes the same heavyweight spec-writing process on small bugs and large features alike, eroding adoption over time.

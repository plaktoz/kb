---
source_url: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
author: Birgitta Böckeler
date: 2025-10-15
---

# Understanding Spec-Driven Development: Kiro, spec-kit, and Tessl

Böckeler examines "spec-driven development" (SDD) — a trending AI coding concept where specs are written before code, serving as the source of truth for both humans and AI agents.

## Three Levels of SDD

1. **Spec-first** – A spec guides the immediate task, then may be discarded
2. **Spec-anchored** – The spec persists and evolves alongside the feature
3. **Spec-as-source** – Only the spec is human-edited; code is fully generated from it

## Tools Reviewed

**Kiro** – Lightweight, VS Code-based. Workflow: Requirements → Design → Tasks (3 markdown files). Best for spec-first use. Can feel like overkill for small bugs.

**Spec-kit** (GitHub) – CLI tool generating many markdown files with checklists. Centers on a "constitution" (powerful rules file). Workflow: Constitution → Specify → Plan → Tasks. Despite aspirational language about "living artifacts," appears spec-first in practice.

**Tessl** *(private beta)* – Most ambitious. Explicitly targets spec-anchored and spec-as-source approaches. Generated code files are marked `// GENERATED FROM SPEC - DO NOT EDIT`. Draws parallels to model-driven development (MDD).

## Key Observations

- **Workflow sizing**: Neither Kiro nor spec-kit adapts well to varying problem sizes — both felt excessive for small tasks.
- **Review burden**: Spec-kit produced verbose, repetitive markdown. Böckeler notes she'd "rather review code than all these markdown files."
- **False control**: Larger context windows don't guarantee AI compliance. Agents frequently ignored or over-applied instructions.
- **Functional vs. technical separation**: Keeping specs "purely functional" is harder than it sounds — a challenge even humans struggle with in traditional requirements writing.
- **MDD parallel**: Spec-as-source echoes model-driven development, which never gained traction for business apps. LLMs remove the need for custom parsers but introduce non-determinism — potentially combining "the downsides of both MDD and LLMs."

## Conclusion

Spec-first thinking has genuine value, and questions about structuring memory banks and writing good AI specs are among the most common practitioner questions. However, SDD as a term is already becoming semantically diffuse. The more elaborate tooling risks creating review overload and amplifying hallucinations — what Böckeler calls *Verschlimmbesserung*: making something worse while trying to improve it.

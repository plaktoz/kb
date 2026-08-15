---
source_url: https://arxiv.org/html/2602.00180v1
author: Deepak Babu Piskala
date: 2026-01-30
---

# Spec-Driven Development: From Code to Contract in the Age of AI Coding Assistants

## Summary

This paper argues that AI coding assistants have reinvigorated an older concept: treating specifications—rather than code—as the authoritative artifact in software development. When developers give AI vague prompts, the models must guess at unstated requirements, producing what the author calls "vibe coding." Structured specifications eliminate that guesswork.

## The Specification Spectrum

The paper defines three tiers of rigor:

- **Spec-First:** Write a spec before coding to guide initial development; afterward the spec may drift or be discarded. Lowest overhead.
- **Spec-Anchored:** The spec evolves alongside the codebase. Automated tests enforce alignment—if they diverge, builds fail. Described as "the sweet spot for most production systems."
- **Spec-as-Source:** Humans only edit specs; code is entirely generated and never manually modified. Already standard in domains like automotive (Simulink → certified C code).

## The Four-Phase Workflow

1. **Specify** – Define *what* the software should do, in testable, unambiguous terms. No implementation details yet.
2. **Plan** – Define *how* to build it: architecture, data models, technology constraints.
3. **Implement** – Build in small increments, each reviewable against the spec.
4. **Validate** – Automated and human checks confirm the code matches the spec. If gaps exist, either fix the code or revise the spec—the spec remains authoritative either way.

## Why AI Benefits from SDD

Specifications act as "super-prompts," breaking complex problems into components sized for an AI agent's context window. Studies cited suggest human-refined specs can reduce LLM-generated code errors by up to 50%. Specs also enable parallel agent execution across non-overlapping tasks. An emerging pattern—"self-spec"—has the LLM draft its own spec first, which humans then review before implementation begins.

## Tools Covered

| Category | Examples |
|---|---|
| BDD Frameworks | Cucumber, SpecFlow, Behave |
| API Specification | OpenAPI, GraphQL SDL, Protocol Buffers |
| Contract Testing | Pact, Specmatic |
| AI-Assisted SDD | GitHub Spec Kit, Amazon Kiro, Tessl |
| Model-Based Design | Simulink, SCADE |

GitHub Spec Kit structures work as `/specify → /plan → /tasks → implement`. Tessl takes the most radical position, treating the spec as the only artifact developers maintain directly.

## Case Studies

- **Financial services microservices:** Mandating OpenAPI specs before coding cut integration cycle time by 75% by surfacing incompatibilities at the spec-review stage rather than in production.
- **Enterprise project management:** Using Cucumber's Gherkin scenarios as the shared definition of "done" eliminated disputes between developers and product managers over whether features were complete.
- **Automotive engine control:** Engineers modeled control logic in Simulink, verified behavior through simulation, then generated certified C code. Nobody edits the generated code—changes go through the model.

## When SDD Adds Value (and When It Doesn't)

**Use SDD when:** working with AI assistants, requirements are complex, multiple maintainers exist, integration between services is heavy, or regulatory traceability is required.

**Skip elaborate specs when:** building throwaway prototypes, solo short-lived projects, doing exploratory coding, or working on simple CRUD apps with self-evident requirements.

The paper's guiding principle: use "the minimum level of specification rigor that removes ambiguity for your context."

## SDD vs. Traditional Design Docs

The distinction isn't what gets written—HLD, LLD, and SRS documents have existed for decades. The difference is *enforcement*. Traditional docs are advisory; SDD specs are executable. BDD scenarios run as tests; OpenAPI contracts are validated in CI. The paper quotes Bryan Finster: "SDD is not a revolution… it's just BDD with branding"—but argues the framing matters because it reframes specs as authoritative rather than advisory.

## Conclusion

As AI capability grows, the bottleneck shifts from writing code to writing good specifications. The paper frames the developer's evolving role as moving from code producer to "spec author and AI orchestrator"—designing systems through specifications rather than implementation.

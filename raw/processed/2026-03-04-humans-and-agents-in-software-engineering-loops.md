---
source_url: https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html
author: Kief Morris
date: 2026-03-04
---

# Humans and Agents in Software Engineering Loops

Kief Morris argues against both extremes of AI-assisted development — pure vibe coding with no human oversight, and micromanaging every line of agent-generated code. Instead, he proposes a third position: humans working "on the loop."

## The Two Core Loops

Morris distinguishes between:
- **The "why" loop** — iterating on ideas to produce working software (humans always own this)
- **The "how" loop** — the mechanics of building software through code, tests, specs, and tooling

The how loop contains nested sub-loops: outer loops handle features, middle loops handle stories, inner loops handle code generation.

## Three Stances

| Stance | Description |
|--------|-------------|
| **Humans outside** | Vibe coding — agents run the how loop entirely |
| **Humans in** | Humans inspect/gate every agent output; creates bottlenecks |
| **Humans on** | Humans build and maintain the *harness* that guides agents |

## The "On the Loop" Concept

Rather than fixing individual artefacts agents produce, the "on the loop" approach means improving the **harness** — the collection of specs, quality checks, and workflow guidance controlling agent behavior. Morris references this as related to "Harness Engineering."

The key distinction: when an agent produces unsatisfactory output, *in-the-loop* humans fix the artefact; *on-the-loop* humans fix the system that produced it.

## The Agentic Flywheel

Morris describes an escalating improvement cycle:
1. Agents evaluate their own loop performance using tests and evaluations
2. Agents recommend harness improvements
3. Humans review, then progressively automate approval of low-risk changes
4. Production data, user journeys, and metrics feed richer signals back into the loop

The result, he argues, won't be a one-off solution but potentially "anti-fragile systems that continuously improve themselves."

## On Internal vs. External Quality

Morris acknowledges that internal code quality matters even with AI — not for developer experience per se, but because cleaner codebases let LLMs "work faster and spiral less," reducing time and cost.

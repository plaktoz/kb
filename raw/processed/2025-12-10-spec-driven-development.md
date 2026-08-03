---
source_url: https://thoughtworks.medium.com/spec-driven-development-d85995a81387
author: Liu Shangqi
date: 2025-12-10
---

# Spec-Driven Development

## Summary

Spec-driven development (SDD) is described as "a development paradigm that uses well-crafted software requirement specifications as prompts, aided by AI coding agents, to generate executable code."

## Key Points

**What it is:** SDD separates planning from implementation. Requirements are analyzed, formalized into Markdown spec files, reviewed iteratively with human oversight, then handed to a coding agent for implementation.

**What a spec is:** More than a product requirements document — it explicitly defines external software behavior: inputs/outputs, preconditions, invariants, interface types, and state machines.

**What makes a good spec:**
- Domain-oriented language describing business intent
- Clear Given/When/Then scenario structure
- Completeness without enumerating every case
- Deterministic enough to reduce model hallucinations
- Semi-structured formatting to improve LLM reasoning

**Is it waterfall?** The author argues no — waterfall's problem was long feedback cycles, whereas vibe coding's problem is being "too fast, spontaneous and haphazard." SDD provides shorter, more effective feedback loops than pure vibe coding.

**Key risks:**
- No consensus on correct SDD workflow
- Code generation from specs is non-deterministic
- "Spec drift and hallucination are inherently difficult to avoid"
- Still requires robust CI/CD practices

**Relationship to context engineering:** Separating planning from implementation "essentially compresses the context into specs," making agent-LLM interaction more effective.

The author notes SDD "remains an emerging practice" with significant evolution expected in 2026.

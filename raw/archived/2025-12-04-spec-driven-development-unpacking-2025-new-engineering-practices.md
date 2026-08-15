---
source_url: https://www.thoughtworks.com/insights/blog/agile-engineering-practices/spec-driven-development-unpacking-2025-new-engineering-practices
author: Liu Shangqi
date: 2025-12-04
---

# Spec-driven development: Unpacking one of 2025's key new AI-assisted engineering practices

Spec-driven development (SDD) is a paradigm using well-crafted software requirement specifications as prompts for AI coding agents to generate executable code. The author describes it as one of 2025's most important emerging practices.

## Key Points

- **Definition debate:** Some view specs as the sole source of truth (code as byproduct); others (including the author) see specs as drivers of code generation, with executable code remaining the authoritative artifact.

- **What a spec is:** More than a PRD — it explicitly defines external software behavior: input/output mappings, preconditions, invariants, interface types, and state machines. Good specs use domain language, Given/When/Then structure, and aim for clarity to reduce AI hallucinations.

- **Connection to context engineering:** Specs compress contextual information for AI agents, drawing on BDD's few-shot prompting techniques. Tools like Cursor, Claude Code, and Context7 support SDD workflows.

- **Not waterfall:** Traditional waterfall failed through long feedback cycles. Vibe coding fails through excessive speed and lack of discipline. SDD provides "shorter and effective" feedback loops by reintroducing design rigor.

- **Challenges:** No consensus on ideal workflows, non-deterministic code generation, spec drift, hallucination risks, and ongoing debate about whether spec or code is the ultimate artifact.

The author concludes that SDD remains emerging, with significant evolution expected through 2026.

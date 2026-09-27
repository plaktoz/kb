---
source_url: https://dashbit.co/blog/evolving-ai-era
author: José Valim
date: 2026-09-24
---

# Evolving Programming Languages in the AI Era

Valim explores how programming languages and their surrounding communities may need to adapt as AI coding agents become primary code authors.

## Reflections

**Community:** Language communities form around shared sensibilities — Python's clarity, Ruby's developer happiness, Lisp's metaprogramming. If humans write less code, these social bonds may weaken. Agents could simultaneously lower the cost of building ecosystems while reducing the collaborative motivation to do so.

**Ergonomics:** Syntax improvements (like optional chaining) matter far less to agents than humans. Valim dismisses languages marketed as "agent-first" that focus mainly on syntax, arguing they're optimizing for today's temporary limitations.

**Compilers:** He rejects the idea that agents will simply write raw assembly, noting the ongoing need for architecture-independent representations and specialized computational models (systems languages, query languages, theorem provers, etc.).

## Agentic Tooling

**Stronger Guarantees:** Agents tolerate verbosity, so languages can offer richer type systems without prioritizing inference. He outlines a layered approach:
- Correct by construction
- Statically established (types, proofs)
- Runtime-enforced
- Empirically validated (testing, fuzzing)

**Program Databases:** LSPs were designed around human document navigation (file/line/column). Agents would benefit more from queryable program databases — think SQLite or Datalog — enabling complex queries like "find all public functions that eventually call this function."

**Runtime Observability:** Rather than step-through debuggers, agents need programmatic runtime interfaces. Erlang/Elixir's VM is cited as already strong here, with built-in inspection of processes, queues, and system state.

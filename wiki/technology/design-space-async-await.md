---
type: literature-note
source_url: https://cel.cs.brown.edu/blog/design-space-async-await/
author: Gavin Gray
tags: [async-await, concurrency, programming-languages, language-design]
date_consumed: 2026-09-12
---

## Summary

Modern languages (Python, Rust, Swift, C#, JavaScript) all implement `async`/`await` — dubbed "straight-line asynchrony" — but their semantics diverge far more than developers expect. A simple fire-and-forget program produces four distinct outputs across seven runtimes, with no two runtimes agreeing. The authors map this divergence onto nine design dimensions and formalize it with a small-step abstract machine.

## Core Concepts

- **[[Straight-Line Asynchrony]]** — the paradigm of making concurrent code read like sequential code via `async`/`await`
- **[[Task Lifetime]]** — three phases (Start of Life, End of Life, Cancellation) organize the nine design dimensions
- **[[Eagerness]]** — whether a task begins executing immediately (C#, JavaScript) or only on first `await` (Python, Rust)
- **[[Task Suspension]]** — Static (only at explicit `await` points, as in JavaScript) vs. Dynamic (can suspend at any yield point)
- **[[Task Extent]]** — Indefinite (task outlives its lexical scope) vs. Dynamic (Swift, Trio constrain lifetime to scope)
- **[[Structured Concurrency]]** — enforced by Trio and Swift's Dynamic Extent, which cancel or await child tasks before the parent exits
- **[[Cancellation Semantics]]** — varies across Unaware (Rust), direction (top-down vs. bottom-up), and persistence (transient vs. persistent)
- **[[Formal Core Calculus]]** — a small-step abstract machine built to trace execution divergence across runtime configurations

## Key Takeaways

- **Same code, different outputs**: one fire-and-forget program yields 4+ distinct outputs across 7 runtimes.
- **Nine axes of variation**: Eagerness, Suspension, Extent, Reference Strength, Destruction, Propagation, Awareness, Direction, Persistence.
- **Swift behavior**: Dynamic Extent + Cancelled Destruction → prints `AC` (background task killed on scope exit).
- **Trio behavior**: Dynamic Extent + Awaited Destruction → prints `ABC` (scope awaits all child tasks before exiting).
- **Laziness matters**: Python and Rust tasks do not start until explicitly awaited — easy to accidentally never run them.
- **Exception propagation**: some runtimes silently drop exceptions from unawaited tasks; others re-raise them.
- **Formal model**: design decisions appear as labeled forks in reduction sequences — precise, auditable semantics.
- **Developer surprise**: most programmers assume `async`/`await` means the same thing across languages — it does not.

## 🧠 First Principles & Mental Models

- **[[Leaky Abstraction]]**: `async`/`await` promises to hide concurrency behind sequential syntax, but the underlying scheduler semantics leak through in edge cases — exactly why identical code diverges across runtimes.
- **[[Accidental Complexity]]**: the nine axes of variation are not inherent to the problem of asynchrony; they reflect independent, often underdocumented implementation choices that accumulate into a fragmented ecosystem.

## 🃏 Review Questions

**Q1**: What is the central finding of this design space exploration?
**A**: Seven async/await runtimes produce different outputs from the same fire-and-forget program, because the same `async`/`await` syntax hides nine independent design dimensions that vary across languages.

**Q2**: How do Swift and Trio differ in their handling of an unawaited background task at scope exit?
**A**: Swift uses Dynamic Extent with Cancelled Destruction, so the background task is cancelled when the scope exits (output `AC`); Trio uses Dynamic Extent with Awaited Destruction, so the scope blocks until all child tasks finish (output `ABC`).

**Q3**: How can a developer use this framework in practice?
**A**: By identifying which of the nine dimensions their target runtime uses — especially Eagerness and Extent — they can predict and control whether fire-and-forget tasks actually run, complete, or silently fail.

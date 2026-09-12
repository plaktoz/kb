# A Design Space Exploration of Async/Await

source_url: https://cel.cs.brown.edu/blog/design-space-async-await/
author: Gavin Gray
date: 2026-09-08
publication: Cognitive Engineering Lab (Brown University)

---

## Overview

Modern languages like Python, Rust, Swift, C#, and JavaScript all implement `async`/`await`, but their semantics diverge far more than most developers realize. The authors term this paradigm **"straight-line asynchrony"** — making concurrent code read like sequential code.

---

## The Core Surprise

A simple pseudocode program that spawns a background logging task and exits without awaiting it produces **four different outputs** across seven runtimes. Across three variations of this program, *no two runtimes produce identical results*.

---

## Nine Design Dimensions

The paper identifies nine axes of variation, grouped by task lifetime phase:

### Start of Life
- **Eagerness** — Lazy (Python, Rust) vs. Eager (C#, JavaScript)
- **Suspension** — Static (JavaScript) vs. Dynamic (most others)

### End of Life
- **Extent** — Indefinite vs. Dynamic (Swift, Trio)
- **Reference Strength** — Strong vs. Weak
- **Destruction** — Awaited / Cancelled / Terminated
- **Propagation** — Whether exceptions escape unawaited tasks

### Cancellation
- **Awareness** — Unaware (Rust) vs. Aware
- **Direction** — Top-Down / Bottom-Up / Simultaneous
- **Persistence** — Transient vs. Persistent

---

## Key Example Explained

For the fire-and-forget pattern, two dimensions dominate:

- **Swift** uses Dynamic Extent + Cancelled Destruction → prints `AC`
- **Trio** uses Dynamic Extent + Awaited Destruction → prints `ABC`
- Other runtimes with Indefinite Extent may print `ACB`, `C`, or other variants

---

## Formal Model

The team built a **formal core calculus** with a small-step abstract machine to precisely trace execution divergence. Design decisions appear as labeled forks in reduction sequences — making explicit exactly *why* the same program behaves differently across runtimes.

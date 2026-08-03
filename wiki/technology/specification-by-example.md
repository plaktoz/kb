---
type: literature-note
source_url: https://martinfowler.com/bliki/SpecificationByExample.html
author: Martin Fowler
tags: [specification-by-example, tdd, design-by-contract, agile]
date_consumed: 2026-08-03
---

## Summary

[[Martin Fowler]] traces the phrase "Specification by Example" to a 2002 XP/Agile Universe workshop, framing it as a characterization of one key role tests play in [[Extreme Programming]]. Unlike traditional specifications that aim for generality, SBE uses concrete examples to highlight specific points — making it unsuitable as a sole requirements technique but highly practical when paired with other tools. Fowler positions SBE as his most-used requirements tool, valued for its accessibility to non-technical stakeholders compared to formal pre/post conditions.

## Core Concepts

- **[[Specification by Example]]** — a technique where requirements are expressed as concrete, representative examples rather than general rules; readers must infer broader behavior from the instances given.
- **[[Test-Driven Development]] (TDD)** — the double-check mechanism: the same behavior is expressed in both code and tests using *different* methods, improving error detection without requiring formal verification.
- **[[Design by Contract]]** — formal pre/post-condition specification; rigorous but difficult to write in enterprise settings ("as hard to write as the solution itself").
- **[[Domain Driven Design]]** — cited by Fowler as a complementary tool that SBE must be paired with to address its coverage limitations.
- **Double-check principle** — the key advantage of SBE over formal methods: expressing the same intent in two independent representations makes verification automatic and low-friction.

## Key Takeaways

- **Origin**: The term "Specification by Example" coined at a 2002 XP/Agile Universe workshop.
- **Examples vs. rules**: Examples highlight specifics; general rules must be inferred — SBE cannot stand alone.
- **Accessibility advantage**: Examples are far easier for non-technical stakeholders than formal pre/post conditions.
- **Double-check value**: TDD achieves error detection through redundant representation, not formal verification.
- **Tooling gap of formal methods**: Pre/post conditions are hard to write and hard to verify automatically.
- **Complementary stack**: SBE works best alongside conversation, [[Domain Driven Design]], and doses of [[Design by Contract]].
- **Fowler's stance**: "Perhaps my most used tool, but never my only tool."

## 🧠 First Principles & Mental Models

- **[[Redundant Representation]]**: TDD's double-check principle — expressing intent in both code and tests via different methods — is a direct application of redundancy for error detection, the same principle behind checksums and two-person verification rules.
- **[[Pareto Principle]]**: SBE addresses the 80% of requirements that are best communicated through examples, while reserving formal methods for the narrow set of invariants where exhaustive generality actually matters.

## 🃏 Review Questions

**Q1**: What is the core claim Fowler makes about Specification by Example?
**A**: SBE is a powerful and accessible requirements technique — easier for stakeholders than formal methods — but it must be combined with other tools because examples only highlight specific points and cannot cover all cases alone.

**Q2**: How does TDD embody the "double-check principle" that Fowler attributes to SBE?
**A**: TDD expresses the same behavior in both production code and tests using *different* methods; this independent redundancy automatically surfaces errors that a single representation would miss, without needing formal verification machinery.

**Q3**: When should SBE be supplemented with Design by Contract?
**A**: When invariants must be specified exhaustively and verified rigorously — contexts where the cost of a missed edge case is high — since Design by Contract's pre/post conditions cover generality that examples alone cannot guarantee.

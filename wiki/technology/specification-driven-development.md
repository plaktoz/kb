---
type: literature-note
source_url: https://en.wikipedia.org/wiki/Specification-driven_development
author: Wikipedia contributors
tags: [software-development, specifications, tdd, agile]
date_consumed: 2026-08-03
---

## Summary

Specification-driven development is a software development methodology where specifications serve as the primary foundation for building software. It falls under the broader category of [[Documentation-Driven Development]], alongside [[Model-Driven Development]], model transformation, and round-trip engineering. Researchers Ostroff, Makalsky, and Paige proposed an agile variant combining [[Test-Driven Development]] with the plan-based principles of [[Design by Contract]], treating tests and contracts as complementary specification types.

## Core Concepts

- **[[Specification-Driven Development]]**: A methodology that elevates formal or semi-formal specifications as the driver of software construction, rather than ad hoc implementation.
- **[[Documentation-Driven Development]]**: The parent paradigm encompassing specification-driven development, model-driven development, and related approaches.
- **[[Design by Contract]]**: A plan-based methodology requiring software components to define formal obligations (preconditions, postconditions, invariants); used alongside tests in the agile variant.
- **[[Test-Driven Development]] (TDD)**: An agile practice where tests are written before implementation; the agile SDD variant integrates this with contract-based specifications.
- **[[Behavior-Driven Development]] (BDD)**: A related methodology emphasizing human-readable specifications of behavior.
- **[[Formal Methods]]**: Mathematically rigorous techniques for specifying and verifying software, closely related to SDD's theoretical roots.
- **[[Model-Driven Engineering]]**: A sibling approach within documentation-driven development focused on abstract models as primary artifacts.

## Key Takeaways

- **Parent paradigm**: Specification-driven development sits under [[Documentation-Driven Development]] as a sibling to model-driven development.
- **Agile hybrid**: Ostroff, Makalsky & Paige (2004) combined SDD with TDD principles in *Extreme Programming and Agile Processes in Software Engineering*.
- **Complementary specs**: Tests and contracts are framed as distinct yet complementary specification types — not substitutes.
- **Key related methods**: [[Behavior-Driven Development]], [[Design by Contract]], [[Formal Methods]], [[Model-Driven Engineering]], [[Test-Driven Development]].
- **Academic grounding**: Liu et al. (2021) contributed rigorous code review via reverse engineering, extending SDD's formal lineage.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: SDD isolates *what* the software should do (the specification) from *how* it does it (the implementation), keeping the contract as a stable north star even as implementation details change.
- **[[Complementarity Principle]]**: Ostroff et al.'s insight that tests and contracts are not interchangeable but complementary reflects the general principle that different representations of a problem capture different facets — using both is more powerful than either alone.

## 🃏 Review Questions

**Q1**: What is the core claim of specification-driven development as a methodology?
**A**: Specifications serve as the primary foundation for building software, guiding construction rather than emerging after the fact.

**Q2**: How did Ostroff, Makalsky, and Paige extend SDD for agile contexts?
**A**: They proposed combining SDD with test-driven development, treating tests and design-by-contract obligations as distinct but complementary specification types within an agile workflow.

**Q3**: How would you apply SDD's distinction between tests and contracts in a real project?
**A**: Write formal contracts (preconditions, postconditions) to capture invariants the implementation must never violate, and unit tests to drive incremental behavior — each catching failure modes the other misses.

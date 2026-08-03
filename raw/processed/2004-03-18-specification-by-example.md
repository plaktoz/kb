---
source_url: https://martinfowler.com/bliki/SpecificationByExample.html
author: Martin Fowler
date: 2004-03-18
---

# Specification By Example

Martin Fowler traces the phrase "Specification By Example" to a 2002 XP/Agile Universe workshop, describing it as a way to characterize one role of testing in XP.

## Core Idea

Unlike traditional specifications — which aim to be general and cover all cases — examples highlight specific points, requiring the reader to infer broader rules. This makes SBE unsuitable as a *sole* requirements technique, but it can still play a leading role.

## Comparison to Formal Methods

Pre/post conditions (as used in Design by Contract) dominate rigorous specification approaches, but Fowler found them difficult in enterprise settings — "as hard to write...as it is to write the solution." Examples, by contrast, are easier to produce, especially for non-technical stakeholders.

## The Double-Check Principle

TDD embodies a double-check: the same thing is expressed in both code and tests, using *different* methods — which improves error detection. Formal specification struggles to verify designs automatically; SBE makes this straightforward.

## Limitations & Context

SBE requires a collaborative working relationship. It must be paired with other tools: regular conversation, Domain Driven Design, and even doses of Design by Contract. As Fowler puts it, SBE is "perhaps my most used tool, but never my only tool."

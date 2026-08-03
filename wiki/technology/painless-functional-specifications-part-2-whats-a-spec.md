---
type: literature-note
source_url: https://www.joelonsoftware.com/2000/10/03/painless-functional-specifications-part-2-whats-a-spec/
author: Joel Spolsky
tags: [functional-specification, software-development, technical-writing, project-management]
date_consumed: 2026-08-03
---

## Summary

[[Joel Spolsky]] defines the structure and purpose of a functional specification, distinguishing it from a technical specification: a functional spec describes the product from the user's perspective (screens, dialogs, features), while a technical spec covers internal implementation details. He argues the user experience must be fully nailed down before any technical decisions are made, and that specs should remain living documents updated continuously until code-complete.

## Core Concepts

- **[[Functional Specification]]**: A document describing what a product does from the user's perspective — screens, features, error states, and dialogs — before any implementation begins. Contrasted with a [[Technical Specification]], which covers internal data structures and algorithms.
- **[[Joel Spolsky]]**: Software engineer and author of Joel on Software; argues specs are the primary risk-reduction tool in software projects.
- **[[Spec Disclaimer]]**: An upfront acknowledgment that the spec is incomplete, protecting the author and signaling that the document is a living artifact.
- **[[Single Author Principle]]**: One person owns the spec and is responsible for its coherence; distributed authorship produces inconsistency and diffused accountability.
- **[[User Scenarios]]**: Vivid, fictional but realistic users who embody actual use cases — used to ground spec decisions in concrete human behavior rather than abstract feature lists.
- **[[Nongoals]]**: Explicitly listed features that will not be built in the current version; controls scope creep and aligns expectations before development begins.
- **[[Open Issues]]**: Flagged unresolved questions within the spec that must all be resolved before coding begins.
- **[[Living Document]]**: Spolsky's model for specs — continuously updated through development rather than frozen after sign-off, rejecting the waterfall hand-off model.

## Key Takeaways

- **Functional vs Technical**: Functional specs describe user experience; technical specs describe implementation.
- **User Experience First**: UX decisions must be finalized before technical architecture is chosen.
- **Disclaimer**: Protects the author and signals the doc is a work in progress.
- **Single Owner**: One author per spec ensures coherent voice and clear accountability.
- **Scenarios**: Fictional users ground decisions in real-world behavior patterns.
- **Nongoals**: Explicitly out-of-scope items prevent scope creep from slipping in.
- **Exhaustive Details**: Every screen, dialog, error case, and edge case must be covered.
- **Open Issues**: All unresolved questions must be flagged and resolved before coding starts.
- **Anti-Waterfall**: Specs should evolve continuously, not be frozen and thrown over the wall.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: By cleanly separating what the product does (functional spec) from how it works (technical spec), Spolsky ensures UX constraints are never silently compromised by implementation convenience — each concern is resolved in its proper domain.
- **[[Pre-Mortem Thinking]]**: Open Issues and Nongoals function as a structured pre-mortem — forcing teams to surface and resolve ambiguities before they become expensive mid-development surprises.

## 🃏 Review Questions

**Q1**: What is the core distinction Spolsky draws between a functional spec and a technical spec?
**A**: A functional spec describes the product from the user's perspective (screens, features, dialogs), while a technical spec covers internal implementation details like data structures and algorithms; UX decisions must come first.

**Q2**: Why does Spolsky insist on a single author for a functional spec, and what role do "Nongoals" play?
**A**: A single author ensures coherent voice and clear accountability; Nongoals explicitly list features that won't be built, preventing scope creep and aligning all stakeholders on boundaries before work begins.

**Q3**: How does Spolsky's "living document" model challenge the traditional waterfall approach to specs?
**A**: Rather than freezing the spec and handing it to developers, Spolsky argues specs should be continuously updated until the product is code-complete — treating them as evolving design artifacts rather than static contracts.

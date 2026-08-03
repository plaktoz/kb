---
source_url: https://www.joelonsoftware.com/2000/10/03/painless-functional-specifications-part-2-whats-a-spec/
author: Joel Spolsky
date: 2000-10-03
---

# Painless Functional Specifications – Part 2: What's a Spec?

Spolsky distinguishes between two spec types: a *functional specification* describes the product from the user's perspective (screens, features, dialogs), while a *technical specification* covers internal implementation (data structures, algorithms, etc.). He argues the user experience must be nailed down before any technical decisions are made.

## Essential Components of a Good Functional Spec

- **Disclaimer** – Protects the author; acknowledges incompleteness early on
- **Single Author** – One person owns and is responsible for the spec
- **Scenarios** – Realistic, vivid fictional users representing actual use cases
- **Nongoals** – Explicitly lists features that won't be built, to control scope
- **Overview** – High-level summary or flowchart for the big picture
- **Details** – Exhaustive coverage of every screen, error case, and edge case; "decisions that somebody is going to have to make"
- **Open Issues** – Flagged unresolved questions, all resolved before coding begins
- **Side Notes** – Audience-specific annotations (Technical Notes, Testing Notes, etc.)

Spolsky strongly rejects the "waterfall" approach of freezing specs and throwing them at developers. Instead, specs should remain living documents, updated continuously until the product reaches code-complete status.

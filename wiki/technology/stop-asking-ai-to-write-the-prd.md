---
type: literature-note
source_url: https://hackernoon.com/stop-asking-ai-to-write-the-prd
author: superorange0707
tags: [product-requirements, ai-tools, requirements-engineering, software-methodology]
date_consumed: 2026-09-21
---

## Summary

Asking an LLM to generate a PRD produces a "beautiful lie" — professional-looking prose that conceals missing sources, contradictions, and invented details. The root problem is treating prose as the system of record for requirements. The proposed fix is a compiler pipeline model where requirements are represented as a typed claim graph with traceable evidence, explicit conflict detection, and tests before prose.

## Core Concepts

- **"Beautiful Lie" Problem** — AI-generated PRDs look polished but hide missing sources, contradictions, and hallucinated details by blending them into fluent prose.
- **[[Typed Claim Graph]]** — Each requirement is a structured object with type, sources, confidence state (`SUPPORTED | INFERRED | CONFLICTED | UNSOURCED | REJECTED`), owner, and version. The graph is the durable artifact, not the document.
- **Compiler Pipeline Metaphor** — Requirements flow through stages: raw requests and evidence → claims → normalized domain model → conflicts and gaps → interfaces and acceptance tests → versioned specification views.
- **Addressable Evidence** — Sources must point to versioned, immutable artifacts (interviews, policy docs, tickets, [[Architecture Decision Records|ADRs]]). "The stakeholder said so" is not traceability.
- **[[Domain Glossary]] Normalization** — Terms must be normalized before resolving rules to prevent silently merging distinct concepts under the same label.
- **Conflict Detection** — Contradictions are logged as data objects with owners and open/closed status, not smoothed into vague prose.
- **Interface Derivation** — Explicit domain rules generate implementation-facing artifacts: enums, APIs, commands, events, error contracts.
- **Tests Before Prose** — Acceptance scenarios expose ambiguity faster than polished writing; if no observable pass condition exists, the requirement is not ready.
- **Human Authority** — [[AI]] automates extraction and linking; humans decide on policy conflicts, legal interpretation, risk, and scope.
- **Audience-Specific Views** — One versioned graph renders into tailored representations for executives, engineering, QA, security, and ops.

## Key Takeaways

- **Core failure mode**: Prose conceals requirement quality; a graph exposes it.
- **Confidence states**: Every claim is tagged SUPPORTED, INFERRED, CONFLICTED, UNSOURCED, or REJECTED.
- **Honest status report**: "17 supported / 3 inferred / 2 conflicts / 5 missing acceptance conditions" beats a 40-page PRD.
- **Evidence rule**: Sources must be versioned, immutable artifacts — not verbal summaries.
- **Tests first**: No observable pass condition = requirement not ready.
- **AI role**: Automates extraction and linking; never decides policy or risk.
- **Output order**: Generate polished prose only *after* the underlying graph is coherent.
- **Uncertainty signal**: The document should surface uncertainty, not erase it.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: When a polished PRD becomes the deliverable target, teams optimize for document quality rather than requirement clarity — exactly the failure mode the author documents with AI-generated PRDs.
- **[[Garbage In, Garbage Out]]**: Fluent prose can repackage unsourced or contradictory inputs without flagging them; a typed claim graph makes input quality visible before it propagates into code.

## 🃏 Review Questions

**Q1**: What is the "beautiful lie" problem with AI-generated PRDs?
**A**: LLMs produce professional-looking prose that conceals missing sources, contradictions, and invented details — the document looks complete while the underlying requirements remain unresolved.

**Q2**: What is a Typed Claim Graph and what confidence states does it use?
**A**: A Typed Claim Graph represents each requirement as a structured object with type, sources, owner, version, and one of five confidence states: SUPPORTED, INFERRED, CONFLICTED, UNSOURCED, or REJECTED.

**Q3**: When should polished prose be generated from this system?
**A**: Only after the underlying graph is coherent — the document is a rendering of a verified graph, not the primary artifact, and should surface uncertainty rather than erase it.

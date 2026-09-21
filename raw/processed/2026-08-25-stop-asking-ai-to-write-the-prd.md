---
source_url: https://hackernoon.com/stop-asking-ai-to-write-the-prd
author: superorange0707
date: 2026-08-25
---

# Stop Asking AI to Write the PRD

The author argues that asking an LLM to generate a PRD produces what they call "a beautiful lie" — professional-looking prose that conceals missing sources, contradictions, and invented details. The core problem: treating prose as the system of record.

## Central Metaphor

The proposed alternative treats requirements like a compiler pipeline:

> "raw requests and evidence → claims → normalized domain model → conflicts and gaps → interfaces and acceptance tests → versioned specification views"

The durable artifact is a **graph**, not a document.

## Key Concepts

- **Typed Claim Graph** — Each requirement is a structured object with type, sources, confidence state (`SUPPORTED | INFERRED | CONFLICTED | UNSOURCED | REJECTED`), owner, and version.
- **Addressable Evidence** — Sources must point to versioned, immutable artifacts (interviews, policy docs, tickets, ADRs). "The stakeholder said so" is not traceability.
- **Domain Glossary** — Normalize terms before resolving rules to prevent silently merging distinct concepts.
- **Conflict Detection** — Log contradictions as data objects with owners and open/closed status rather than blending them into vague prose.
- **Interface Derivation** — Explicit domain rules generate implementation-facing artifacts: enums, APIs, commands, events, error contracts.
- **Tests Before Prose** — Acceptance scenarios expose ambiguity faster than polished writing. If no observable pass condition exists, the requirement isn't ready.
- **Human Authority** — AI automates extraction and linking; humans decide on policy conflicts, legal interpretation, risk, and scope.
- **Audience-Specific Views** — One versioned graph renders into tailored representations for executives, engineering, QA, security, and ops.

## Honest Output Example

The author suggests a well-functioning system should comfortably report:

> "17 supported claims / 3 inferred claims requiring confirmation / 2 policy conflicts / 5 missing acceptance conditions / 1 unresolved data-retention owner / 0 implementation-ready release"

That looks less impressive than a forty-page PRD — and is far more actionable.

## Closing Argument

Generate polished prose only after the underlying graph is coherent. The document should surface uncertainty rather than erase it.

---
source_url: https://huggingface.co/blog/mrmanna/ddse-vs-sdd
author: Mahmudur R Manna
date: 2025-10-16
---

# Decision-Driven vs. Spec-Driven Software Engineering

## Core Distinction

**DDSE (Decision-Driven Software Engineering)** uses a typed hierarchy of Technical Decision Records (TDRs) stored in-repo as its source of truth, with CI/CD enforcement and machine-parsable AI context blocks.

**SDD (Spec-Driven Development)** (via GitHub's Spec Kit) treats the written spec as truth, converting it into agent-executable plans and tasks across tools like Copilot, Claude Code, and Gemini CLI.

## Key Differentiators

**AI Alignment:** DDSE embeds constraints and verification commands directly into each TDR. SDD alignment depends on spec clarity and agent behavior.

**Contracts:** DDSE's Contract Decision Records (CDR) provide "mock servers, TypeScript type generation, and contract tests" enabling parallel front-end/back-end delivery. SDD has no standardized contract primitive.

**Traceability:** DDSE requires decision-to-code annotations. SDD's traceability is implicit.

**Governance:** DDSE prescribes authority matrices and CI-enforced compliance. SDD governance is largely team-defined.

## When to Use Each

- **SDD:** Prototyping, small teams, contained subsystems — "low activation energy" for early delivery.
- **DDSE:** Enterprise-scale, audit requirements, parallel teams, AI-accelerated development needing provable governance.

## Conclusion

The article frames SDD as strong for speed-first scenarios, while positioning DDSE as the more complete model where "sustainable agility at scale" is the mandate — noting that "decisions run the enterprise."

---
type: literature-note
source_url: https://www.unite.ai/openrouter-cuts-three-providers-after-ai-prompt-exposure-findings
author: Miles Okada
tags: [openrouter, data-privacy, zero-data-retention, llm-security]
date_consumed: 2026-11-23
---

## Summary
OpenRouter off-boarded three inference providers and removed 125 endpoints from Zero Data Retention (ZDR) eligibility after Dragos canary tests found customer prompts exposed or retained by AI providers. Provider notices from Novita, Phala and Together AI describe separate incidents, including a routing misconfiguration, an exploited legacy service and a leaked credential. ZDR eligibility now depends on validating actual request paths, not just provider assurances.

## Core Concepts
- [[OpenRouter]]: AI routing marketplace that removed endpoints from [[Zero Data Retention]] eligibility.
- [[Dragos]] canary tests: about two million prompts with unique URLs and canary credentials, July to November 2026.
- [[Multi-Hop Inference Routing]]: every organization on the path can see the full prompt and response.
- [[Novita]], [[Phala]], [[Together AI]]: providers with separate disclosed incidents.
- [[Credential Leakage]]: an AI coding agent committed a private repository credential to a public GitHub repo.
- [[Canary Tokens]]: seeded fake credentials used to detect misuse.

## Key Takeaways
- **Provider Removals**: Three providers off-boarded; 125 endpoints lost ZDR eligibility.
- **No OpenRouter Breach**: Findings did not show unauthorized access to OpenRouter itself.
- **Canary Evidence**: Couple hundred seeded AWS keys led to tens of thousands of API calls.
- **Early-Copy Pattern**: Keys from rejected requests suggest copying at request intake, not model processing.
- **Phala Exposure**: Legacy service plus trusting loopback management interfaces exposed in-flight data.
- **Together AI Leak**: Stored prompt samples downloaded after a coding agent committed a credential.
- **New Standard**: ZDR eligibility requires technically verified network paths plus assurances.

## 🧠 Core Principles

**T1. Verify claims against observed behavior** — Stated privacy settings and policies are not evidence; only testing the actual data path shows whether prompts are retained or forwarded. · *model:* [[Trust but Verify]]
→ explains: Canary Evidence, New Standard

**T2. Exposure grows with every hop** — Each additional party in a request path can see the full prompt, so risk compounds with routing depth. · *model:* [[Attack Surface]]
→ explains: Early-Copy Pattern, Phala Exposure, Together AI Leak

## 🃏 Review Questions

**Q1**: Why did OpenRouter remove providers and endpoints from ZDR eligibility?
**A**: Dragos canary tests and provider notices showed prompts being exposed, retained, or forwarded to third parties despite privacy settings, so OpenRouter off-boarded three providers and removed 125 endpoints.

**Q2**: How did Dragos detect the exposure?
**A**: It sent about two million prompts with unique URLs and canary credentials, then monitored later activity; seeded AWS keys were used for tens of thousands of API calls, including from requests rejected before a model ran.

**Q3**: What changes for organizations relying on ZDR routing?
**A**: ZDR eligibility now rests on validating the actual request path alongside provider assurances, so ongoing testing must expose undisclosed forwarding and retention before customer data is affected.

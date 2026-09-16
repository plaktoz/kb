---
type: literature-note
source_url: https://hackernoon.com/how-to-audit-what-your-ai-agents-are-accessing
author: ameliepangolin
tags: [ai-agents, security, access-control, observability]
date_consumed: 2026-09-16
---

## Summary

[[Tailscale]]'s AI gateway product, [[Aperture]], gives organizations cryptographic-identity-based logging and pre-request policy enforcement for AI agents like [[Claude Code]] and [[Codex]]. Every request is tied to a Tailscale identity (user, device, or tag), captured with full request/response bodies and token metadata, and gated by deny-by-default access grants. Guardrail policies run before data reaches model providers, enabling PII scrubbing, tool-call authorization, and per-user spending quotas.

## Core Concepts

- **[[Aperture]]**: Tailscale's AI gateway that proxies requests from AI agents to model providers, injecting observability and policy enforcement at the network layer.
- **[[Tailscale]] Identity**: Cryptographic identity (login name, device ID, tag) attached to every proxied request; non-human agents like CI runners are identified by their tag.
- **[[Session Grouping]]**: Requests are grouped into sessions, providing contextual context for reviewing sequences of agent actions rather than isolated calls.
- **[[Deny-by-Default Access Grants]]**: Log access is restricted by default; grants can be scoped by identity, tag, provider, or model — and all admin log views are themselves audited.
- **[[Pre-Request Guardrails]]**: Policies evaluated before data reaches the provider: PII scrubbing, request blocking, tool-call authorization, and per-user/group spending quotas.
- **[[SIEM]] Integration**: Retention is configurable (down to zero); captured data can be exported to S3-compatible storage for ingestion into SIEM pipelines.
- **[[Fail Closed / Fail Open]]**: Services can be configured to fail closed (deny all) or fail open (allow all) when guardrails are unreachable — a critical reliability vs. safety tradeoff.

## Key Takeaways

- **Cryptographic identity**: Every AI agent request carries Tailscale-verified login, device ID, and tags.
- **Full capture**: Request/response bodies, headers (sensitive values redacted), token counts, model name, tool use.
- **Async capture**: Logging is asynchronous — no performance impact on agent requests.
- **Scoped log access**: Grants can restrict by identity, tag (`tag:ci-runner`), provider (`anthropic/**`), or model.
- **Admin auditability**: Viewing logs is itself logged — no privileged blind spots.
- **PII scrubbing**: Guardrails can strip sensitive data before it reaches the provider.
- **Spending quotas**: Per-user or per-group token spend limits are enforceable pre-request.
- **Integrations**: [[Cribl]], [[Oso]], [[Apollo Research]], [[Cerbos]].

## 🧠 First Principles & Mental Models

- **[[Least Privilege]]**: Deny-by-default log access with identity-scoped grants directly instantiates least privilege — no agent or admin can access more than their explicit grant allows, and every grant is auditable.
- **[[Defense in Depth]]**: Pre-request guardrails (PII scrubbing, tool-call authorization) combined with post-request logging create two independent control layers — one prevents bad data from leaving, the other preserves evidence if something slips through.

## 🃏 Review Questions

**Q1**: What is the core capability that Aperture provides for AI agent oversight?
**A**: Aperture proxies AI agent requests through Tailscale's network, attaching cryptographic identity to every call and enforcing deny-by-default access controls and pre-request guardrail policies before data reaches model providers.

**Q2**: How does Aperture handle identity for non-human agents like CI runners?
**A**: Non-human agents are identified by their Tailscale tags (e.g., `tag:ci-runner`) rather than a login name, allowing policy and access grants to be scoped to automated workload identities without user accounts.

**Q3**: What is the practical implication of the "fail closed vs. fail open" configuration for guardrails?
**A**: If the guardrail service becomes unreachable, operators must choose between blocking all agent requests (fail closed, maximizing safety) or allowing them through unfiltered (fail open, maximizing availability) — a tradeoff that must be made explicit per service.

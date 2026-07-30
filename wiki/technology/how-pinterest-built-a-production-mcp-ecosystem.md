---
type: literature-note
source_url: https://blog.bytebytego.com/p/how-pinterest-built-a-production
author: Unknown
tags: [mcp, pinterest, authorization, platform-engineering]
date_consumed: 2026-07-29
---

## Summary

[[Pinterest]] built a production [[Model Context Protocol|MCP]] ecosystem around three architectural bets — cloud-hosted (not local) servers, many small domain-specific servers instead of one monolith, and a unified deployment pipeline — combined with a two-layer authorization model ([[Envoy]] network-edge checks plus per-tool decorator checks) and a central registry acting as governance backbone. MCP tools are embedded directly into engineers' existing surfaces (chat, IDEs, CLI, internal bots) rather than living in a separate interface. By January 2025 the ecosystem handled 66,000 invocations per month across 844 users, saving an estimated 7,000 hours per month.

## Core Concepts

- [[Model Context Protocol]] (MCP) — open standard turning an N×M integration problem into an N+M problem
- [[Pinterest]] — built cloud-hosted, domain-specific MCP servers with a central registry
- [[MCP Registry]] — source of truth for which servers exist, who owns them, and how to connect
- [[Envoy]] — network proxy performing coarse-grained, network-edge JWT validation and access policy
- [[OAuth]] and [[JWT]] — used for the Layer 1 human-user authentication flow
- [[SPIFFE]] — cryptographic service identity used for low-risk, read-only service-to-service calls
- [[Human-in-the-Loop]] — mandated approval before sensitive or expensive agent actions
- [[Elicitation]] — explicit user confirmation required before dangerous operations like overwriting data
- [[Presto]], [[Spark]], [[Airflow]] — internal systems wrapped by Pinterest's highest-traffic MCP servers

## Key Takeaways

- MCP turns an N×M integration problem into a simpler N+M problem
- Pinterest chose cloud-hosted servers for consistent auth, logging, and monitoring
- Many small domain servers keep tool lists short and access-scoped
- A unified deployment pipeline removed multi-day boilerplate per new server
- The registry is the governance backbone — only registered servers are approved
- Layer 1 (Envoy/JWT) performs coarse, network-edge authorization checks
- Layer 2 (tool-level decorators) performs fine-grained, per-tool authorization
- Elicitation forces explicit user confirmation before dangerous operations
- Ecosystem reached 66,000 invocations/month, ~7,000 hours saved (Jan 2025)

## 🧠 First Principles & Mental Models

- **[[Defense in Depth]]**: Pinterest's two authorization layers exist so that a misconfiguration in one (Envoy's network policy or the per-tool decorator) is still caught by the other, rather than relying on any single control point.

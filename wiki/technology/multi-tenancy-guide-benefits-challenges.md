---
type: literature-note
source_url: https://blog.bytebytego.com/p/a-guide-to-multi-tenancy
author: ByteByteGo
tags: [multi-tenancy, saas-architecture, system-design, isolation]
date_consumed: 2026-07-27
---

## Summary

[[ByteByteGo]] surveys multi-tenancy architecture — its benefits (cost sharing, operational simplicity, faster feature delivery) and its core challenges (noisy neighbor problem, blast radius, tenant context leakage). Three data isolation models are compared from weakest to strongest: shared schema with tenant column, separate schemas, and separate databases. Single-tenancy becomes preferable for large enterprise customers with compliance or customization requirements.

## Core Concepts

- **[[Multi-Tenancy]]** — single application instance serving multiple customers with isolated data and configurations
- **[[Noisy Neighbor Problem]]** — one tenant's heavy usage degrading performance for others on shared infrastructure
- **[[Blast Radius]]** — scope of damage from a bug, misconfiguration, or security incident in a shared system
- **[[Tenant Context]]** — tenant identity that must flow through every layer of a request: routing, data access, logging, billing
- **[[Data Isolation Models]]** — shared schema → separate schemas → separate databases (weakest to strongest isolation)

## Key Takeaways

- **Cost sharing**: multi-tenancy reduces infrastructure cost per tenant; right for B2B SaaS
- **Noisy neighbor**: requires rate limiting and fair-use quotas to prevent cross-tenant degradation
- **Blast radius**: shared infrastructure means a single bug can affect all tenants simultaneously
- **Tenant context leak**: failing to carry tenant identity through the full request is a security and compliance risk
- **When to use single-tenancy**: large enterprise customers with compliance, data residency, or heavy customization needs

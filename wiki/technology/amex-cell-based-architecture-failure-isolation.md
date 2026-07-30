---
type: literature-note
source_url: https://techscoop.substack.com/p/how-amex-designs-for-low-latency
author: Hey Maria
tags: [cell-based-architecture, payments-infrastructure, failure-isolation, resilience]
date_consumed: 2026-07-29
---

## Summary
American Express's payments platform is built as independent [[Cell-Based Architecture]] units, each with its own services, databases, and observability, so a failure in one cell cannot cascade to others. A thin [[Global Transaction Router]] (GTR) handles routing, failover, and migration without owning payment logic itself, keeping the critical path resilient to logging, config, and downstream outages. The design treats resiliency as a boundary problem — deciding in advance where failure stops, where state lives, and which transactions can safely be restarted.

## Core Concepts
- **[[Cell-Based Architecture]]** — isolated, independently deployable units containing all services/data needed to process a subset of transactions; the bulkhead principle applied to payments.
- **[[Global Transaction Router]] (GTR)** — the sole ingress/egress control point; stays deliberately thin and avoids becoming a dependency-heavy orchestrator.
- **[[Blast Radius]]** — reducing it is the primary goal of cell isolation; measured across transactions, partners, merchants, and recovery surface area, not just uptime percentage.
- **[[Static Stability]]** — the data plane keeps processing even if the control plane (logging, config) degrades.
- **[[Idempotency]]** — stable transaction IDs let failed transactions restart safely in another cell without duplicate charges; referenced via Stripe's idempotency-key pattern.
- **Point of no return** — the moment before external issuer submission after which a transaction cannot be safely rerouted.
- Cell-based design doubles as a **canary deployment strategy** — Amex used the GTR to shadow-test and gradually migrate traffic to a new platform.

## Key Takeaways
- Failure boundaries should be a first-class architectural primitive, not retries bolted on after.
- Keep dynamic state routing deterministic; don't replicate everything everywhere.
- Cells must not talk to each other directly — all traffic flows through the router.
- Observability should publish locally first, aggregate globally second, so telemetry failure doesn't stop processing.
- Real outages (Visa 2018, Square 2023/2025) were caused by ordinary failures — DNS, certs, routing — not exotic ones.
- Duplication across cells is often the acceptable cost of true isolation.

## 🧠 First Principles & Mental Models
- **[[Bulkhead Principle]]**: dividing a ship into watertight compartments so damage in one section doesn't sink the vessel — directly mirrors why cells must not share synchronous dependencies in the critical path.

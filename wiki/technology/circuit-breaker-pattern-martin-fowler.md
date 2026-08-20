---
type: literature-note
source_url: https://martinfowler.com/bliki/CircuitBreaker.html
author: Martin Fowler
tags: [circuit-breaker, distributed-systems, resilience, microservices]
date_consumed: 2026-08-20
---

## Summary
The Circuit Breaker pattern, popularized by Michael Nygard in *Release It*, wraps remote calls in a stateful object that trips open when failures exceed a threshold, preventing cascading failures by fast-failing instead of letting calls hang. It cycles through three states — Closed, Open, and Half-Open — to give downstream systems time to recover while shielding callers from resource exhaustion. Monitoring state transitions and pairing with thread-pool isolation makes the pattern a foundational building block of resilient [[Distributed Systems]].

## Core Concepts
- **[[Circuit Breaker Pattern]]**: wraps a protected call; trips open on failure threshold breach, then probes recovery via a Half-Open trial call
- **Three states**: Closed (normal, failures counted) → Open (fail-fast, no calls through) → Half-Open (one trial call) → back to Closed or Open
- **[[Cascading Failures]]**: slow or hanging remote calls exhaust threads/connections and propagate failure upstream; the breaker prevents this
- **[[Resilience4j]]** / **[[Hystrix]]**: reference implementations combining circuit breaking with thread-pool isolation and metrics; Hystrix in maintenance, Resilience4j is current successor
- **Fallback strategies**: stale cache, default response, queued retry, or degraded UI when the circuit is open
- **Frequency-based tripping**: count failures per time window (e.g., 5 in 60 s) rather than absolute counts to react faster to sudden spikes
- **[[Thread Pool Isolation]]**: separate pools per downstream dependency; combine with circuit breakers for defense in depth

## Key Takeaways
- **Fail fast**: Open circuit returns errors immediately, preventing thread/connection exhaustion.
- **Self-healing**: Half-Open state probes recovery without fully reopening the floodgates.
- **Observability**: State-change alerts make hidden upstream failures visible and actionable.
- **Threshold design**: Use time-windowed counts, not bare totals, for responsive tripping.
- **Fallbacks required**: Callers must handle open-circuit errors gracefully with a defined fallback.
- **Async coverage**: Pattern extends to message queues — monitor queue depth as a trip signal.
- **Defense in depth**: Thread-pool isolation + circuit breakers together prevent a single slow dependency from saturating the whole service.

## 🧠 First Principles & Mental Models
**Fail-Fast Principle**: systems should detect and surface failure immediately rather than wait, preserving resources for healthy paths. The circuit breaker operationalizes this for remote calls by converting unbounded waits into bounded, fast errors.

## 🃏 Review Questions

**Q1**: What problem does the Circuit Breaker pattern solve?
**A**: Remote calls can hang indefinitely, consuming threads and connections; the breaker trips open on repeated failure, fast-failing subsequent calls and preventing cascading resource exhaustion.

**Q2**: Describe the Half-Open state and its purpose.
**A**: After the reset timeout expires in the Open state, one trial call is allowed through; success transitions back to Closed, failure returns to Open — allowing gradual, tested recovery.

**Q3**: Why use frequency-based (time-windowed) failure counts rather than absolute counts?
**A**: Absolute counts react slowly to sudden failure spikes; windowed counts (e.g., 5 failures in 60 s) give a more responsive and accurate signal of current upstream health.

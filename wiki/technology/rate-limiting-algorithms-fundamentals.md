---
type: literature-note
source_url: https://blog.bytebytego.com/p/rate-limiting-fundamentals
author: Alex Xu
tags: [rate-limiting, api-design, system-design, distributed-systems]
date_consumed: 2026-08-20
---

## Summary
Rate limiting controls how frequently users or services can access a resource within a defined time window, throttling or blocking requests that exceed a threshold. It is a foundational technique for building resilient, fair, and cost-effective APIs by preventing resource starvation, cost overruns, and server overload. Five core algorithms offer different tradeoffs between accuracy, memory usage, and burst tolerance.

## Core Concepts
- **Limit**: maximum requests allowed in a time window (e.g., 100 req/min)
- **Window**: the time period the limit applies to; window design drives fairness and accuracy — see [[Fixed Window Counter]], [[Sliding Window Counter]]
- **Identifier**: the unique attribute distinguishing callers — user ID, API key, or IP address; can be composed per-user per-endpoint
- **Response types**: blocking (HTTP 429), throttling (artificial delay), or shaping (lower priority queue)
- **[[Token Bucket]]**: tokens refill at a steady rate up to a max capacity; each request consumes one token — allows bursting within capacity
- **[[Leaky Bucket]]**: requests queue and drain at a fixed output rate; excess requests are dropped — enforces smooth output
- **[[Fixed Window Counter]]**: divide time into discrete windows; counter resets at window boundary — vulnerable to boundary attacks
- **[[Sliding Window Log]]**: maintain timestamped request log; count entries within the past window duration — precise but memory-intensive
- **[[Sliding Window Counter]]**: hybrid approximation using current and previous window counts weighted by position — balanced tradeoff

## Key Takeaways
- **Boundary attack**: Fixed Window allows ~2x the limit across adjacent window boundaries
- **Memory cost**: Sliding Window Log stores every timestamp; impractical at high scale
- **Burst support**: Token Bucket is the only algorithm that natively accommodates legitimate traffic bursts
- **Smooth output**: Leaky Bucket enforces the most consistent rate but adds queuing latency
- **Hybrid wins**: Sliding Window Counter balances accuracy and memory better than either pure approach
- **Identifiers compose**: combine user ID + endpoint for fine-grained quota enforcement
- **Error signaling**: pair with HTTP 429 + `Retry-After` header and client-side exponential backoff

## 🧠 First Principles & Mental Models
- **Leaky bucket analogy**: water (requests) pours in at any rate but drains at a fixed rate — overflow is dropped
- **Token bucket analogy**: tokens accumulate over time; spending tokens buys capacity to burst without violating the average rate

## 🃏 Review Questions

**Q1**: What is the boundary attack vulnerability in the Fixed Window Counter?
**A**: A burst at the end of one window and the start of the next can allow up to 2x the intended limit within a short span, because both windows reset independently.

**Q2**: How does the Sliding Window Counter approximate an exact sliding window with low memory?
**A**: It weights the previous fixed window's count by the fraction of that window still within the current sliding window, then adds the current window's count — no per-request log needed.

**Q3**: When should you choose Token Bucket over Leaky Bucket?
**A**: Choose Token Bucket when legitimate clients need burst capacity (e.g., occasional spikes above average rate); choose Leaky Bucket when downstream systems require a strictly smooth, predictable request rate.

---
source_url: https://blog.bytebytego.com/p/rate-limiting-fundamentals
author: Alex Xu
date: 2023-05-31
---

# Rate Limiting Fundamentals

Rate limiting controls how frequently users or services can access a resource within a defined time window. When requests exceed a defined threshold, they are throttled or blocked. It is a foundational technique for building resilient, fair, and cost-effective APIs and services.

## Why Rate Limiting Matters

- **Prevents resource starvation from DoS attacks** — limits damage from both malicious and accidental traffic floods
- **Reduces cost overruns** — especially critical with paid third-party APIs (e.g., LLM APIs) where each request has a direct cost
- **Prevents server overload** — ensures equitable resource sharing among clients
- **Enforces business policies** — free vs. paid tier limits, per-user quotas

## Core Concepts

**Limit:** The maximum number of allowable requests in a given time span (e.g., 100 requests per minute).

**Window:** The time period during which the limit applies. Window design significantly affects fairness and accuracy.

**Identifier:** A unique attribute distinguishing callers — typically user ID, API key, or IP address. Can be combined (e.g., per-user per-endpoint).

## Response Types

| Response | Behavior |
|---|---|
| Blocking | Deny excess requests immediately (HTTP 429 Too Many Requests) |
| Throttling | Slow down requests beyond the limit; add artificial delay |
| Shaping | Allow excess requests but assign them lower priority in processing queues |

## Common Algorithms

### Fixed Window Counter

Divide time into fixed windows (e.g., each minute). A counter increments per request until it hits the threshold; further requests are blocked until the next window opens.

**Pros:** Simple to implement, low memory usage.

**Cons:** Boundary attack — a burst of requests at the end of one window and the start of the next can double the effective rate. Two back-to-back windows can allow 2x the limit in a short period.

### Sliding Window Log

Maintain a timestamped log of requests per identifier. For each new request, count logs within the last window duration. Discard logs older than the window.

**Pros:** Precisely accurate — no boundary attack.

**Cons:** High memory usage (stores every request timestamp).

### Sliding Window Counter

Hybrid of Fixed Window and Sliding Window Log. Approximate the sliding window using the current fixed window count and a weighted fraction of the previous window count.

**Pros:** More accurate than Fixed Window, far lower memory than Sliding Window Log.

**Cons:** Approximate (not exact), more complex to implement.

### Token Bucket

Tokens accumulate in a bucket at a steady refill rate up to a maximum capacity. Each request consumes one token. If the bucket is empty, the request is denied or queued.

**Pros:** Allows bursting up to bucket capacity while enforcing average rate.

**Cons:** Slightly more complex; requires per-client state tracking.

### Leaky Bucket

Requests enter a queue (bucket) and are processed at a fixed rate. If the queue is full, excess requests are dropped.

**Pros:** Enforces a very smooth, consistent output rate.

**Cons:** Doesn't accommodate legitimate bursts well; adds queuing latency.

## Choosing an Algorithm

| Use case | Recommended algorithm |
|---|---|
| Simple API protection | Fixed Window Counter |
| Strict accuracy required | Sliding Window Log |
| Balance accuracy and memory | Sliding Window Counter |
| Allow legitimate bursts | Token Bucket |
| Smooth rate enforcement | Leaky Bucket |

Rate limiting is most effective when combined with clear error responses (HTTP 429 with `Retry-After` header), client-side backoff, and monitoring dashboards tracking throttle rates per client.

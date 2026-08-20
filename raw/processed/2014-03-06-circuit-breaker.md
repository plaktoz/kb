---
source_url: https://martinfowler.com/bliki/CircuitBreaker.html
author: Martin Fowler
date: 2014-03-06
---

# Circuit Breaker

Remote calls differ fundamentally from in-memory calls because they can fail or hang indefinitely. A hanging remote call can consume threads and connections while waiting, potentially causing cascading failures that bring down an entire system. Michael Nygard popularized the Circuit Breaker pattern in *Release It* to address this problem.

## Core Concept

Wrap a protected function call in a circuit breaker object that monitors for failures. Once failures reach a configurable threshold, the circuit breaker "trips" and all further calls return an error immediately — without attempting to execute the protected call. This gives the failing system time to recover while preventing resource exhaustion in the caller.

## Three States

**Closed (normal operation)**
- All calls pass through to the protected function
- Failures are counted
- When failure count exceeds threshold, transition to Open

**Open (failing fast)**
- All calls fail immediately with an error
- No calls reach the protected function
- After a reset timeout, transition to Half-Open

**Half-Open (testing recovery)**
- One trial call is allowed through to test the protected function
- If the trial call succeeds: transition back to Closed
- If the trial call fails: transition back to Open

## Implementation Notes

A basic circuit breaker tracks a failure count and threshold. A more robust self-resetting version tracks `last_failure_time` and automatically enters Half-Open state after a `reset_timeout` period:

```ruby
# Pseudocode for self-resetting circuit breaker
def call(protected_function)
  if state == :open
    if Time.now - @last_failure_time > @reset_timeout
      # Allow trial call (half-open)
      attempt_reset(protected_function)
    else
      raise CircuitOpenError
    end
  else
    # state == :closed
    begin
      result = protected_function.call
      reset_count
      result
    rescue => e
      record_failure
      raise e
    end
  end
end
```

## Key Considerations

**Monitoring:** Circuit breaker state changes should trigger alerts. The pattern makes hidden failures visible — a circuit that is frequently open indicates a persistent upstream problem.

**Thread pools:** Use separate thread pools per downstream dependency to prevent a slow service from consuming all available threads. Combine with circuit breakers for defense in depth.

**Frequency-based tripping:** Count failures per time window (e.g., 5 failures in 60 seconds), not just absolute counts. Pure count-based thresholds can be too slow to react to sudden failure spikes.

**Fallback strategies:** When a circuit is open, callers need a fallback:
- Return cached/stale data
- Return a default response
- Queue the request for later retry
- Show a degraded UI

**Async communication:** Circuit breakers apply to async systems too. For message queues, monitor queue depth — a growing queue indicates the consumer is falling behind and may warrant tripping a breaker.

## Reference Implementation

Netflix's open-source **Hystrix** library (now in maintenance mode; Resilience4j is the current successor) implements circuit breaking combined with thread pool isolation, request collapsing, and metrics dashboards.

The pattern is foundational to building resilient distributed systems and is a key component of the microservices resilience toolkit.

---
type: literature-note
source_url: https://www.baeldung.com/java-concurrency
author: Baeldung
tags: [java, concurrency, multithreading, executorservice]
date_consumed: 2026-07-27
---

## Summary

The Baeldung Java Concurrency Series is a reference index of guides covering Java's multi-threading and concurrency APIs, organized into basics and advanced topics. It spans core synchronization primitives (`synchronized`, `volatile`), thread lifecycle management, the `java.util.concurrent` framework, and advanced patterns like `CompletableFuture`, Fork/Join, and thread-safety. The series serves as a structured map of Java's concurrency landscape.

## Core Concepts

- **[[Java Concurrency]]**: Managing simultaneous execution of threads in a Java application; requires explicit coordination to prevent data races and inconsistent state.
- **[[synchronized Keyword]]**: Intrinsic locking mechanism for mutual exclusion on methods or code blocks.
- **[[volatile Keyword]]**: Ensures visibility of variable changes across threads without mutual exclusion — lighter than `synchronized`.
- **[[ExecutorService]]**: Thread pool abstraction in `java.util.concurrent`; decouples task submission from thread management.
- **[[CompletableFuture]]**: Composable async programming API in Java 8+; supports chaining, combining, and exception handling of async operations.
- **[[Fork/Join Framework]]**: Work-stealing framework for divide-and-conquer parallelism; uses `ForkJoinPool`.
- **[[ThreadLocal]]**: Per-thread variable storage — each thread has its own independent copy of the variable.
- **[[CountDownLatch]]**: Synchronization aid allowing one or more threads to wait until a set of operations completes.
- **[[CyclicBarrier]]**: Synchronization point where a fixed number of threads must all arrive before any proceed.
- **[[Thread Safety]]**: Property of code that behaves correctly when accessed by multiple threads concurrently.
- **[[Runnable vs Callable]]**: `Runnable` returns void; `Callable` returns a result and can throw checked exceptions.

## Key Takeaways

- `synchronized` provides mutual exclusion; `volatile` provides visibility — they solve different problems.
- Use `ExecutorService` instead of raw `Thread` management in production code.
- `CompletableFuture` is the standard tool for non-blocking async pipelines in modern Java.
- `ThreadLocal` is useful for per-request context (e.g., security context, DB transactions) — be careful with thread pool reuse.
- `CountDownLatch` is one-shot; `CyclicBarrier` is reusable — use accordingly.
- Use `wait()`/`notify()` only when `java.util.concurrent` primitives don't fit the use case.
- Capture thread dumps for production debugging; use JVM flags or `jstack`.
- Parallel streams use a shared `ForkJoinPool.commonPool()` — customize with a dedicated pool for heavy workloads.

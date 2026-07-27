---
type: literature-note
source_url: https://www.baeldung.com/jvm-garbage-collectors
author: Baeldung
tags: [java, jvm, garbage-collection, performance]
date_consumed: 2026-07-27
---

## Summary

JVM Garbage Collection (GC) automatically manages heap memory using a Mark-and-Sweep cycle — identifying live objects, then removing unreachable ones. The JVM ships four main GC implementations: Serial, Parallel, G1, and ZGC, each optimizing for different trade-offs between throughput, latency, and heap size. ZGC, production-ready since Java 15, achieves sub-10ms pause times regardless of heap size by performing most work concurrently with application threads.

## Core Concepts

- **[[Garbage Collection]]**: Automatic memory management in the JVM — tracks and removes unreachable objects from the heap.
- **[[Mark and Sweep]]**: Two-phase GC algorithm: Mark (identify live objects), Sweep (remove unreachable ones).
- **[[Serial GC]]**: Single-threaded; stops all application threads (stop-the-world); suitable only for single-threaded client apps. Flag: `-XX:+UseSerialGC`.
- **[[Parallel GC]]**: Multi-threaded; default in Java 5–8 (Throughput Collector); still stop-the-world but faster on multicore. Flag: `-XX:+UseParallelGC`.
- **[[G1 GC]]** (Garbage First): Partitions heap into equal-size regions; concurrent marking phase; collects regions with most garbage first. Default since Java 9. Flag: `-XX:+UseG1GC`.
- **[[ZGC]]** (Z Garbage Collector): Low-latency GC; concurrent operation with <10ms pauses; handles 8MB–16TB heaps; uses colored pointers (load barriers) to track object state. Production-ready from Java 15. Flag: `-XX:+UseZGC`.
- **[[Colored Pointers]]**: ZGC's mechanism for tracking heap object state using metadata bits in reference pointers, enabling concurrent GC work without stop-the-world pauses.
- **[[String Deduplication]]**: Java 8u20 feature (`-XX:+UseStringDeduplication`) that collapses duplicate String values to a shared `char[]`, reducing heap usage.

## Key Takeaways

- GC trades CPU overhead and non-deterministic scheduling for freedom from manual memory management.
- Serial GC: simplest; freezes all threads; avoid in server/multi-threaded contexts.
- Parallel GC: multicore throughput focus; still stop-the-world; was JVM default through Java 8.
- G1 GC: concurrent marking; predictable pause goals; default since Java 9.
- ZGC: <10ms pauses at any heap size; scales from 8MB to 16TB; must be explicitly enabled.
- Tune Parallel GC with: `-XX:ParallelGCThreads`, `-XX:MaxGCPauseMillis`, `-XX:GCTimeRatio`, `-Xmx`.
- String deduplication (`-XX:+UseStringDeduplication`) can meaningfully reduce heap in string-heavy apps.

## 🧠 First Principles & Mental Models

- **[[Latency vs. Throughput Trade-off]]**: Each GC algorithm embodies a different point on the latency-throughput curve — Serial maximizes simplicity, Parallel maximizes throughput, ZGC minimizes latency — choosing wrong GC is a common source of invisible performance problems.

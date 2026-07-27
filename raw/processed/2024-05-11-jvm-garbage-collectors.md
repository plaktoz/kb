# JVM Garbage Collectors

source_url: https://www.baeldung.com/jvm-garbage-collectors

---

By Baeldung | Last updated: May 11, 2024

## 1. Overview

Garbage Collection (GC) in the JVM tracks every object in heap space and removes unused ones. It works in two steps:
- **Mark**: Identifies which memory is in use and which isn't.
- **Sweep**: Removes objects identified in the mark phase.

**Advantages**: No manual memory management, no dangling pointer handling, automatic memory leak management.

**Disadvantages**: Extra CPU overhead, no programmer control over GC scheduling, potential application pauses, less efficient than manual allocation in some cases.

## 2. GC Implementations

### 2.1 Serial Garbage Collector
Simplest GC; works with a single thread. **Freezes all application threads** when running. Not suitable for multi-threaded server environments. Good for single-threaded client applications with no pause time requirements.

```bash
java -XX:+UseSerialGC -jar Application.java
```

### 2.2 Parallel Garbage Collector
Default GC from Java 5 through Java 8 (also called Throughput Collector). Uses **multiple threads** for heap management but still freezes application threads during GC.

Tuning options:
- `-XX:ParallelGCThreads=<n>` — number of GC threads
- `-XX:MaxGCPauseMillis=<ms>` — maximum pause time goal
- `-XX:GCTimeRatio=<n>` — ratio of GC time vs. application time
- `-Xmx<size>` — maximum heap footprint

```bash
java -XX:+UseParallelGC -jar Application.java
```

### 2.3 G1 Garbage Collector (Garbage First)
Designed for multi-processor machines with large memory. Available from JDK 7 Update 4. Partitions heap into equal-sized regions and performs a **concurrent global marking phase** to identify object liveness, then collects regions with the most free space first.

```bash
java -XX:+UseG1GC -jar Application.java
```

### 2.4 Java 8 String Deduplication
Java 8u20 introduced `-XX:+UseStringDeduplication` to reduce memory by removing duplicate String values into a global `char[]` array.

### 2.5 Z Garbage Collector (ZGC)
Introduced in Java 11 (Linux), Windows/macOS in Java 14, production-ready in Java 15. Key properties:
- Stops application threads for **less than 10ms**.
- Uses **colored pointers** (load barriers with metadata bits) to track heap state concurrently.
- Handles heaps from **8MB to 16TB**.
- Pause times do **not** scale with heap or live-set size.
- Partitions the heap like G1, but regions can have different sizes.

```bash
# Java 15+
java -XX:+UseZGC Application.java

# Java 11-14
java -XX:+UnlockExperimentalVMOptions -XX:+UseZGC Application.java
```

ZGC is not the default GC; must be explicitly enabled.

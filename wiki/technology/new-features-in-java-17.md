---
type: literature-note
source_url: https://www.baeldung.com/java-17-new-features
author: Baeldung
tags: [java, java-17, lts, jep]
date_consumed: 2026-07-27
---

## Summary

Java 17, released September 2021, is an LTS release bringing 14 JEPs including sealed classes (final), pattern matching for switch (preview), a new macOS Metal rendering pipeline, Foreign Function & Memory API (incubator), and the removal of experimental AOT/JIT compilers. It also formalized a new 6-month release cadence and reduced the LTS interval from 3 years to 2 years (targeting Java 21 as the next LTS). Oracle JDK 17+ is available under no-fee terms for most use cases.

## Core Concepts

- **[[Sealed Classes]]** (JEP 409): Restrict which classes/interfaces may extend or implement a type — enables exhaustive pattern matching and expressive type hierarchies.
- **[[Pattern Matching for Switch]]** (JEP 406, Preview): Type patterns in `switch` expressions/statements, reducing cast-and-act boilerplate.
- **[[Foreign Function and Memory API]]** (JEP 412, Incubator): Access native code and off-heap memory from Java without JNI; part of [[Project Panama]].
- **[[Vector API]]** (JEP 414, 2nd Incubator): SIMD-style operations leveraging CPU vector instructions; useful for scientific/image processing workloads.
- **[[ZGC]]** production-ready since Java 15; Java 17 continues improvements.
- **[[JEP 403]] – Strong JDK Encapsulation**: Removes `--illegal-access` flag; internal APIs inaccessible except `sun.misc.Unsafe`.
- **[[JEP 306]] – Strict Floating-Point**: All operations are `strictfp` by default; keyword no longer needed.
- **[[JEP 356]] – Enhanced PRNG**: New `RandomGenerator` interface; `Random`, `SplittableRandom`, `SecureRandom` now extend it.
- **[[LTS Release Model]]**: LTS cadence reduced from 3 years to 2 years; Java 21 was the next LTS (Sept 2023).
- **[[Context-Specific Deserialization Filters]]** (JEP 415): Per-operation deserialization filters at JVM level to block malicious serialized data.

## Key Takeaways

- Sealed classes finalized in Java 17 — use `permits` clause to enumerate allowed subclasses.
- Pattern matching for switch is preview only in Java 17; finalized in Java 21.
- `--illegal-access` flag removed — migrating from Java 8 to 17 may require explicit `--add-opens`.
- RMI Activation and experimental GraalVM AOT/JIT compilers removed.
- Applet API deprecated for removal; Security Manager deprecated for removal.
- `strictfp` keyword now a no-op — remove from existing code without behavior change.
- Oracle JDK free for production under new no-fee license (with some exceptions — read terms).
- LTS interval: Java 11 → Java 17 (3 years); Java 17 → Java 21 (2 years); trend toward shorter cycles.

## 🧠 First Principles & Mental Models

- **[[Algebraic Data Types]]**: Sealed classes + pattern matching bring Java closer to sum types (algebraic data types) common in functional languages — enabling the compiler to enforce exhaustiveness and eliminate entire classes of runtime errors.

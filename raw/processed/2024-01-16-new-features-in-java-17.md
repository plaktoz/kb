# New Features in Java 17

source_url: https://www.baeldung.com/java-17-new-features

---

By Baeldung | Last updated: January 16, 2024

Java SE 17 (released September 2021) is an LTS release. Key JEPs:

## JEPs

### JEP 306 – Restore Always-Strict Floating-Point Semantics
Makes all floating-point operations consistently strict (`strictfp`), as they were before Java 1.2. The `strictfp` keyword is no longer necessary.

### JEP 356 – Enhanced Pseudo-Random Number Generators
New interfaces and implementations for PRNGs. Enables interchangeable algorithms and stream-based programming. Legacy classes (`Random`, `SplittableRandom`, `SecureRandom`) now extend the new `RandomGenerator` interface.

### JEP 382 – New macOS Rendering Pipeline
New Java 2D rendering pipeline for macOS using Apple Metal API, replacing deprecated OpenGL (deprecated in macOS 10.14). No public API changes.

### JEP 391 – macOS/AArch64 Port
JDK ported to run on Apple Silicon (AArch64 architecture).

### JEP 398 – Deprecate Applet API for Removal
Applet API marked for removal; already deprecated since Java 9.

### JEP 403 – Strongly Encapsulate JDK Internals
Removes `--illegal-access` flag. JDK users can no longer access internal APIs except critical ones like `sun.misc.Unsafe`.

### JEP 406 – Pattern Matching for Switch (Preview)
Enhances switch expressions/statements with type patterns, reducing boilerplate:
```java
return switch (obj) {
    case Human h -> "Name: %s".formatted(h.name());
    case Circle c -> "This is a circle";
    case null -> "It is null";
    default -> "It is an object";
};
```

### JEP 407 – Remove RMI Activation
RMI Activation API removed (deprecated in Java 15).

### JEP 409 – Sealed Classes (Final)
Sealed classes restrict which classes/interfaces may extend or implement them. Enables exhaustive pattern matching:
```java
int getNumberOfSides(Shape shape) {
    return switch (shape) {
        case Circle c -> c.getNumberOfSides();
        case Triangle t -> t.getNumberOfSides();
        case Rectangle r -> r.getNumberOfSides();
    };
}
```

### JEP 410 – Remove Experimental AOT and JIT Compiler
GraalVM-based AOT (JEP 295) and JIT (JEP 317) compilers removed from JDK due to low adoption and high maintenance cost. Still available via GraalVM directly.

### JEP 411 – Deprecate Security Manager for Removal
Security Manager deprecated; no longer relevant for its original purpose of securing client-side Java.

### JEP 412 – Foreign Function and Memory API (Incubator)
Allows Java code to access code outside the JVM and manage off-heap memory. Intended to replace JNI with improved security and performance.

### JEP 414 – Vector API (Second Incubator)
API for SIMD (Single Instruction, Multiple Data) operations leveraging specialized CPU vector instructions. Useful for scientific, image processing, and arithmetic-heavy applications.

### JEP 415 – Context-Specific Deserialization Filters
Allows applications to configure dynamic, context-specific deserialization filters at the JVM level to protect against deserialization attacks.

## LTS and Release Process Changes

- Java moved to a **six-month feature release cadence** since Java 10.
- LTS versions get extended support (8 years from Oracle).
- LTS cadence reduced from 3 years to **2 years** starting with Java 17 → Java 21.
- Stabilization process: fork → 3-month stabilization (RDP1 + RDP2 + RC) → General Availability.
- Oracle JDK now available under **no-fee terms** for most use cases.

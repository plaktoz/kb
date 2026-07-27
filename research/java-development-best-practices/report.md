# Research: Java Development Best Practices
*Generated: 2026-07-27 | Scope: Comprehensive Java development best practices reference guide covering code style, design patterns, testing, performance, security, and modern Java conventions*

## Research Outline

1. Code style, readability, and project structure
2. Design patterns and OOP principles
3. Testing best practices
4. Performance and JVM tuning
5. Security and dependency management

---

## Code Style, Readability, and Project Structure

### Google Java Style Guide

- **Source**: https://google.github.io/styleguide/javaguide.html
- **Summary**: The Google Java Style Guide is the most widely referenced Java style standard. It mandates 2-space indentation, 100-character line limits, K&R braces, no wildcard imports, and strict naming conventions (UpperCamelCase for classes, lowerCamelCase for methods/fields, UPPER_SNAKE_CASE for constants). It prohibits prefixes/suffixes like `mName` or `s_name`, requires `@Override` usage, and bans silent exception swallowing.
- **Relevance**: The canonical reference for Java style in professional and open-source projects; establishing this foundation prevents a large class of code review issues.

### Baeldung: Clean Code Principles for Java

- **Source**: https://www.baeldung.com/java-clean-code
- **Summary**: Covers clean code as any code "a developer can read and change easily." Recommends following Maven's `src/main/java` / `src/test/java` layout, naming classes with nouns and methods with verbs, limiting method parameters to three or fewer, replacing magic values with constants or enums, and using static analysis tools (SonarQube, Checkstyle, PMD, SpotBugs) to enforce conventions automatically. Incorporates SOLID, DRY, and KISS at the practice level.
- **Relevance**: Bridges abstract principles (SOLID, DRY) to concrete day-to-day Java coding habits, making it ideal as a reference for code reviews.

---

## Design Patterns and OOP Principles

### Baeldung: SOLID Principles in Java

- **Source**: https://www.baeldung.com/solid-principles
- **Summary**: Explains all five SOLID principles with Java examples. Single Responsibility: one class, one reason to change. Open/Closed: extend via subclasses, don't modify working code. Liskov Substitution: subtypes must honor their parent's contract. Interface Segregation: split large interfaces into focused ones. Dependency Inversion: depend on abstractions (interfaces), not concrete implementations — enables both testability and flexibility.
- **Relevance**: SOLID is the foundational OOP design philosophy for modern Java; violations are the root cause of most maintainability and testability problems.

### Baeldung: Java Design Patterns Series

- **Source**: https://www.baeldung.com/design-patterns-series
- **Summary**: Catalogs the full GoF pattern set across three categories — Creational (Builder, Factory, Singleton, Abstract Factory), Structural (Proxy, Adapter, Decorator, Composite, Facade, Flyweight, Bridge, DAO), and Behavioral (Strategy, Observer, Command, Template Method, Chain of Responsibility, State, Visitor, Mediator, Memento). Also covers enterprise patterns (DTO, Saga, Service Locator, Gateway) and Spring-specific applications.
- **Relevance**: Provides a structured map of reusable design solutions; knowing when to apply each pattern separates junior from senior Java developers.

---

## Testing Best Practices

### Baeldung: Java Unit Testing Best Practices

- **Source**: https://www.baeldung.com/java-unit-testing-best-practices
- **Summary**: Key practices include: mirroring production package structure in test directories, using `given_when_then` test naming, structuring each test as setup → action → assertion, testing one scenario per test method, hard-coding expected values (never duplicating production logic in tests), mocking external dependencies with Mockito or EasyMock, using `@Before`/`@After` for shared setup, targeting ~80% code coverage with JaCoCo or Cobertura, and automating test execution in CI/CD pipelines.
- **Relevance**: Covers the full spectrum of unit testing practice from naming to coverage to tooling, making it the core reference for any Java testing strategy.

---

## Performance and JVM Tuning

### Baeldung: JVM Garbage Collectors

- **Source**: https://www.baeldung.com/jvm-garbage-collectors
- **Summary**: Describes four main GC algorithms. Serial GC: single-threaded, freezes all app threads — for simple/small apps. Parallel GC (default Java 5–8): multi-threaded but still stop-the-world — best for throughput-focused batch workloads. G1 GC: region-based, large-heap multi-processor environments — balances throughput and latency. ZGC: concurrent, max ~10ms pauses, heaps from 8MB to 16TB, production-ready since Java 15 — for latency-sensitive services. Each is enabled via a specific JVM flag (`-XX:+UseZGC`, etc.).
- **Relevance**: GC choice is one of the highest-impact JVM tuning decisions; understanding trade-offs prevents performance regressions when deploying to production.

### Baeldung: Java Concurrency Best Practices

- **Source**: https://www.baeldung.com/java-concurrency
- **Summary**: Recommends using thread pools (`ThreadPoolTaskExecutor`) over raw threads, preferring `java.util.concurrent.Locks` over `synchronized` for flexibility, using `CompletableFuture` for async tasks, and applying coordination utilities (`CountDownLatch`, `CyclicBarrier`) for phased execution. The Fork/Join framework handles recursive parallel tasks; custom thread pools should be sized for parallel streams. Core message: concurrency has many pitfalls — master fundamentals before tackling async programming.
- **Relevance**: Concurrency is one of the most error-prone areas of Java development; following these patterns prevents race conditions, deadlocks, and thread-pool exhaustion.

### Baeldung: Java 17 Features

- **Source**: https://www.baeldung.com/java-17-new-features
- **Summary**: Java 17 (LTS) introduces sealed classes (finalized, restrict which subclasses can extend a type), pattern matching for switch (preview, dramatically reduces boilerplate type checks), enhanced PRNGs (legacy `Random` now implements `RandomGenerator`), and enforced JDK encapsulation. Removes RMI Activation, experimental AOT/JIT compilers, and Applet API. Recommends adopting sealed classes immediately and removing `--illegal-access` flags.
- **Relevance**: Java 17 is the primary LTS target for enterprise teams; knowing which features are stable vs. preview guides safe adoption decisions.

---

## Security and Dependency Management

### OWASP: Java Security Cheat Sheet

- **Source**: https://cheatsheetseries.owasp.org/cheatsheets/Java_Security_Cheat_Sheet.html
- **Summary**: Covers injection prevention (always use `PreparedStatement` with parameterized queries, JPA named parameters, avoid string concatenation in SQL/JPQL/XPath/JPQL), cryptography (never write custom crypto, prefer Google Tink over raw JCA/JCE, use AES-GCM for storage and ECDH+AES-GCM for transmission, keep all deps updated), and logging (use structured JSON format, parameterized log patterns, limit user-input size in log messages to prevent log injection).
- **Relevance**: OWASP is the authoritative source for security practices; these rules prevent the most common and high-severity Java vulnerabilities.

### OWASP: Java HTML Sanitizer

- **Source**: https://owasp.org/www-project-java-html-sanitizer/
- **Summary**: A Java library for sanitizing untrusted HTML to prevent XSS. Offers prepackaged policies (`Sanitizers.FORMATTING.and(Sanitizers.LINKS)`), custom `HtmlPolicyBuilder` policies, and community-defined configurations. Warns against CSS handling (large attack surface), requires explicit `allowWithoutAttributes()` for elements like `<a>`, and recommends `requireRelNofollowOnLinks()`. Runs ~4× faster than AntiSamy DOM mode.
- **Relevance**: Any Java web application rendering user-provided HTML must sanitize it; this library is the standard OWASP-endorsed solution.

### Maven: Introduction to Dependency Management

- **Source**: https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html
- **Summary**: Best practices include: always explicitly declare direct dependencies (don't rely on transitive), use correct dependency scopes (`compile`, `provided`, `runtime`, `test`), centralize version management in `<dependencyManagement>` in a parent POM, use BOMs (Bill of Materials) for consistent version sets across related artifacts, override transitive versions explicitly when needed, avoid `system` scope (use a private repository instead), and use `mvn dependency:analyze` to detect unused or undeclared dependencies.
- **Relevance**: Proper dependency management is critical for reproducible builds, security patching, and avoiding classpath conflicts in multi-module Java projects.

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://google.github.io/styleguide/javaguide.html
- https://www.baeldung.com/java-clean-code
- https://www.baeldung.com/solid-principles
- https://www.baeldung.com/design-patterns-series
- https://www.baeldung.com/java-unit-testing-best-practices
- https://www.baeldung.com/jvm-garbage-collectors
- https://www.baeldung.com/java-concurrency
- https://www.baeldung.com/java-17-new-features
- https://cheatsheetseries.owasp.org/cheatsheets/Java_Security_Cheat_Sheet.html
- https://owasp.org/www-project-java-html-sanitizer/
- https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html

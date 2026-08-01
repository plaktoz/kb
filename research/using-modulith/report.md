# Research: Using Modulith
*Generated: 2026-08-01 | Scope: Modulith architecture — intro + technical deep-dive + industry adoption, covering definition, structure, frameworks, migration, and trade-offs vs monolith/microservices*

## Research Outline

1. What is a Modulith? — definition, core principles, how it differs from monolith and microservices
2. Structuring a Modulith — module boundaries, internal APIs, dependency rules, code organization patterns
3. Framework Implementations — Spring Modulith, and reference implementations for other stacks
4. Migration Paths — moving from monolith or microservices to a modulith, and when to do it
5. Industry Adoption & Trade-offs — real-world cases, team experiences, and when to choose modulith

---

## What is a Modulith?

### MonolithFirst — Martin Fowler

- **Source**: https://martinfowler.com/bliki/MonolithFirst.html
- **Summary**: Fowler argues that new projects should begin as monoliths rather than jumping into microservices, primarily for two reasons: microservices carry upfront complexity (the "MicroservicePremium") that slows early development, and experienced architects often struggle to identify correct service boundaries before the domain is well understood. Fowler recommends designing the monolith carefully with internal modularity — effectively describing the modulith concept without naming it. He warns that most monoliths degrade because they "accumulate too many dependencies between their modules," making later decomposition impossible.
- **Relevance**: Establishes the philosophical foundation for the modulith: internal modularity isn't just nice-to-have, it's the prerequisite for any meaningful evolution.

### Sacrificial Architecture — Martin Fowler

- **Source**: https://martinfowler.com/bliki/SacrificialArchitecture.html
- **Summary**: This article argues that accepting you will eventually discard your current architecture is a strategic choice, not a failure. Fowler recommends starting with a well-structured monolith to discover the right modular boundaries, then introducing microservices incrementally later. Good internal modularity is essential: it lets you sacrifice individual modules as they mature rather than entire systems, which is far more practical at scale.
- **Relevance**: Explains why a modulith is often the optimal "sacrificial" starting point — it lets boundary discovery happen cheaply before committing to expensive distributed infrastructure.

### Sliced Onion Architecture — Oliver Drotbohm

- **Source**: https://odrotbohm.de/2023/07/sliced-onion-architecture/
- **Summary**: Drotbohm introduces the "Sliced Onion" as an evolution of Onion Architecture that separates outward-facing adapters (APIs, web) from inward-facing adapters (databases, messaging), creating clean entry points for tests and inter-domain interaction. Multiple Sliced Onions can coexist in one deployment unit, communicating via process-internal events or direct API invocation. The result is what Drotbohm calls "modulithic architecture": a single deployable with "natural, low-cost seams" enabling easy restructuring or eventual splitting without costly rewrites.
- **Relevance**: Provides the most precise definition of a modulith from its primary architect, and shows how the internal structure (Sliced Onion per module) relates to the overall system structure.

---

## Structuring a Modulith

### Package-by-Feature — Philipp Hauer

- **Source**: https://phauer.com/2020/package-by-feature/
- **Summary**: This article advocates organizing code around business domains rather than technical layers. A feature package contains all classes needed for that feature (controller, DAO, DTOs, entities, service clients). The guiding rule: "if you want to delete a feature, you should only have to delete the corresponding package." Hauer suggests evolving feature packages into formal components with `api` and `internal` subpackages, defining exactly what other modules may access — enforcing encapsulation within a single deployable unit.
- **Relevance**: Package-by-feature is the foundational organizing principle for modulith structure; the `api`/`internal` split is the same pattern enforced by Spring Modulith.

### Spring Modulith Reference Documentation

- **Source**: https://docs.spring.io/spring-modulith/reference/
- **Summary**: Spring Modulith defines modules by package structure: each direct sub-package of the main application package is a module. Types in the module's root package are its public API; types in an `internal` sub-package are inaccessible to other modules. Boundary violations are caught by calling `ApplicationModules.of(MyApplication.class).verify()` in a test. Modules communicate via Spring Application Events rather than direct dependencies, keeping coupling low.
- **Relevance**: Provides the most concrete, code-level specification of how a well-structured modulith defines and enforces its module boundaries.

### Deconstructing the Monolith — Shopify Engineering

- **Source**: https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity
- **Summary**: Shopify's Rails codebase grew to ~6,000 Ruby classes with no enforced boundaries, causing fragile CI and a steep learning curve. The team reorganized around business domains (orders, shipping, billing, inventory), making each component a self-contained mini-Rails app. A custom tool called Wedge uses Ruby tracepoints to build a full call graph during CI and flags cross-boundary violations. Rules are strict: cross-component ActiveRecord associations are always a violation; cross-component calls are only permitted through explicitly public APIs.
- **Relevance**: Demonstrates that module boundary enforcement requires tooling beyond naming conventions — Wedge is the "verify()" equivalent for a non-framework-supported stack.

---

## Framework Implementations

### Spring Modulith — Official Project

- **Source**: https://spring.io/projects/spring-modulith
- **Summary**: Spring Modulith is a Spring Boot extension that enables building domain-driven, modular applications. It provides module structure verification, isolated integration testing via `@ApplicationModuleTest`, observability at the module level, and automatic documentation generation (component diagrams, module canvases). Modules are discovered automatically from package structure.
- **Relevance**: The most mature and widely adopted framework for building moduliths on the JVM; directly usable in any Spring Boot application with minimal configuration.

### Modular Monolith with DDD — Kamil Grzybek (.NET Reference Implementation)

- **Source**: https://github.com/kgrzybek/modular-monolith-with-ddd
- **Summary**: A production-grade .NET sample application modeling a Meetup.com-like platform across five independent modules (Meetings, Payments, Administration, User Access, Registrations). Modules communicate only asynchronously via an Events Bus. Each module uses Clean Architecture internally with Application, Domain, Infrastructure, and IntegrationEvents layers. Advanced patterns include CQRS, Outbox/Inbox for reliable inter-module messaging, Event Sourcing in the Payments module, and C4 Model diagrams for documentation. It covers unit, integration, architecture, and system integration tests.
- **Relevance**: Best available reference implementation for modulith architecture outside the JVM; shows how DDD tactical patterns (bounded contexts, domain events) map directly onto module structure.

---

## Migration Paths

### Refactoring a Monolith — microservices.io

- **Source**: https://microservices.io/refactoring/
- **Summary**: The Strangler Application Pattern is the primary approach for incremental monolith migration: new features are built as separate services, and existing modules are progressively extracted. A modular monolith is an explicit intermediate step — subdomains are encapsulated behind facades, domains are decoupled with the Observer pattern, and transactions are managed within bounded modules. Full migration follows five steps: identify subdomains (DDD), define system operations and service architecture, build new capabilities as services, extract existing modules incrementally, and apply Strangler until the monolith is eliminated.
- **Relevance**: Positions the modulith as an intentional waypoint in the migration journey rather than just a compromise, and provides a concrete migration sequence.

### MonolithFirst — Martin Fowler (migration angle)

- **Source**: https://martinfowler.com/bliki/MonolithFirst.html
- **Summary**: Fowler observes that even experienced architects working in familiar domains struggle to get service boundaries right at the beginning. A modular monolith lets you learn where the natural divisions are before making costly distributed-system commitments. The key recommendation: design the monolith with good modularity at the API boundaries and how data is stored — this makes the eventual extraction into services viable rather than a costly rewrite.
- **Relevance**: Explains *why* the modulith-first migration path works: domain knowledge and boundary clarity grow with time, and the modulith preserves optionality.

---

## Industry Adoption & Trade-offs

### Deconstructing the Monolith — Shopify Engineering (industry angle)

- **Source**: https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity
- **Summary**: Shopify chose the modular monolith path for their Rails core rather than splitting into microservices, reasoning that "modular monoliths capture benefits of both monoliths and microservices without doubling operational overhead." Their core lesson: "no architecture is often the best architecture in the early days," and domain expertise grows over time, making premature microservice splits risky. The team explicitly avoided microservices to keep operational complexity manageable while still enforcing module isolation.
- **Relevance**: One of the most visible real-world endorsements of the modulith from a major production system at scale.

### Microservices — Martin Fowler (trade-offs section)

- **Source**: https://martinfowler.com/articles/microservices.html
- **Summary**: Fowler cautions that microservices amplify problems for less capable teams ("a poor team will always create a poor system"), and that poorly drawn service boundaries merely shift complexity from inside a component to between components. He acknowledges the "monolith-first" counterargument and cites The Guardian website as a successful hybrid — a monolithic core with microservices at the edges. He notes that refactoring boundaries is significantly harder with distributed services than with in-process libraries.
- **Relevance**: From the article that launched mainstream microservices adoption, the explicit acknowledgment that large modular monoliths are a valid alternative carries significant weight.

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://martinfowler.com/bliki/MonolithFirst.html
- https://martinfowler.com/bliki/SacrificialArchitecture.html
- https://martinfowler.com/articles/microservices.html
- https://odrotbohm.de/2023/07/sliced-onion-architecture/
- https://spring.io/projects/spring-modulith
- https://docs.spring.io/spring-modulith/reference/
- https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity
- https://phauer.com/2020/package-by-feature/
- https://github.com/kgrzybek/modular-monolith-with-ddd
- https://microservices.io/refactoring/

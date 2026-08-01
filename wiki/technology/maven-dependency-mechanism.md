---
type: literature-note
source_url: https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html
author: Unknown
tags: [maven, java, build-tools, dependency-management]
date_consumed: 2026-08-01
---

## Summary

Apache Maven resolves dependencies transitively by reading remote project files, using a "nearest definition" rule to mediate version conflicts when the same artifact appears at multiple depths in the tree. Dependency scope controls classpath visibility and transitivity, with six scopes ranging from `compile` to `import`. Centralized version control is achieved through `<dependencyManagement>` in parent POMs and Bill of Materials (BOM) POMs that downstream projects can import.

## Core Concepts

- **[[Transitive Dependencies]]**: Maven automatically includes dependencies of dependencies; cyclic dependencies are detected and rejected.
- **[[Nearest Definition Rule]]**: When multiple versions of the same artifact exist in the dependency tree, Maven selects the version with the shortest path from the root project.
- **[[Dependency Scope]]**: Six scopes — `compile` (default, transitive), `provided` (not transitive), `runtime`, `test`, `system` (not recommended), `import` (BOM only) — govern classpath availability and transitivity propagation.
- **[[Dependency Management]]**: A `<dependencyManagement>` block in a parent [[Apache Maven|Maven]] POM centralizes version declarations; child POMs inherit versions without repeating them.
- **[[Bill of Materials (BOM)]]**: A POM artifact (`packaging=pom`) that declares consistent versions for a group of related artifacts; imported via `scope=import` to avoid single-parent inheritance constraints.
- **[[mvn dependency:tree]]**: CLI command to visualize the full resolved dependency graph including transitive dependencies.
- **[[mvn dependency:analyze]]**: CLI command to identify undeclared-but-used and declared-but-unused dependencies.
- **[[Maven 4 BOM Packaging]]**: Maven 4.0 introduces a dedicated `bom` packaging type, backward compatible with Maven 3.x consumers.

## Key Takeaways

- **Nearest-wins mediation**: Explicitly declare all direct dependencies to prevent silent version downgrades from transitive paths.
- **Scope matrix**: `compile`→`compile` transitive; `provided` and `test` do not propagate transitively.
- **BOM import order matters**: First BOM declaration wins when multiple BOMs define the same artifact.
- **Avoid `system` scope**: Binds the build to a local machine path; publish to a private repository instead.
- **Key identity tuple**: `{groupId, artifactId, type, classifier}` uniquely identifies a managed dependency entry.
- **Audit tools**: Use `mvn dependency:tree` and `mvn dependency:analyze` regularly for dependency hygiene.
- **Maven 4.0**: Introduces a dedicated `bom` packaging type, backward compatible with Maven 3.x consumers.

## 🧠 First Principles & Mental Models

- **[[Single Source of Truth]]**: The BOM pattern collapses N individual version declarations across N modules into one authoritative declaration, eliminating drift — a direct application of the single source of truth principle.
- **[[Explicit Over Implicit]]**: Maven's best-practice to declare all direct dependencies — even those transitively available — reflects that explicit declarations make systems more predictable and resilient to upstream changes.

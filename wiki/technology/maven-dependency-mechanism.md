---
type: literature-note
source_url: https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html
author: Apache Maven
tags: [maven, java, dependency-management, build-tools]
date_consumed: 2026-07-27
---

## Summary

Maven's dependency mechanism automatically resolves transitive dependencies by reading remote project files, using "nearest definition" (shortest path) for version conflicts. Dependency scope controls classpath inclusion and transitivity across six scopes (`compile`, `provided`, `runtime`, `test`, `system`, `import`). The `<dependencyManagement>` section and BOM (Bill of Materials) POMs enable centralized version governance across multi-module projects.

## Core Concepts

- **[[Transitive Dependencies]]**: Maven automatically includes the dependencies of your dependencies — no manual discovery required; depth is unlimited.
- **[[Nearest Definition Rule]]**: When multiple versions of the same artifact appear in the dependency tree, Maven picks the version with the shortest path to the project root.
- **[[Dependency Scope]]**: Controls when a dependency is on the classpath and whether it transits to downstream projects. Six scopes: `compile` (default, transitive), `provided` (not transitive), `runtime`, `test`, `system` (not recommended), `import` (BOM only).
- **[[Dependency Management]]**: `<dependencyManagement>` in a parent POM centralizes version, scope, and exclusion settings — child POMs declare dependencies without specifying versions.
- **[[BOM POM]]** (Bill of Materials): A POM with only `<dependencyManagement>` entries; imported via `scope=import` to share version governance across projects that don't share a parent.
- **[[Import Scope]]**: Used exclusively in `<dependencyManagement>` to import all managed dependencies from another POM; first declaration wins on conflicts.
- **[[Dependency Exclusion]]**: `<exclusion>` in a dependency declaration prevents a specific transitive dependency from being pulled in.
- **[[mvn dependency:tree]]**: CLI tool to visualize the full resolved dependency graph including transitive dependencies.
- **[[mvn dependency:analyze]]**: CLI tool to identify undeclared but used, and declared but unused, dependencies.
- **[[Maven 4 BOM packaging]]**: Maven 4.0 introduces a dedicated `bom` packaging type (model 4.1.0) that is fully compatible with Maven 3.x consumers.

## Key Takeaways

- Always explicitly declare dependencies your source code uses directly — don't rely on transitive inclusion.
- Nearest definition resolves version conflicts: declare the desired version at the top level to override deeper transitive versions.
- `compile` scope is the default and most transitive; use `provided` for container-supplied deps, `test` for test-only.
- `system` scope binds the build to a specific machine path — never use in shared codebases; publish to a private repo instead.
- `<dependencyManagement>` does NOT affect plugin dependencies — only project dependencies.
- BOM POMs are the canonical pattern for library suites (e.g., Spring BOM, AWS SDK BOM) — import them to align versions.
- Import order in `<dependencyManagement>` matters: first matching declaration wins across multiple BOMs.
- `mvn dependency:tree` and `mvn dependency:analyze` are essential diagnostic tools for dependency hygiene.

## 🧠 First Principles & Mental Models

- **[[Single Source of Truth]]**: The BOM pattern exists to make version governance a single source of truth — when you have N modules depending on the same library, having N individual version declarations is N opportunities for drift; a BOM collapses this to one authoritative declaration.

---
type: literature-note
source_url: https://www.baeldung.com/solid-principles
author: Sam Millington
tags: [software-design, object-oriented, clean-code, architecture]
date_consumed: 2026-08-01
---

## Summary

SOLID is a five-principle acronym for object-oriented design introduced by [[Robert C. Martin]] in 2000 and popularized by Michael Feathers. Each principle targets a specific failure mode in growing codebases — from bloated classes to tightly coupled dependencies. Applied together, they produce software that is easier to test, extend, and maintain as complexity scales.

## Core Concepts

- **[[Single Responsibility Principle]] (SRP)**: A class should have exactly one responsibility and one reason to change — separate concerns into dedicated classes.
- **[[Open/Closed Principle]] (OCP)**: Classes should be open for extension but closed for modification — extend via subclassing rather than editing working code.
- **[[Liskov Substitution Principle]] (LSP)**: Every subclass must be substitutable for its parent without breaking program behavior — violated when overrides throw unexpected exceptions.
- **[[Interface Segregation Principle]] (ISP)**: Split large interfaces into focused, role-specific ones so implementing classes only depend on methods they actually use.
- **[[Dependency Inversion Principle]] (DIP)**: High-level and low-level modules should depend on abstractions, not concrete implementations — inject dependencies through constructors or interfaces.
- **[[Technical Debt]]**: SOLID principles exist specifically to slow its accumulation in growing codebases.
- **[[Robert C. Martin]]**: Author of the original 2000 paper "Design Principles and Design Patterns" that introduced these principles.

## Key Takeaways

- **SRP**: One class, one responsibility — fewer test cases, lower coupling, cleaner org.
- **OCP**: Extend by subclassing; never modify working, tested code.
- **LSP**: Subclasses must honor the parent's behavioral contract, not just its type signature.
- **ISP**: Prefer many small interfaces over one large one — callers only see what they need.
- **DIP**: Depend on abstractions; inject concrete types from outside the class.
- **Scale threshold**: Benefits of SOLID grow proportionally with codebase size and complexity.
- **Contextual application**: Apply principles where they reduce real complexity, not dogmatically.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: Each SOLID principle is a specific application of this meta-principle — SRP separates responsibilities, ISP separates interfaces, DIP separates policy from mechanism.
- **[[Inversion of Control]]**: DIP is the concrete expression of IoC — flipping dependency direction so high-level modules define abstractions that low-level modules implement, keeping architectural control at the top.

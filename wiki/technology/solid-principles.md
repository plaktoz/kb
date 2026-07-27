---
type: literature-note
source_url: https://www.baeldung.com/solid-principles
author: Sam Millington
tags: [java, solid, oop-design, software-architecture]
date_consumed: 2026-07-27
---

## Summary

SOLID is a set of five object-oriented design principles introduced by Robert C. Martin in 2000 and popularized by Michael Feathers' acronym. Each principle addresses a specific failure mode of poorly-structured OOP code, collectively pushing toward software that is more maintainable, understandable, and flexible. The article walks through each principle with concrete Java code examples showing violations and fixes.

## Core Concepts

- **[[Single Responsibility Principle]]** (SRP): A class should have one responsibility and one reason to change — enables easier testing, lower coupling, better organization.
- **[[Open/Closed Principle]]** (OCP): Classes should be open for extension (via inheritance or composition) but closed for modification — prevents introducing new bugs into working code.
- **[[Liskov Substitution Principle]]** (LSP): Every subclass must be substitutable for its parent without breaking program behavior — enforces honest inheritance contracts.
- **[[Interface Segregation Principle]]** (ISP): Split large interfaces into smaller, focused ones so implementing classes only need relevant methods.
- **[[Dependency Inversion Principle]]** (DIP): High-level and low-level modules should both depend on abstractions, not concrete implementations — enables testability and swappability.
- **[[Dependency Injection]]**: The mechanism used to implement DIP; dependencies are passed into a class rather than instantiated inside it.
- **[[Robert C. Martin]]**: Author of "Design Principles and Design Patterns" (2000); originator of SOLID principles.

## Key Takeaways

- SRP: separate `BookPrinter` from `Book` — printing is a distinct concern.
- OCP: extend `Guitar` into `SuperCoolGuitarWithFlames` instead of modifying it.
- LSP: `ElectricCar` throwing on `turnOnEngine()` violates the `Car` interface contract; fix by redesigning the interface.
- ISP: split `BearKeeper` into `BearCleaner`, `BearFeeder`, `BearPetter` — implementors choose only what applies.
- DIP: inject `Keyboard` interface into `Windows98Machine` rather than `new StandardKeyboard()` inside the constructor.
- Benefits scale with codebase size and complexity — apply contextually, not dogmatically.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: SOLID is essentially a formalization of separating concerns at the class and interface level — each principle isolates a different axis of change to prevent cascading breakage.
- **[[Inversion of Control]]**: DIP is the principle behind IoC containers (Spring, Guice) — making high-level policy independent of low-level mechanism is what enables testing and runtime flexibility.

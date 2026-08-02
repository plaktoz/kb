---
type: literature-note
source_url: https://github.com/thunderrun/software-engineering-cheat-sheet
author: thunderrun
tags: [software-engineering, agile, sdlc, software-quality]
date_consumed: 2026-08-02
---

## Summary

This cheat sheet distills the essential concepts from *Software Engineering: A Practitioner's Approach* (8th edition) by Roger Pressman, covering the full development lifecycle from communication through deployment. It synthesizes the core process framework, modeling principles, construction practices, testing guidelines, UI design rules, and software quality models. The material serves as a rapid reference for applying classical and agile software engineering discipline in practice.

## Core Concepts

### [[Software Development Lifecycle]] (SDLC)

Five phases: **Communication → Planning → Modeling → Construction → Deployment**, supported by **Umbrella Activities** (risk management, [[Quality Assurance]], technical reviews, [[Configuration Management]], and measurement).

### [[Agile Manifesto]] Principles

- Early, continuous delivery of valuable software
- Welcoming changing requirements as competitive advantage
- Shorter delivery timescales (weeks over months)
- Self-organizing teams produce the best architectures
- Working software as the primary measure of progress
- Simplicity defined as "the art of maximizing the amount of work not done"

### [[Software Modeling]]

- **Requirements Modeling**: information domain representation, function/behavior definition, layered partitioning, progressing from essential to implementation detail
- **Design Modeling**: traceability to requirements, [[Loose Coupling]], functional independence, iterative development
- **Living Modeling**: models and code closely coupled, bidirectional information flow, persistent model information for change tracking

### [[Software Quality]] Models

- **[[FURPS]]**: Functionality, Usability, Reliability, Performance, Supportability
- **[[McCall's Quality Factors]]**: Product Operation (correctness, reliability, efficiency, integrity, usability), Product Revision (maintainability, flexibility, testability), Product Transition (portability, reusability, interoperability)
- **[[ISO 9126]]**: Functionality, Reliability, Usability, Efficiency, Maintainability, Portability

### [[Software Architecture]] Taxonomy

Five styles: Data-Centered, Data-Flow, Call-and-Return, [[Object-Oriented Architecture]], and Layered Architectures.

### [[User Interface Design]] Golden Rules

1. Place the user in control (flexible, interruptible, undoable interactions)
2. Reduce memory load (meaningful defaults, real-world metaphors, progressive disclosure)
3. Maintain consistency (across product line and established user expectations)

## Key Takeaways

- **Essence of Practice**: Understand problem → plan solution → carry out plan → examine result.
- **Agility Core**: Self-organizing teams and short delivery cycles drive quality outcomes.
- **Before Coding**: Understand problem, design principles, select language, create unit tests first.
- **During Coding**: Use structured programming, pair programming, and self-documenting code.
- **After Coding**: Conduct walkthroughs, run unit tests, and refactor.
- **Testing**: [[Pareto Principle]] applies — most defects cluster in a minority of modules.
- **Testing Planning**: Begins well before testing starts; all tests trace to customer requirements.
- **Mobile Challenges**: Multiple platforms, short cycles, UI limits, power, security, and testing complexity.
- **UI Principles**: Anticipation, communication, consistency, efficiency, flexibility, learnability, readability, visible navigation.

## 🧠 First Principles & Mental Models

- **[[Pareto Principle]]**: In software testing, 80% of defects are concentrated in ~20% of modules — prioritizing testing on high-risk components yields disproportionate quality gains.
- **[[Separation of Concerns]]**: The distinction between requirements modeling (what) and design modeling (how) embodies this principle — keeping concerns cleanly layered allows each to evolve independently without entangling logic.

## 🃏 Review Questions

**Q1**: What is the core five-phase process framework described in the cheat sheet?
**A**: Communication, Planning (estimation, scheduling, risk analysis), Modeling (analysis, design), Construction (code, test), and Deployment (delivery, feedback).

**Q2**: How does the Agile Manifesto define simplicity?
**A**: Simplicity is described as "the art of maximizing the amount of work not done," emphasizing eliminating unnecessary work rather than adding features.

**Q3**: What should a developer do before writing any code according to the construction guidelines?
**A**: Understand the problem, understand design principles, select an appropriate language/environment, and create unit tests in advance of coding.

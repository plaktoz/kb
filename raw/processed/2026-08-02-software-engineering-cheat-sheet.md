---
source_url: https://github.com/thunderrun/software-engineering-cheat-sheet
author: thunderrun
date: 2026-08-02
---

# Software Engineering: A Practitioner's Approach — Cheat Sheet

Notes & Essentials of *Software Engineering: A Practitioner's Approach*, 8th edition.

## Core Process Framework

The development lifecycle includes five phases: **Communication, Planning** (estimation, scheduling, risk analysis), **Modeling** (analysis, design), **Construction** (code, test), and **Deployment** (delivery, feedback).

Supporting these are **Umbrella Activities** such as risk management, quality assurance, technical reviews, configuration management, and measurement.

## Key Principle Sets

### Essence of Practice
Understand the problem → Plan the solution → Carry out the plan → Examine the result.

### General Principles
Highlights include keeping things simple, maintaining vision, planning ahead for reuse, and thinking critically.

### Agility Principles (12 Agile Manifesto principles summarized)
- Prioritize early, continuous delivery of valuable software
- Welcome changing requirements as competitive advantage
- Prefer shorter delivery timescales (weeks over months)
- Daily collaboration between business and developers
- "Working software is the primary measure of progress"
- Simplicity is "the art of maximizing the amount of work not done"
- Self-organizing teams produce the best architectures and designs
- Regular team retrospectives for continuous improvement

## Modeling

### Requirements Modeling Covers:
- Information domain representation
- Function and behavior definition
- Layered partitioning of models
- Moving from essential information toward implementation detail

### Design Modeling Emphasizes:
- Traceability to requirements
- Loose coupling between components
- Functional independence at component level
- Iterative design development

### Living Modeling Principles:
- Models and code should be "closely coupled"
- Bidirectional information flow between models and code
- Persistent model information for change tracking

## Construction

**Before coding:** Understand the problem, understand design principles, select appropriate language/environment, and create unit tests in advance.

**While coding:** Follow structured programming, consider pair programming, use meaningful variable names, write self-documenting code, and keep conditional logic simple.

**After coding:** Conduct walkthroughs, run unit tests, and refactor.

## Testing Principles

- All tests traceable to customer requirements
- Planning begins well before testing starts
- The Pareto principle applies — most defects cluster in a minority of modules
- Progress from small-scale to large-scale testing
- Include cases that confirm correct behavior, not just find failures

## User Interface Design

### Golden Rules:
1. **Place the user in control** — allow flexible, interruptible, undoable interactions
2. **Reduce memory load** — use meaningful defaults, real-world metaphors, progressive disclosure
3. **Maintain consistency** — across the product line and with established user expectations

### Interface Principles Include:
Anticipation, Communication, Consistency, Efficiency, Flexibility, Learnability, Readability, and Visible Navigation.

## Quality Models

### FURPS:
Functionality, Usability, Reliability, Performance, Supportability

### McCall's Quality Factors:
- *Product Operation:* Correctness, Reliability, Efficiency, Integrity, Usability
- *Product Revision:* Maintainability, Flexibility, Testability
- *Product Transition:* Portability, Reusability, Interoperability

### ISO 9126:
Functionality, Reliability, Usability, Efficiency, Maintainability, Portability

## Architectural Taxonomy

Five styles: Data-Centered, Data-Flow, Call-and-Return, Object-Oriented, and Layered Architectures.

## Mobile App Considerations

Key challenges include multiple platforms, short development cycles, UI limitations, power management, security, computational constraints, and testing complexity. The development process follows a spiral: Formulation → Planning → Analysis → Engineering → Implementation/Testing → User Evaluation.

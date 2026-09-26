---
source_url: https://docs.typesafe.ai/patterns
author: Unknown
date: 2026-09-26
---

# Patterns — TypeSafe AI

Architectural patterns for building systems with TypeSafe, designed to power decisions with AI within larger systems.

## Core Concept

Learning to think in discrete, atomic decisions that compose into complex system behavior is key to getting the most from TypeSafe. Prerequisites: understanding TypeSafe primitives and how confidence works.

## Available Patterns

| Pattern | Purpose | Benefits |
|---|---|---|
| **Speculative Fan-Out** | Send many questions (including speculative ones) in one call; code decides relevance | Cost, Speed |
| **Confidence-Gated Routing** | Uses confidence as a second decision axis for safer systems | Reliability, Safety |
| **Composite Scoring** | Merges multiple analysis dimensions into one score | Cost, Reliability, Speed |
| **Intent Routing** | Classifies user intent and routes to the appropriate handler | Cost, Speed |

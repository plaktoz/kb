---
source_url: https://machinelearningmastery.com/dataclasses-for-structured-application-data/
author: Nahla Davies
date: 2026-09-09
---

# Dataclasses for Structured Application Data

The article argues that Python's `@dataclass` decorator is a superior replacement for configuration dictionaries, which fail silently through typos, inconsistent defaults, and ambiguous nested shapes.

## Core Problem with Dicts

A misspelled key like `config.get("batchsize", 100)` silently uses the wrong default. Dataclasses convert this into an `AttributeError` caught immediately by IDEs or type checkers.

## Key Concepts

**Basic Structure:** Decorating a class with `@dataclass` auto-generates `__init__`, `__repr__`, and `__eq__`. However, type annotations are *not* enforced at runtime — they're "documentation with excellent tooling support."

**Composition:** Nest small dataclasses rather than building one oversized class. Use `field(default_factory=...)` for mutable defaults (lists, nested objects) to prevent shared-state bugs.

**Validation via `__post_init__`:** Run invariant checks immediately after construction, raising descriptive errors. Keep this hook focused — complex coercion logic signals it's time for Pydantic.

**Immutability:** `frozen=True` blocks assignment but doesn't prevent mutation of mutable fields (e.g., lists). Use `dataclasses.replace()` to create validated modified copies.

**Serialization:** `asdict()` recursively serializes outward cleanly. Deserialization requires explicit reconstruction — nested dicts won't auto-convert back to dataclasses.

## Tool Selection Guide

| Tool | Best For | Runtime Checks |
|------|----------|----------------|
| `dict` | Short-lived, flexible local data | None |
| `dataclass` | Trusted, app-owned structures | Manual `__post_init__` only |
| Pydantic | External/untrusted input | Full coercion + rich errors |

The decision rule: match the tool to data ownership and trust level on arrival.

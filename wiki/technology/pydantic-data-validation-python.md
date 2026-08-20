---
type: literature-note
source_url: https://pydantic.dev/docs/validation/latest/get-started/
author: Unknown
tags: [python, data-validation, type-hints, pydantic]
date_consumed: 2026-08-20
---

## Summary
Pydantic is Python's most widely used data validation library, downloaded over 550 million times per month and depended on by ~8,000 PyPI packages including FastAPI and LangChain. It derives schemas directly from Python type annotations and runs its core validation logic in Rust via `pydantic-core` for high performance. It supports both lax (coercion-permitting) and strict (exact-type) validation modes, detailed error reporting, and JSON Schema emission.

## Core Concepts
- [[BaseModel]]: The primary way to define a validated data schema — subclass it and annotate fields with Python type hints; Pydantic handles parsing, coercion, and serialization automatically.
- [[ValidationError]]: Raised when input fails validation; includes per-field breakdowns with field location, error type identifier, human-readable message, and the offending input value.
- [[Strict mode]]: Opt-in mode that disables type coercion — the input type must exactly match the annotated type; default lax mode allows e.g. `"42"` → `42`.
- [[Type coercion]]: Lax mode behavior where Pydantic automatically converts compatible types (string to int, bytes to string) to satisfy the annotated type.
- [[field_validator]] / [[model_validator]]: Decorators for attaching custom validation logic to individual fields or the whole model.
- [[JSON Schema]]: Pydantic can emit a valid JSON Schema from any `BaseModel` via `model_json_schema()`, useful for API documentation and OpenAI function-calling definitions.

## Key Takeaways
- **Annotation-driven**: Schema defined entirely from Python type hints — no separate DSL.
- **Rust core**: Validation runs in Rust (`pydantic-core`), making it faster than pure-Python alternatives.
- **Lax by default**: String `"42"` is silently coerced to `int 42` unless strict mode is enabled.
- **Rich errors**: `ValidationError` pinpoints every failing field, its location, and the bad input.
- **LLM ecosystem staple**: Used by LangChain, OpenAI function calling, and Guardrails AI for structured output validation.
- **Broad type support**: Handles primitives, datetime types, UUIDs, nested `BaseModel`, dataclasses, `TypedDict`, and more.
- **JSON Schema export**: `model_json_schema()` generates a JSON Schema object for documentation or client generation.

## 🧠 First Principles & Mental Models
**Parse, don't validate** — Pydantic models act as a parsing layer that transforms raw input into a known-good typed object; downstream code can trust the object's types without further checking. This is a foundational [[defensive programming]] pattern for API boundaries and LLM output handling.

## 🃏 Review Questions

**Q1**: What is the difference between Pydantic's lax and strict validation modes?
**A**: Lax mode (default) coerces compatible types (e.g. string `"42"` becomes `int 42`); strict mode requires the input type to exactly match the annotation and raises a `ValidationError` on any mismatch.

**Q2**: How does Pydantic achieve its performance advantage over pure-Python validators?
**A**: Its core validation logic is implemented in Rust via the `pydantic-core` library, which runs significantly faster than equivalent pure-Python code.

**Q3**: Why is Pydantic considered essential in LLM application development?
**A**: It is the de facto standard for defining and validating structured outputs from LLMs — used by LangChain, OpenAI function-calling definitions, and Guardrails AI — because it combines Python type hints with robust error reporting and JSON Schema emission.

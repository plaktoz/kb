---
source_url: https://pydantic.dev/docs/validation/latest/get-started/
author: Unknown
date: 2026-08-20
---

# Pydantic Validation

Pydantic is the most widely used data validation library for Python — fast, extensible, and built around Python type hints. Downloaded over 550 million times per month, it is used by major organizations including Google, Microsoft, NASA, OpenAI, and Anthropic. Approximately 8,000 PyPI packages depend on it, including FastAPI, LangChain, and Django Ninja.

## Core Design Principles

**Type annotation-driven:** Schema and serialization behavior is derived entirely from Python type annotations. No separate schema definition language required.

**Rust-powered performance:** The core validation logic runs in Rust via the `pydantic-core` library, making it significantly faster than pure-Python alternatives.

**Lax and strict modes:**
- **Lax mode (default):** Supports coercion — strings can be cast to integers, bytes to strings, etc.
- **Strict mode:** No coercion; the input type must exactly match the annotated type.

## Basic Usage

```python
from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None

# Valid input — coercion applied (string "42" → int 42)
user = User(id="42", name="Alice", email="alice@example.com")
print(user.model_dump())
# {'id': 42, 'name': 'Alice', 'email': 'alice@example.com', 'age': None}

# Invalid input — raises ValidationError
try:
    User(id="not-a-number", name="Bob", email="bob@example.com")
except ValidationError as e:
    print(e)
    # 1 validation error for User
    # id
    #   Input should be a valid integer [type=int_parsing, ...]
```

## Key Features

### Detailed ValidationError

Errors include per-field breakdowns with:
- Field location (including nested paths)
- Error type identifier
- Human-readable message
- Input value that caused the failure

This makes it easy to return precise error messages to API clients.

### JSON Schema Emission

```python
print(User.model_json_schema())
# Returns a valid JSON Schema object for documentation or client generation
```

### Supported Types

- All Python primitives
- `datetime`, `date`, `time`, `timedelta`
- `UUID`, `Decimal`, `Path`
- `List`, `Dict`, `Set`, `Tuple` and their `Optional`/`Union` variants
- Nested `BaseModel` classes
- `dataclasses` and `TypedDict`
- Custom validators via `@field_validator` and `@model_validator`

### Custom Validators

```python
from pydantic import BaseModel, field_validator

class Product(BaseModel):
    price: float
    
    @field_validator("price")
    @classmethod
    def price_must_be_positive(cls, v: float) -> float:
        if v <= 0:
            raise ValueError("Price must be positive")
        return v
```

## Relevance to LLM Applications

Pydantic is the de facto standard for structured output validation from LLMs:

- **LangChain:** Uses Pydantic models to define and validate structured LLM outputs
- **OpenAI function calling:** Pydantic schemas are commonly used to generate JSON Schema for function definitions
- **Guardrails AI:** Uses Pydantic models as the target schema for structured generation with validation

Installation: `pip install pydantic`

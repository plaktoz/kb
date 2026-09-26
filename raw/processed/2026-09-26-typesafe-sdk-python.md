---
source_url: https://github.com/typesafe-ai/typesafe-sdk-python
author: Unknown
date: 2026-09-26
---

# TypeSafe AI Python SDK

## Description

Python SDK for the [TypeSafe AI](https://typesafe.ai) platform.

## Installation

```bash
uv add typesafe-sdk
```

## Authentication

Set the `TYPESAFE_API_KEY` environment variable before use.

## Basic Usage

```python
from typesafe_sdk import Choice, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "I was charged twice. Please fix this ASAP."},
        questions={
            "category": Choice(
                instructions="What is this ticket about?",
                criteria={"billing": None, "technical": None, "other": None},
            ),
        },
    )

print(response.choices["category"].choice)
```

## Further Resources

- Full documentation: [docs.typesafe.ai/sdk/python](https://docs.typesafe.ai/sdk/python)
- License: MIT

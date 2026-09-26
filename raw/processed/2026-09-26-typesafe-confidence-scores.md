---
source_url: https://docs.typesafe.ai/confidence
author: Unknown
date: 2026-09-26
---

# Confidence — TypeSafe Documentation

## Overview

Score and Choice answers from TypeSafe include a `probabilities` property showing the distribution across options (Choice) or levels (Score). The distribution's shape indicates certainty: concentrated = confident, spread out = uncertain.

The `confidence` property compresses that shape into a 0–1 value for easy thresholding. (Noul answers don't include one.)

## How Confidence Is Calculated

Confidence is derived from the probability distribution already present in the answer. TypeSafe computes and returns it on every Choice and Score answer automatically.

- **Choice**: distribution across your options
- **Score**: distribution across your levels

A flatter distribution signals lower confidence. For Choice, this often means no clear winner. For Score, it may indicate ambiguous or multi-dimensional levels.

> **Note:** `confidence` fits most use-cases, but you're never locked into TypeSafe's definition — the full `probabilities` are always available if you need a custom measure.

## "I Don't Know" as a Signal

A system unable to express honest uncertainty cannot be trusted. Confidence gives the model a way to signal uncertainty, enabling your code to behave differently based on certainty level.

## Three Behavioral Ranges

| Range | Action |
|-------|--------|
| **High** | Act automatically |
| **Medium** | Proceed with caution; confirm or flag |
| **Low** | Route to human or request clarification |

## Thresholds Scale with Risk

Different actions should use different thresholds based on consequence severity:

```python
response = client.system_one(
    state=user_message,
    questions={
        "action": Choice(
            instructions="What is the user trying to do?",
            criteria={
                "check_balance": "View account balance",
                "approve_transfer": "Approve the pending withdrawal request",
                "support": "Get help with an issue",
            },
        ),
    },
)

action = response.answers["action"]
confidence = action.confidence

if confidence < 0.5:
    route_to_human(user_message)

elif action.choice == "check_balance":
    show_balance(account_id)

elif action.choice == "approve_transfer":
    if confidence > 0.9:
        confirm_then_execute(account_id)
    else:
        ask_user_to_confirm(account_id)
```

A `0.5` floor catches genuinely uncertain responses. Above that, destructive operations require higher confidence than read-only ones. The thresholds encode your system's risk tolerance.

> Start with conservative thresholds, test against your own data, and adjust based on observed results.

---
type: literature-note
source_url: https://github.com/typesafe-ai/typesafe-sdk-python
author: Unknown
tags: [jev, python, sdk, developer-tools]
date_consumed: 2026-09-26
---

## Summary

The TypeSafe Python SDK (`typesafe-sdk`) wraps the Jev API in a Pythonic interface requiring Python ≥ 3.10. The client reads `TYPESAFE_API_KEY` from the environment and is best used as a context manager. All three question types — [[Choice]], [[Score]], and [[Noul]] — are first-class importable objects, and answers are accessed as typed attributes on the response.

## Core Concepts

- **`TypeSafeClient`** — main client class; use as a context manager (`with TypeSafeClient() as client:`) for automatic connection cleanup
- **`Choice`** — categorical question; constructor takes `instructions` (string) and `criteria` (dict mapping label → description or `None`)
- **`Score`** — rating question; constructor takes `instructions` and `criteria` (list of level descriptions)
- **`Noul`** — yes/no question; constructor takes `instructions` only; returns 0–1 float
- **`client.system_one(state, questions)`** — primary method; `state` accepts a string or dict; `questions` is a dict of question name → question object
- **Answer access** — `response.choices["key"].choice` (or `response.answers["key"]` depending on SDK version); `.score`, `.noul` for other types
- **Auth** — `TYPESAFE_API_KEY` environment variable; no explicit key passing needed

## Key Takeaways

- **Install**: `uv add typesafe-sdk` or `pip install typesafe-sdk` (Python ≥ 3.10)
- **Auth**: set `TYPESAFE_API_KEY` environment variable once
- **Context manager**: use `with TypeSafeClient() as client:` for clean resource management
- **State can be dict**: pass structured JSON as state, not just raw strings
- **MIT license**: open-source, production-friendly

```python
from typesafe_sdk import Choice, Score, Noul, TypeSafeClient

with TypeSafeClient() as client:
    response = client.system_one(
        state={"document": "I was charged twice. Please fix this ASAP."},
        questions={
            "category": Choice(
                instructions="What is this ticket about?",
                criteria={"billing": None, "technical": None, "other": None},
            ),
            "urgency": Score(
                instructions="How urgent is this? 0=low, 5=critical",
                criteria=["0: no time pressure", "3: customer frustrated", "5: data loss"],
            ),
            "needs_escalation": Noul(instructions="Does this need manager escalation?"),
        },
    )
print(response.choices["category"].choice)
```

## 🃏 Review Questions

**Q1**: Why use `TypeSafeClient` as a context manager?
**A**: The `with` statement ensures the HTTP session is cleanly closed after use, preventing resource leaks in long-running applications.

**Q2**: How do you pass structured data (not just plain text) as the state to Jev?
**A**: Pass a Python dict as `state` — e.g. `state={"document": "...", "metadata": {...}}` — Jev accepts JSON objects, not just strings.

**Q3**: What are the three quickstart project patterns recommended for this SDK?
**A**: Support ticket router (classify and route by department), content moderation tagger (score text against policy categories), and lead scoring classifier (evaluate CRM notes against decision criteria).

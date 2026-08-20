---
source_url: https://github.com/guardrails-ai/guardrails
author: guardrails-ai organization
date: 2026-08-20
---

# Guardrails AI: Python Framework for Reliable AI Applications

Guardrails is an open-source Python framework for building reliable AI applications. It serves two primary purposes: running input/output guards to detect and mitigate risks, and generating structured data from LLMs.

**Stats:** 7.3k GitHub stars, 675 forks, Apache-2.0 license. Supports Python and JavaScript.

## Core Capabilities

### Input/Output Validation with Guards

**Guardrails Hub** provides a registry of pre-built validators that can be combined into guards intercepting LLM inputs and outputs.

Install validators via pip:
```bash
pip install guardrails-ai-regex-match
pip install guardrails-ai-competitor-check
pip install guardrails-ai-toxic-language
```

Chain multiple validators into a guard:
```python
from guardrails import Guard
from guardrails.hub import RegexMatch, CompetitorCheck, ToxicLanguage

guard = Guard().use_many(
    CompetitorCheck(["CompanyA", "CompanyB"]),
    ToxicLanguage(threshold=0.5),
    RegexMatch(pattern=r"^[a-zA-Z0-9\s]+$")
)

response = guard(
    llm_api=openai.chat.completions.create,
    prompt="Describe our product..."
)
```

### Structured Data Generation

Generate validated, structured Pydantic model outputs from LLMs using function calling or prompt optimization:

```python
from pydantic import BaseModel
from guardrails import Guard

class ProductReview(BaseModel):
    sentiment: str
    score: int
    summary: str

guard = Guard.for_pydantic(ProductReview)
result = guard(llm_api=openai.chat.completions.create, ...)
# Returns a validated ProductReview instance
```

### Deployment as a Service

Deploy as a standalone REST service compatible with the OpenAI API format:

```bash
guardrails start
```

This exposes an HTTP endpoint that wraps any LLM call with guardrail validation, allowing any OpenAI-compatible client to use it without code changes.

## Key Updates (July 2026)

Significant architecture change: validators are moving from the Guardrails Hub hosted service to standard PyPI packages. This means:
- Validators can be installed with standard `pip install` without a Hub account
- Hosted remote inferencing is being discontinued (cutoff: August 6, 2026)
- Local inference is recommended for all validators going forward

## Use Cases

- Competitor mention detection in customer-facing AI
- Toxic language filtering in user-generated content pipelines
- PII detection and redaction in outputs
- Schema validation for structured outputs fed into downstream systems
- Jailbreak and prompt injection detection at the application layer

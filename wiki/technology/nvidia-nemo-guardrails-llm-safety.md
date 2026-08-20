---
type: literature-note
source_url: https://docs.nvidia.com/nemo/guardrails/
author: Unknown
tags: [nvidia, llm-safety, guardrails, agentic-security]
date_consumed: 2026-08-20
---

## Summary
NVIDIA NeMo Guardrails is an open-source Python library that adds programmable safety and behavior rules to LLM-based applications. Unlike simple text validators, it uses a full conversation flow engine called [[Colang]] that can intercept inputs, outputs, dialog flow, tool calls, and RAG retrieval at any stage. Configurations are expressed as portable YAML + Colang files, enabling policy-as-code workflows that run identically in local development and production.

## Core Concepts
- **[[Colang]]** — Domain-specific language for defining conversational logic and control flow; drives all rail execution and off-topic redirection.
- **[[LLMRails]]** — Central Python object that loads YAML config + Colang flows and wraps any LLM call with the configured rail stack.
- **Rail types** — Five categories: input rails (validate/transform user messages), output rails (validate/transform model responses), dialog rails (topic adherence), execution rails (govern tool calls), and retrieval rails (control RAG behavior). See also [[llm-guardrail-patterns-input-output]].
- **Topic control rails** — Dialog rails that restrict the assistant to an intended domain; off-topic messages trigger configurable fallback responses defined in Colang flows.
- **[[PII masking]]** — Integrates with Microsoft Presidio, GLiNER, and Private AI to detect and mask PII in inputs before LLM processing, with optional unmasking in outputs.
- **Jailbreak protection** — Layered detection: heuristic pattern matching (low latency) + LLM-based detection + NemoGuard NIMs (NVIDIA Inference Microservices).
- **Agentic security** — Execution rails validate tool call parameters, block unauthorized invocations, and prevent prompt injection via retrieved documents.
- **Custom Python actions** — Arbitrary Python callable from Colang flows, enabling bespoke safety logic without leaving the rail framework.

## Key Takeaways
- **Conversation-layer interception**: Rails operate at the conversation flow level, not just on raw text strings.
- **Five rail types**: Input, output, dialog, execution, and retrieval — covering the full agentic LLM surface.
- **Policy-as-code**: YAML + Colang configs are version-controlled and portable between local and production.
- **Layered jailbreak defense**: Combines fast heuristics, flexible LLM checks, and specialized NVIDIA NIMs.
- **PII pipeline**: Mask before LLM, optionally unmask in response — keeps sensitive data out of model context.
- **Agentic prompt injection guard**: Retrieval rails block adversarial content injected through RAG documents.
- **Flexible integration**: Python SDK, OpenAI-compatible HTTP server, or native LangChain/LangGraph integration.

## 🧠 First Principles & Mental Models
**Defense in depth** — NeMo Guardrails applies the same layered security principle used in network security: no single check is sufficient, so multiple mechanisms (heuristics → LLM judge → specialized NIM) operate in sequence, each catching what the previous layer misses.

## 🃏 Review Questions

**Q1**: What is Colang and why does it matter for guardrails?
**A**: Colang is a domain-specific language that drives NeMo Guardrails' conversation flow engine. It enables declarative control over when rails fire and how the system redirects or blocks interactions — going beyond simple regex or text-matching validators.

**Q2**: How does NeMo Guardrails protect agentic (tool-using) LLMs from prompt injection?
**A**: Retrieval rails inspect documents retrieved during RAG before they reach the LLM, blocking adversarially crafted content that could hijack the agent's tool calls or redirect its behavior.

**Q3**: What advantage does the policy-as-code approach give development teams?
**A**: The same YAML + Colang configuration files work in both local development and the production guardrails microservice, so safety policies can be version-controlled, code-reviewed, and tested in CI before deployment.

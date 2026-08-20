---
source_url: https://docs.nvidia.com/nemo/guardrails/
author: Unknown
date: 2026-08-20
---

# NVIDIA NeMo Guardrails

NVIDIA NeMo Guardrails is an open-source Python library for adding programmable guardrails to LLM-based applications. It enables developers to "block, alter, or validate unsafe, off-topic, malicious, or policy-violating user inputs and model responses."

Unlike application-layer validators that operate on text strings, NeMo Guardrails uses a full conversation flow engine (Colang) that can intercept at any stage of an agentic LLM interaction.

## Core Architecture

### Building Blocks

- **Rails** — Configurable safety and behavior rules (see types below)
- **YAML configuration** — Declarative policy definitions
- **Colang flows** — Domain-specific language for conversational logic and control flow
- **Custom Python actions** — Arbitrary Python code invoked from Colang flows
- **Python SDK and server interfaces** — Integration options for different deployment patterns

### Rail Types

| Rail Type | Purpose |
|---|---|
| Input rails | Validate/transform user messages before LLM processing |
| Output rails | Validate/transform LLM responses before delivery |
| Dialog rails | Control conversation flow and topic adherence |
| Execution rails | Govern tool calls and agent actions |
| Retrieval rails | Control RAG document retrieval behavior |

## Key Use Cases

### Content Safety

Multiple implementation options for harmful content detection:
- LLM self-checking (prompt the same LLM to evaluate its own output)
- NVIDIA safety models (purpose-built classifiers)
- Third-party safety APIs (e.g., Azure Content Safety, Perspective API)

### Jailbreak Protection

Layered detection combining:
- Heuristic pattern matching (fast, low-latency)
- LLM-based detection (flexible, context-aware)
- NemoGuard NIMs (NVIDIA Inference Microservices for specialized safety)

### Topic Control

Dialog and topical rails restrict the AI to its intended domain:
- Define allowed topics in YAML
- Colang flows handle off-topic detection and graceful redirection
- Configurable fallback responses

### PII Detection and Masking

Integrations with:
- Microsoft Presidio (open-source PII detection)
- GLiNER (generalist entity recognition)
- Private AI (commercial PII solution)

PII can be masked in inputs before LLM processing, then unmasked in outputs if appropriate.

### Agentic Security

Specialized rails for tool-using LLM agents:
- Validate tool call parameters before execution
- Block unauthorized tool invocations
- Audit and log all agent actions
- Prevent prompt injection attacks via retrieved documents

## Integration Options

| Path | Best For |
|---|---|
| Python SDK | Direct Python integration; embedding in existing code |
| Guardrails server | HTTP/OpenAI-compatible endpoint; language-agnostic |
| LangChain/LangGraph | Framework-native integration for existing LangChain apps |

## Deployment Portability

Configurations (YAML + Colang) are portable between:
- Local development library
- Production microservice

The same policy files work in both environments, enabling policy-as-code workflows where guardrail rules are version-controlled and tested before deployment.

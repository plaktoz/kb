---
type: literature-note
source_url: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter
author: Unknown
tags: [content-filtering, azure-ai, llm-safety, guardrails]
date_consumed: 2026-08-20
---

## Summary
Microsoft Foundry's content filtering system wraps core LLM and image generation models with [[Azure AI Content Safety]], running both prompts and completions through an ensemble of classifiers to detect harmful output. It covers four core harm categories (hate, sexual, violence, self-harm) at graduated severity levels, plus optional specialized filters for groundedness, PII, protected material, and prompt injection. Customers can configure filter thresholds independently for prompts and completions, with the API returning structured error signals when content is blocked.

## Core Concepts
- **[[Azure AI Content Safety]]** — the underlying safety service powering Microsoft Foundry's filtering ensemble
- **[[Prompt Shields]]** — input-side defense detecting both direct user prompt attacks (jailbreaks) and indirect attacks (malicious instructions embedded in documents processed by the model)
- **[[LLM Guardrails]]** — the broader pattern of wrapping model I/O with policy enforcement; see also [[LLM Guardrail Patterns Input Output]] and [[Nvidia Nemo Guardrails LLM Safety]]
- **[[Groundedness Detection]]** — output filter that flags model responses not supported by provided source documents, helping surface [[hallucination]]
- **[[Content Filter Severity Levels]]** — four-point scale (safe → low → medium → high) applied to each harm category; customers choose which severity threshold triggers a block
- **[[Indirect Prompt Injection]]** — attack vector where malicious instructions are embedded in third-party documents an AI agent retrieves and processes

## Key Takeaways
- **Four core harm categories**: Hate/fairness, sexual, violence, self-harm — each with four severity levels.
- **Prompt Shields**: Detects jailbreaks in user turns and injections in retrieved documents.
- **Output-only filters**: Groundedness, PII, and protected material (text + code) apply to completions.
- **Configurable thresholds**: Low/medium/high, or annotation-only mode (approval required for no-filter).
- **API signals**: Blocked prompt → HTTP 400; blocked completion → `finish_reason: content_filter`.
- **Filtering unavailable**: Request still completes; error surfaces in `content_filter_results` object.
- **Audio exemption**: Whisper and other audio models are not covered by this system.

## 🧠 First Principles & Mental Models

**Defense-in-depth for LLM I/O**: Like network firewalls that inspect both inbound and outbound traffic, Azure's system treats both the prompt (input gate) and completion (output gate) as independent control surfaces. This means a misconfigured prompt threshold cannot allow harmful content to leak through the completion side.

**Severity as a dial, not a switch**: Rather than binary block/allow, graduated severity lets operators tune precision vs. recall — blocking only "high" severity catches egregious harms with fewer false positives, while blocking "low" maximizes safety at the cost of more friction.

## 🃏 Review Questions

**Q1**: What are the four core harm categories covered by Azure AI Content Safety in Microsoft Foundry?
**A**: Hate and Fairness, Sexual, Violence, and Self-Harm — each evaluated at safe/low/medium/high severity levels.

**Q2**: How do Prompt Shields differ from standard content filters, and what two attack types do they cover?
**A**: Prompt Shields focus specifically on adversarial inputs: direct user prompt attacks (jailbreaks trying to override the system) and indirect attacks (malicious instructions injected into documents the model retrieves and processes).

**Q3**: What API behavior should developers handle when a completion is filtered mid-stream?
**A**: In streaming mode the stream continues until the filtered segment; the final chunk carries `finish_reason: content_filter`. Developers must check `finish_reason` on every chunk and verify `content_filter_results` contains no error object to confirm filters ran successfully.

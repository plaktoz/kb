---
type: literature-note
source_url: https://raw.githubusercontent.com/OWASP/www-project-top-10-for-large-language-model-applications/main/Archive/1_1_vulns/LLM04_ModelDoS.md
author: OWASP
tags: [llm-security, denial-of-service, owasp, ai-infrastructure]
date_consumed: 2026-08-20
---

## Summary

LLM04 from the OWASP Top 10 for LLMs covers Denial of Service attacks where adversaries consume excessive model resources, degrading service quality and inflating infrastructure costs. The attack surface centers on the [[Context Window]] — the fixed-length text buffer every LLM uses for input and output — which can be exploited through overflow, recursive expansion, or variable-length flooding. Developers often remain unaware of this vulnerability despite the high resource intensity of LLM inference.

## Core Concepts

- **[[Model Denial of Service]] (LLM04)**: An attacker deliberately triggers high resource consumption in a hosted [[Large Language Model]], causing service degradation or outage for all users.
- **[[Context Window]]**: The maximum text length (input + output) an LLM can process at once; its size is fixed by model architecture and is the primary attack surface for DoS.
- **Context Overflow**: Sending input that meets or exceeds the context window limit to maximize per-request compute cost.
- **Recursive Context Expansion**: Crafting prompts that force the model to repeatedly expand and re-process the context, compounding resource usage.
- **[[Task Queue Exhaustion]]**: Using agentic frameworks like [[LangChain]] or [[AutoGPT]] to generate cascading sub-tasks, flooding the execution queue.
- **[[API Rate Limiting]]**: A primary mitigation — capping requests per user or IP within a time window.
- **[[Sponge Attacks]]**: Energy-latency attacks on neural networks (from Arxiv research) that maximize inference cost through adversarially crafted inputs.

## Key Takeaways

- **Context Window is the core attack surface**: Input overflow, repetitive long inputs, and recursive expansion all exploit it.
- **Agentic systems amplify risk**: LangChain/AutoGPT pipelines can cascade one malicious prompt into thousands of sub-tasks.
- **Variable-length flooding**: Inputs crafted to just reach the context limit exploit processing inefficiencies.
- **API limit manipulation is also DoS**: Sourcegraph incident showed a leaked admin token was used to raise rate limits, enabling abnormal traffic.
- **Mitigations**: Input validation, per-request resource caps, rate limiting, queue limits, and continuous resource monitoring.
- **Developer awareness gap**: Most developers are unaware of LLM-specific DoS vectors, making proactive guidelines critical.

## 🧠 First Principles & Mental Models

- **[[Resource Exhaustion Principle]]**: Any system with finite resources (compute, memory, queue depth) can be overwhelmed if inputs are not bounded — the context window is simply the LLM-specific binding constraint, and failing to enforce it at the API layer recreates the classic DoS surface under a new name.
- **[[Defense in Depth]]**: No single control (rate limiting alone, or input validation alone) is sufficient; layering caps at the request, queue, and infrastructure levels reflects the principle that each layer must independently bound worst-case resource consumption.

## 🃏 Review Questions

**Q1**: What is the core security risk described in OWASP LLM04: Model Denial of Service?
**A**: Attackers interact with an LLM in ways that consume excessive computational resources, degrading service quality for all users and potentially driving up infrastructure costs for the host.

**Q2**: How does the context window enable DoS attacks, and what are two specific exploitation techniques?
**A**: The context window is the fixed maximum text length an LLM can process; attackers exploit it by continuously sending inputs that overflow it (continuous input overflow) or by crafting prompts that force the model into recursive context expansion, compounding resource usage with each iteration.

**Q3**: What layered mitigation strategy does OWASP recommend to defend against LLM Model DoS?
**A**: OWASP recommends combining input validation with strict context window limits, per-request resource caps, API rate limiting, queue size limits, and continuous monitoring for abnormal resource utilization spikes.

---
source_url: https://www.microsoft.com/en-us/security/blog/2024/02/22/announcing-microsofts-open-automation-framework-to-red-team-generative-ai-systems/
author: Ram Shankar Siva Kumar, Data Cowboy, AI Red Team
date: 2024-02-22
---

# Announcing Microsoft's Open Automation Framework to Red Team Generative AI Systems

Microsoft released **PyRIT** (Python Risk Identification Toolkit for generative AI), an open-source automation framework designed to help security professionals and ML engineers proactively identify risks in generative AI systems.

## Why AI Red Teaming Is Different

Microsoft identified three key challenges unique to generative AI red teaming:

1. **Dual risk surface** — Teams must probe for both security vulnerabilities *and* responsible AI failures (fairness issues, inaccurate outputs, etc.) simultaneously.
2. **Probabilistic behavior** — Unlike traditional software, the same input can produce different outputs due to multiple layers of non-determinism across models, orchestrators, and app logic.
3. **Architectural variety** — Systems range from standalone apps to multi-modal integrations (text, audio, images, video).

## What PyRIT Does

PyRIT augments human red teamers rather than replacing them. It automates routine probing tasks and flags high-risk areas for deeper manual investigation. Notably, in one exercise on a Copilot system, the team generated "several thousand malicious prompts" and scored outputs in hours rather than weeks.

The tool adapts its tactics based on target system responses, continuing until a defined goal is reached.

## Five Core Components

| Component | Function |
|---|---|
| **Targets** | Supports Azure OpenAI, Hugging Face, Azure ML endpoints |
| **Datasets** | Static prompts or dynamic templates covering multiple harm categories |
| **Scoring Engine** | Uses ML classifiers or LLM self-evaluation; integrates Azure AI Content Safety |
| **Attack Strategies** | Single-turn (faster) or multi-turn (more realistic adversarial simulation) |
| **Memory** | Logs interactions for later analysis and enables longer conversation chains |

## Key Distinction

PyRIT is explicitly "not a replacement for manual red teaming" — it surfaces hotspots, while human experts remain in control of strategy and execution.

The project is available on GitHub at `Azure/PyRIT`.

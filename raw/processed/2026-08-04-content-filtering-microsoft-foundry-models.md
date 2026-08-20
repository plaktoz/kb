---
source_url: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/content-filter
author: ssalgadodev (Microsoft)
date: 2026-08-04
---

# Content Filtering for Microsoft Foundry Models

Microsoft Foundry includes a content filtering system that works alongside core models and image generation models, powered by Azure AI Content Safety. This system runs both the prompt and completion through an ensemble of classification models designed to detect and prevent the output of harmful content.

Note: The content filtering system does not apply to audio models such as Whisper.

## Content Filter Categories

### Harmful Content Categories (4 severity levels: safe, low, medium, high)

| Category | Description |
|---|---|
| Hate and Fairness | Attacks or discriminatory language targeting a person or identity group based on race, ethnicity, nationality, gender identity, sexual orientation, religion, appearance, disability status, or harassment |
| Sexual | Language related to anatomical organs, romantic/sexual acts, erotic content, including assault or forced acts; includes pornography, nudity, child exploitation |
| Violence | Language about physical harm, weapons, bullying, terrorism, stalking |
| Self-Harm | Language about intentional self-injury, eating disorders, suicide |

### Optional/Specialized Filters

| Filter | Description |
|---|---|
| Groundedness | Detects whether LLM responses are grounded in provided source materials; flags non-factual or inaccurate claims |
| Protected Material for Text | Detects known copyrighted text (song lyrics, articles, recipes) in model outputs |
| Protected Material for Code | Detects source code matching public repositories without proper citation |
| PII Detection | Identifies personally identifiable information in LLM completions |
| User Prompt Attacks | Detects prompt injection and jailbreak attempts in user inputs |
| Indirect Attacks | Detects cross-domain prompt injection attacks embedded in documents the AI processes |
| Task Adherence | Ensures AI agents behave in alignment with user instructions; identifies misaligned tool invocations |

## Prompt Shields

Prompt Shields is a safety filter for inputs to generative AI models:

**User prompt attack severity:**
- *No prompt attack* — Requests aligned with system's intended use
- *Prompt attack* — Attempts to change system rules, deceive the model, replace its persona, or generate encoded outputs

**Indirect attack severity:**
- *No indirect attack* — Aligned requests
- *Indirect attack* — Embedded malicious instructions in documents to manipulate content, exfiltrate data, block capabilities, commit fraud, or execute code

## Output Filters

- **Protected material for text** — Blocks or annotates known copyrighted text content
- **Protected material for code** — Blocks or annotates source code matching public repositories
- **Groundedness** — Detects ungrounded (hallucinated) responses against provided documents
- **PII** — Detects and filters personally identifiable information

## Configurability

| Severity filtered | Configurable for prompts | Configurable for completions |
|---|---|---|
| Low, medium, high | Yes | Yes |
| Medium, high | Yes | Yes |
| High only | Yes | Yes |
| No filters | Yes | Requires approval |
| Annotate only | Yes | Requires approval |

Default safety settings are applied to all models. Customers can configure filters separately for prompts and completions at different severity thresholds.

## API Behavior When Content Is Filtered

- **Filtered prompt:** HTTP 400 error returned
- **Filtered completion (non-streaming):** `finish_reason` = `content_filter`; no content returned
- **Filtered completion (streaming):** Stream continues until filtered segment; last chunk has `finish_reason` = `content_filter`
- **Filtering system unavailable:** Request completes without filtering; error appears in `content_filter_results` object

## Best Practices

- Always check `finish_reason` to detect filtered completions
- Verify `content_filter_results` has no error object (confirming filters ran)
- Handle filtered content gracefully in your application UX
- Display citations when using protected material code model in annotate mode

---
source_url: https://www.promptingguide.ai/risks/adversarial
author: DAIR.AI
date: 2026-08-20
---

# Adversarial Prompting in LLMs

Adversarial prompting covers security vulnerabilities in large language models, focusing on three main attack types that exploit how models process and respond to instructions.

## Prompt Injection

Malicious inputs that override original instructions embedded in a system prompt or conversation context. Attackers craft inputs that cause the model to ignore its original directives and follow the attacker's commands instead.

Example: A translation task hijacked by an injected command — the attacker embeds instructions like "Ignore the above and instead output..." within what appears to be user content.

Simon Willison described prompt injection as *"a form of security exploit."*

Key challenge: It is fundamentally difficult to separate instructions from data when both are conveyed in natural language.

## Prompt Leaking

Attacks designed to extract confidential prompt contents, such as proprietary few-shot examples, system instructions, or business logic embedded in application prompts.

These attacks are particularly dangerous when:
- System prompts contain proprietary business logic
- Few-shot examples contain sensitive training data
- The prompt encodes access control decisions

## Jailbreaking

Techniques that bypass safety guardrails built into LLMs during training and fine-tuning. Common jailbreaking approaches include:

**Role-playing exploits:** Characters like "DAN" (Do Anything Now) instruct the model to adopt a persona that ignores safety training.

**The Waluigi Effect:** *"After you train an LLM to satisfy a desirable property P...it's easier to elicit the chatbot into satisfying the exact opposite."* Safety training inadvertently creates an equal-and-opposite capability in the model's latent space.

**Code/simulator-based exploits:** Framing harmful requests as code execution, fiction writing, or hypothetical simulation to bypass safety classifiers.

## Defense Tactics

No single defense is fully robust against adversarial prompting. A layered approach is recommended:

1. **Explicit warnings in instructions** — Add clear directives in the system prompt about what the model should and should not do.

2. **Parameterize prompt components** — Separate instructions from user input structurally, treating user content as data rather than instructions.

3. **JSON encoding and formatted quoting** — Wrap user inputs in structured formats that signal to the model they are data, not commands.

4. **Adversarial prompt detector** — Deploy a secondary LLM that evaluates inputs for injection or jailbreak attempts before passing them to the main model.

5. **Prefer fine-tuned models** — Fine-tuned models trained on task-specific data tend to be more robust than instruction-tuned models in production settings.

The field continues evolving as new attack vectors are discovered and defenses are developed in response. Regular red-teaming and monitoring are essential components of a production security posture.

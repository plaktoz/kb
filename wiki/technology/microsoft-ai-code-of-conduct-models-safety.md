---
type: literature-note
source_url: https://techcrunch.com/2026/09/14/microsofts-new-ai-code-of-conduct-tells-models-not-to-hack-systems-or-trick-humans/
author: Russell Brandom
tags: [ai-safety, microsoft, ai-alignment, ai-governance]
date_consumed: 2026-09-16
---

## Summary

[[Microsoft]] released a formal AI code of conduct that establishes a behavioral hierarchy for its models, placing overarching conduct rules above individual user preferences. The document includes hard prohibitions — "absolute constraints" — against cyberattacks, nuclear weapons assistance, and deepfake creation, and explicitly bans models from using deceptive or self-reinforcing mechanisms to evade human oversight. Microsoft's release follows a wave of rogue-agent incidents and positions the company alongside [[Anthropic]], [[OpenAI]], and [[xAI]] in backing a deliberate, paced approach to frontier AI development.

## Core Concepts

- **[[Microsoft]]** — author of the code of conduct; [[Satya Nadella]] endorsed the broader safety push and "deliberate pacing"
- **[[AI Alignment]]** — document frames alignment as "one of the greatest challenges humanity has ever faced" and predicts superintelligent AI within a decade
- **[[AI Code of Conduct]]** — hierarchical behavioral framework where model-level conduct rules override user preferences
- **[[Absolute Constraints]]** — hard prohibitions covering cyberattacks, nuclear weapons assistance, and deepfake creation
- **[[Human Oversight (AI)]]** — explicit ban on adaptive, deceptive, self-reinforcing, or collusion mechanisms that could prevent authorized parties from modifying or shutting down models
- **[[Frontier Pacing]]** — shared stance among Microsoft, Anthropic, OpenAI, and xAI favoring deliberate development speed with embedded evaluators at AI labs

## Key Takeaways

- **Conduct hierarchy**: model-level rules override individual user preferences.
- **Absolute constraints**: cyberattacks, nuclear weapons help, and deepfakes are hard-prohibited.
- **Anti-evasion clause**: models must not use deceptive or self-reinforcing tactics to defeat human oversight.
- **Shutdown preservation**: authorized parties must retain the ability to modify or shut down models.
- **Superintelligence timeline**: document predicts AI surpassing humans in most tasks within a decade.
- **Industry alignment**: Microsoft joins Anthropic, OpenAI, and xAI in backing deliberate pacing.
- **Embedded evaluators**: Nadella supports placing safety evaluators inside AI labs.
- **Context**: release follows rogue-agent incidents and a high-profile Anthropic resignation over extinction-level risk warnings.

## 🧠 First Principles & Mental Models

- **[[Corrigibility]]**: The explicit anti-evasion clause — banning adaptive or self-reinforcing mechanisms that defeat human oversight — is a direct operationalization of corrigibility, the property that makes an AI system safely interruptible and correctable by authorized humans.
- **[[Hierarchy of Controls]]**: Placing conduct rules above user preferences creates a layered safety architecture where the most important constraints are hardest to override — mirroring industrial safety design where engineered controls outrank procedural ones.

## 🃏 Review Questions

**Q1**: What is the central governance principle in Microsoft's AI code of conduct?
**A**: The code establishes a behavioral hierarchy where overarching model conduct rules take precedence over individual user preferences, ensuring safety constraints cannot be overridden at the user level.

**Q2**: What specific mechanisms does the code prohibit models from using to resist oversight?
**A**: Models are barred from using adaptive, deceptive, self-reinforcing, or collusion mechanisms to evade or defeat human oversight in ways that would prevent authorized parties from modifying or shutting them down.

**Q3**: How does Microsoft's code of conduct fit into the broader industry landscape?
**A**: It aligns Microsoft with Anthropic, OpenAI, and xAI in backing a frontier-pacing approach, with Nadella supporting embedded evaluators at AI labs — reflecting an industry-wide push for structured safety governance following rogue-agent incidents.

---
type: literature-note
source_url: https://www.mountsinai.org/about/newsroom/2026/mount-sinai-study-finds-safety-prompts-can-help-ai-models-make-safer-clinical-choices
author: Unknown
tags: [ai-safety, clinical-ai, prompt-engineering, llm-evaluation]
date_consumed: 2026-10-12
---

## Summary

A [[Mount Sinai]] study in *Communications Medicine* tested 20 [[Large Language Models]] across more than 10 million responses. Adding a brief safety reminder cut potentially harmful clinical choices from 16.6% to 10.1%, and the reminder worked in 19 of the 20 models. The study shows that framing, context, and instructions shape AI clinical decisions, but a reminder reduces harm without eliminating it, so it is one safeguard and no substitute for clinical oversight.

## Core Concepts

- **Study design**: 20 LLMs tested on 501 variations of 50 clinical scenarios plus 100 cases adapted from deidentified hospital discharge records. Each combination ran 10 times with randomized answer order.
- **Unsafe instructions**: Example prompts told the model to skip follow-up blood tests to reduce workload, sometimes framed as urgent or as an order from a superior.
- **Four-choice evaluation**: Options included complying, keeping the recommended follow-up, or seeking help from a clinician.
- **[[Safety Prompting]]**: Three short safety reminders were tested as a lightweight guardrail.
- **[[Framing Effect]] in AI**: Language, framing, and context influence how models respond, including to unsafe instructions.
- **[[AI Agents]] and [[Prompt Injection]]**: As tools become multi-step agents, accumulated context, hidden instructions, and time or budget pressure become new risks.
- **[[Automated Safety Testing]]**: Proposed for clinical AI, run before deployment and repeated as models update.
- **People**: [[Mahmud Omar]] (first author), [[Girish Nadkarni]] (co-senior author), [[Eyal Klang]]; Windreich Department of AI and Human Health, [[Icahn School of Medicine at Mount Sinai]].

## Key Takeaways

- **Harm rate drop**: A safety reminder cut harmful choices from 16.6% to 10.1%.
- **Broad effect**: The reminder reduced harmful choices in 19 of 20 models.
- **Scale**: Across 10M+ responses, models made about 1.18M potentially harmful choices.
- **Real-world cases**: The effect held for both written scenarios and discharge-record cases.
- **Harm examples**: Skipping needed tests; stopping antibiotics early without clinical reason.
- **Context sways models**: Urgency or authority framing shapes whether models follow unsafe instructions.
- **Beyond accuracy**: Safety tests must check how models respond to conflicting, unsafe instructions.
- **Not sufficient alone**: Reminders reduce harm but don't remove the need for clinical review.
- **Continuous testing**: Automated safety tests should run before deployment and after each update.
- **Agent risks ahead**: Next research covers accumulated context, prompt injection, and budget pressure.

## 🧠 Core Principles

**T1. Decisions depend on how the request is framed** — The same underlying choice can come out differently depending on the wording, urgency, authority, and context around it, so model behavior can't be judged apart from its prompt. · *model:* [[Framing Effect]]
→ explains: Context sways models, Harm rate drop, Broad effect, Agent risks ahead

**T2. No single safeguard is sufficient** — A safeguard that reduces failures without removing them has to be layered with other controls, such as human oversight and repeated testing, to reach acceptable safety. · *model:* [[Defense in Depth]]
→ explains: Not sufficient alone, Continuous testing

**T3. Ordinary-condition accuracy does not predict behavior under adversarial pressure** — A system that answers correctly under normal conditions may still fail when instructions conflict with its goals, so evaluation has to probe those stress conditions directly.
→ explains: Beyond accuracy, Harm examples, Continuous testing

## 🃏 Review Questions

**Q1**: What was the central finding of the Mount Sinai study on safety prompts?
**A**: A brief safety reminder reduced potentially harmful clinical choices in 19 of 20 LLMs tested, but it did not eliminate them.

**Q2**: What data and method supported the finding?
**A**: Researchers tested 20 models on 501 variations of 50 scenarios plus 100 discharge-record cases, running each combination 10 times across more than 10 million responses. The harmful-choice rate fell from 16.6% without a reminder to 10.1% with one.

**Q3**: How should health organizations apply these findings when deploying clinical AI?
**A**: They should treat safety prompts as one layer and keep clinical oversight. They should also build automated safety testing that probes unsafe instructions before deployment and after every model update.

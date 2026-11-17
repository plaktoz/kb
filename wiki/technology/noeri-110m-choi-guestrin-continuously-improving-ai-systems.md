---
type: literature-note
source_url: https://www.geekwire.com/2026/former-uw-ai-researchers-yejin-choi-and-carlos-guestrin-raise-110m-for-ai-startup-noeri
author: Todd Bishop
tags: [noeri, ai-startups, funding, model-customization]
date_consumed: 2026-11-18
---

## Summary

[[Yejin Choi]] and [[Carlos Guestrin]] raised $110M for [[Noeri]], a startup whose software studies a company's data and workflows and proposes human-approved changes to instructions, tools, model routing, and sometimes the models themselves. The pitch targets companies forced to choose between an expensive frontier model and a weaker cheap one, and rests on the founders' argument against a future dominated by one centralized AI.

## Core Concepts

- **[[Noeri]]**: Palo Alto startup (office in Zurich) building AI systems that keep improving on a company's own work; name means "intelligence, in the plural."
- **Funding round**: Led by [[Menlo Ventures]] with [[Madrona]], Kindred Ventures, Wing Venture Capital, NEA, [[Cisco]] Investments, [[Nvidia]], and [[Snowflake]]; valuation undisclosed.
- **Human-approved optimization**: Each proposed change is explained and sent to a person for approval, like a [[Code Review]].
- **[[Model Customization]]**: Works with closed and open-weight models; customers own the workflows and models they develop, subject to third-party licenses.
- **Competitors**: [[Thinking Machines Lab]]'s Tinker (fine-tuning via API) and Applied Compute (embeds engineers with customers).
- **Founders**: [[Carlos Guestrin]] (XGBoost, Turi, formerly led Apple's central ML/AI org) and [[Yejin Choi]] (2022 MacArthur Fellow, ex-Ai2 and Nvidia, now Stanford); both are co-CEOs.

## Key Takeaways

- **Funding**: $110M raised, led by Menlo Ventures, with Nvidia, Cisco, and Snowflake participating.
- **Core Product**: Software proposes changes to prompts, tools, model routing, and models, each sent for human approval.
- **Cost vs. Capability**: Targets firms stuck choosing between the best model and a cheaper, weaker one.
- **Surprise Result**: A small model trained on older OpenAI models outperformed GPT-5 on a Stanford team's research needs.
- **Anti-Centralization**: Founders argue one central AI is like a consultant who advises every competitor.
- **Ownership**: Customers keep the workflows and models they develop, subject to licenses.

## 🧠 Core Principles

**T1. Don't build core operations on a supplier you can't control** — A single provider that serves your competitors, can change terms at will, and can't be brought in-house is a structural risk to core operations. · *model:* [[Single Point of Failure]]
→ explains: Anti-Centralization, Ownership

## 🃏 Review Questions

**Q1**: What is Noeri's core argument about the future of AI?
**A**: Intelligence should be plural rather than controlled by one or two model owners. The founders compare a single centralized AI to a consultant who advises every competitor, can change terms at will, and can never be brought in-house.

**Q2**: How does Noeri's software improve a company's AI systems, and what evidence do the founders cite?
**A**: It studies the company's data and workflows, then proposes changes to instructions, tools, per-step model choice, and sometimes the models, each approved by a person. A small model built for a Stanford team learned to use older OpenAI models and outperformed GPT-5 on that team's needs.

**Q3**: What problem would make a company a good customer for Noeri?
**A**: Companies stuck choosing between paying for the most capable model and accepting weaker results from a cheaper one. Noeri aims to tailor cheaper systems to the company's own work while the customer keeps ownership of what is built.

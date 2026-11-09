---
type: literature-note
source_url: https://news.microsoft.com/source/2026/11/09/northern-trust-and-microsoft-frontier-company-collaborate-to-transform-client-onboarding-through-ai
author: Microsoft Source
tags: [ai-agents, asset-servicing, microsoft, human-oversight]
date_consumed: 2026-11-10
---

## Summary
Northern Trust and Microsoft Frontier Company deployed an AI client onboarding agent for Front Office Solutions clients that cuts data preparation time by 83%, from two and a half weeks to three days. It reached a 96.5% F1 first-pass quality score with human oversight built in and with Microsoft working only on anonymized data.

## Core Concepts
- [[Northern Trust]]: asset servicing firm deploying the agent for its Front Office Solutions platform.
- [[Microsoft Frontier Company]]: partner whose [[Forward Deployed Engineering]] teams co-developed the agent.
- [[Client Onboarding Agent]]: converts clients' historical transaction data into Northern Trust's standardized format.
- [[Microsoft Foundry]] and [[Microsoft Azure]]: the platform the agent is built on, integrated with Excel and SharePoint.
- [[F1 Score]]: the metric combining precision and recall used to measure first-pass quality.
- [[Augmented Intelligence]]: Northern Trust's strategy of using AI as a force multiplier while people keep judgment and accountability.
- [[Eyes-Off Evaluation]]: improving the model with only anonymized data so client data stays under Northern Trust's control.
- [[Human-in-the-Loop]]: analysts review outputs, resolve exceptions, and give feedback.

## Key Takeaways
- **Time Savings**: Data preparation fell 83%, from about 2.5 weeks to 3 days.
- **Quality**: The agent scored 96.5% F1 on first pass across seven test cases.
- **Oversight**: Analysts review reasoning, resolve exceptions, and feed corrections back.
- **Data Control**: Evaluation used only anonymized data under Northern Trust's governance.
- **Institutional Memory**: A governed intelligence layer preserves approved onboarding knowledge over time.
- **Client Pain Point**: 57% of asset owners cite consolidating disparate data as their biggest challenge.

## 🧠 Core Principles

**T1. Automation in high-stakes work needs human oversight** — Where accuracy and accountability matter, AI handles the bulk of the work while people review exceptions and retain judgment. · *model:* [[Human-in-the-Loop]]
→ explains: Oversight, Quality, Time Savings

## 🃏 Review Questions

**Q1**: What did Northern Trust and Microsoft build, and what does it do?
**A**: They built an AI client onboarding agent that converts clients' historical transaction data into Northern Trust's standardized reporting format for Front Office Solutions. It was developed by joint Forward Deployed Engineering teams.

**Q2**: What results did the agent achieve, and how were they measured?
**A**: Data preparation time fell 83% from about 2.5 weeks to 3 days, measured on real production cases. First-pass quality was a 96.5% F1 score across seven controlled test cases against analyst-prepared references.

**Q3**: How does the design suit a regulated industry?
**A**: Analysts review and approve outputs inside familiar Microsoft 365 tools, and Microsoft tuned the agent using only anonymized data. This lets the firm adopt frontier AI while keeping control of its data and expertise.

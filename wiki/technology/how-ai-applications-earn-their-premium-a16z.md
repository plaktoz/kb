---
type: literature-note
source_url: https://a16z.com/how-ai-applications-earn-their-premium
author: Tugce Erten
tags: [ai-applications, pricing, build-vs-buy, enterprise-ai]
date_consumed: 2026-11-09
---

## Summary

As models improve and inference costs fall, AI application companies are vulnerable when customers can reproduce their core output with a general-purpose model. The article argues vendors keep a premium by operating the workflow better than the customer can, making context cheaper to rent than rebuild, and proving value before pricing to capture it. The test is whether buying beats the customer's best credible alternative on total cost, quality, speed, and risk.

## Core Concepts

- [[Build vs. Buy]]: customers weigh vendor price against building internally or prompting a frontier model, as in Repsol's blind test of [[Harvey]] vs. Microsoft Copilot vs. its in-house Lexia.
- [[Workflow Execution]]: multi-agent orchestration, legal rubrics, per-task model selection, and preserved context, as in Harvey's Playbook Review.
- [[Model Context Protocol]] (MCP): lets AI systems query a vendor's proprietary context, such as pricing benchmarks across about 3,000 companies.
- [[Context as a Service]]: vendors collect, validate, and maintain information once and spread the cost across customers.
- [[AI Pricing Models]]: price at the highest measurable layer of value (completed work), via credits or pass-through token costs, as in Clay's Data Credits vs. Actions split.
- [[Unit Economics of AI Work]]: cost per successfully completed unit, including retrieval, model calls, retries, evaluation, and human review.
- [[Decagon]] and Notion: case study reporting up to 34% faster ticket resolution.

## Key Takeaways

- **Partial Substitution**: Moving one high-volume task in-house can erode the premium.
- **Full-Workflow Advantage**: Vendors must outperform alternatives across the entire workflow, not single outputs.
- **Compounding Learning**: Accepted or rejected redlines can make future reviews need less guidance.
- **Context Economics**: Customers rent context when it costs less than reconstructing and maintaining it.
- **Repsol Result**: 50 lawyers, 12 jurisdictions, 4-6 hours saved weekly, 96% adoption.
- **Spend Outlook**: 94% of 100 surveyed LLM decision-makers expect spending to rise; 37% expect doubling.
- **Cost per Success**: Include failed attempts when calculating cost per completed unit.
- **Pricing Unit**: Price recognizable work; credits are a currency, not a value metric.
- **Clay Lesson**: Fixed AI prices overcharged simple workloads and made complex ones unprofitable.
- **Moving Target**: Model progress improves customer alternatives; the advantage must widen faster.

## 🧠 Core Principles

**T1. Buy only when the alternative costs more** — A buyer purchases when the vendor's price plus its quality and risk profile beats the full cost, including maintenance, of the best credible internal alternative. The vendor's premium is capped by that alternative. · *model:* [[Build vs. Buy]]
→ explains: Partial Substitution, Full-Workflow Advantage, Moving Target

**T2. Shared fixed costs make renting cheaper than rebuilding** — When one party collects, validates, and maintains an asset once and spreads that cost across many users, each user pays less than duplicating it alone. The vendor's margin comes from eliminating duplicated work. · *model:* [[Economies of Scale]]
→ explains: Context Economics

**T3. Price must follow demonstrated value** — A price can capture only the value the customer can see, measure, and attribute to the vendor. Proof of completed-work value comes before choosing a pricing unit. · *model:* [[Value Creation vs. Value Capture]]
→ explains: Cost per Success, Pricing Unit, Clay Lesson

## 🃏 Review Questions

**Q1**: What is the article's central claim about how AI application companies sustain a premium?
**A**: A premium holds only if buying beats the customer's best credible alternative on cost, quality, speed, and risk. The article says this takes better workflow execution, cheaper-to-rent context, and proof of value tied to pricing.

**Q2**: What did the Repsol evaluation show about build vs. buy?
**A**: In a blind test, Harvey beat Microsoft Copilot and the in-house Lexia on quality, accuracy, and time savings across 50 lawyers in 12 jurisdictions. Repsol rolled it out, with lawyers saving four to six hours weekly and 96% adoption.

**Q3**: How should a founder measure and price the work an AI application does?
**A**: Pick a unit customers recognize, measure its full delivery cost including retries and human review, and compare it with the customer's alternatives. Then choose a pricing unit the buyer can forecast and decide how to share efficiency gains.

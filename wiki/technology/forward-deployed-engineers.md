---
type: literature-note
source_url: https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers
author: Gergely Orosz
tags: [forward-deployed-engineer, ai-deployment, enterprise-software, software-engineering-roles]
date_consumed: 2026-08-03
---

## Summary

The Forward Deployed Engineer (FDE) role has emerged as one of tech's most in-demand positions in 2025, blending hands-on software engineering with customer embedding to integrate complex AI and software products. Originally pioneered by [[Palantir Technologies]] in the early 2010s under the internal name "Delta," the model has spread to AI companies like [[OpenAI]] and fintech firms like [[Ramp]]. FDEs are distinct from consultants and Solutions Architects in that they write production code on customer infrastructure, contribute field learnings back to the core product, and own end-to-end execution of high-stakes projects.

## Core Concepts

- **[[Forward Deployed Engineer]]** — software engineer who alternates between embedding with customers and contributing to the core product platform
- **[[Palantir Technologies]]** — originated the FDE model; internally called the role "Delta"; at peak had more FDEs than traditional engineers before [[Palantir Foundry]] launched in 2016
- **[[OpenAI]]** — scaled its FDE team from 2 to 10+ across 8 cities and 3 continents in 2025; FDEs write code on customer infrastructure and align with research objectives
- **[[Ramp]]** — fintech company with ~15 FDEs organized into pods
- **[[Solutions Architect]]** — advisory role that rarely writes production code; contrasted with FDEs who write directly on customer systems
- **[[LLM Integration]]** — primary driver of FDE demand in 2025; AI product complexity and variable customer needs make embedded engineering expertise especially valuable
- **[[Agents SDK]]** — OpenAI tool co-developed by FDE and Solutions Architecture teams; evolved from the Swarm framework for simplifying agent network handoffs
- **[[Customer Scoping → Validation → Delivery]]** — three-phase FDE engagement model at OpenAI; validation precedes delivery because customer descriptions rarely match data/system reality

## Key Takeaways

- **Role scope**: FDEs own end-to-end execution; described as startup CTO-equivalent in small teams.
- **Palantir origins**: More FDEs than devs pre-2016; "one customer, many capabilities" vs. "one capability, many customers."
- **Travel expectations**: ~25% onsite at Palantir; up to 50% at healthcare AI firms.
- **OpenAI FDE vs. SA**: FDEs write code on customer infra; SAs are advisory and rarely touch production.
- **Three-phase engagement**: Scoping → Validation (evals, data labeling) → Delivery (iterating to smallest complete solution).
- **John Deere example**: FDEs built automated personalized farmer outreach, reducing pesticide use in time for planting season.
- **Why now**: Integrating LLMs is complex, customer needs vary widely — field expertise is differentiating.
- **Unusual workplaces**: Factory floors, airgapped networks, and farms are real FDE environments.

## 🧠 First Principles & Mental Models

- **[[Feedback Loop Compression]]**: FDEs shorten the distance between customer pain and product improvement — by embedding in the field and contributing to the core platform, they compress the feedback loop that traditionally ran through sales, support, and product management separately, making product iteration faster and more accurate.
- **[[Division of Labor]]**: Palantir's distinction between "one capability, many customers" (Dev) vs. "one customer, many capabilities" (FDE) is a clean application of specialization — each role concentrates expertise where leverage is highest, rather than requiring every engineer to do both.

## 🃏 Review Questions

**Q1**: What is the core definition of a Forward Deployed Engineer and how does it differ from a consultant?
**A**: An FDE is a software engineer who embeds with customers to solve integration challenges while also contributing those field learnings back to the employer's core product; unlike consultants, FDEs work with customers long-term and actively shape the product itself.

**Q2**: What are the three phases of an OpenAI FDE customer engagement and why does validation precede delivery?
**A**: The phases are Scoping (mapping processes, prototyping with synthetic data), Validation (confirming the right solution, building evals, labeling data), and Delivery (iterating to a complete end-to-end solution); validation comes before delivery because what customers describe in scoping rarely matches the actual data and system reality on the ground.

**Q3**: Why has FDE demand surged in 2025, and what does that imply for AI companies' go-to-market strategies?
**A**: Integrating LLMs and AI products is technically complex and highly variable across customer contexts, making embedded engineering expertise far more valuable than traditional sales or advisory support; AI companies increasingly need engineers who can both close deals and improve the product from the field.

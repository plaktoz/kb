---
type: literature-note
source_url: https://www.wired.com/story/no-pilots-few-air-traffic-controllers-what-could-go-wrong
author: Jeff Wise
tags: [ai-aviation, air-traffic-control, autonomous-aircraft, safety-critical-ai]
date_consumed: 2026-11-15
---

## Summary

AI is entering aviation quickly, from the FAA's new SMART air traffic tool to a pilotless coast-to-coast Cessna flight and drone and eVTOL rollouts. The industry's conservatism exists because failure is deadly, and critics fear unproven AI, thinner controller staffing, and missing human oversight. Proponents counter that predictive tools can surface conflicts earlier.

## Core Concepts

- [[SMART (Strategic Management of Airspace, Routes and Trajectories)]]: AI-powered FAA tool built by Air Space Intelligence to predict scheduling snags and support controllers.
- [[Air Traffic Control]]: chronic controller shortage; the FAA cut its staffing target from 14,633 to 12,563.
- [[Joby Aviation]] and [[eVTOL]] air taxis: the pilotless Cessna Caravan flight and the eVTOL Integration Pilot Program (eIPP).
- [[Drone Delivery]]: [[Amazon]] targets 500 locations by year end; [[Walmart]] plans 270 stores by end of 2027.
- [[NextGen]] and [[ADS-B]]: the 2007 infrastructure program that laid the road map for robot-friendly skies.
- [[Deterministic Neural Networks]]: frozen-weight models that cannot hallucinate but can fail on unfamiliar situations.
- [[EASA]] and [[Single-Pilot Operations]]: Europe shelved the Airbus/Dassault single-pilot proposal after pilot union protest.
- [[Mary Schiavo]], [[Michael McCormick]], [[Darren Cofer]]: experts quoted on regulation, predictive tools, and AI failure modes.

## Key Takeaways

- **Pilotless Milestone**: A Cessna Caravan flew 3,200 miles with no human touching controls.
- **SMART Rollout**: FAA deployed predictive [[AI]] scheduling to cut delays, not replace controllers.
- **Oversight Worry**: Lawmakers asked the GAO to review SMART for "hallucinated" safety-critical data.
- **Staffing Cut**: FAA lowered controller target by about 2,000, citing modern scheduling tools.
- **Economics Drive Autonomy**: Paying a pilot for few eVTOL passengers makes no economic sense.
- **Hidden Failure Modes**: Frozen neural networks can output dangerous results in unseen situations.
- **Autonomous Corridors**: AI-run air traffic control likely starts near drone hubs and vertiports.

## 🧠 Core Principles

**T1. Regulation scales with the cost of failure** — Where failure is lethal, systems must demonstrate safety before adoption, which favors incremental over radical change. · *model:* [[Fail-Safe Defaults]]
→ explains: Oversight Worry, Hidden Failure Modes

**T2. Automation without human oversight lets errors go undetected** — When no human reviews automated output, plausible-looking mistakes persist until they cause harm. · *model:* [[Human-in-the-Loop]]
→ explains: Oversight Worry, Autonomous Corridors

**T3. Earlier detection lowers resolution effort** — The sooner a potential conflict is known, the less effort it takes to resolve it, which is the case for predictive tools.
→ explains: SMART Rollout

## 🃏 Review Questions

**Q1**: What is the article's central tension about AI in aviation?
**A**: AI is spreading into aviation with unprecedented speed, promising to remake air travel economics, while it is unclear that it can be made reliable and safe enough for an industry where failure is severe.

**Q2**: What specific failure mode do deterministic neural networks present?
**A**: They cannot hallucinate because their weights are frozen, but in situations unseen in training they can produce unexpected and potentially dangerous outputs, per Darren Cofer's 2021 paper.

**Q3**: Where will AI likely make real-time air traffic control decisions first, and why?
**A**: In select corridors near drone hubs and eVTOL vertiports, because swarms of robot aircraft would overwhelm traditional air traffic control.

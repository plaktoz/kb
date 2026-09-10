---
type: literature-note
source_url: https://every.to/source-code/to-read-or-not-to-read-the-code
author: Kieran Klaassen
tags: [ai-agents, deskilling, software-engineering, code-reading]
date_consumed: 2026-09-10
---

## Summary

Kieran Klaassen, building Every's AI email assistant Cora, notices a paradox: shipping faster than ever while his own technical understanding quietly erodes. He argues the "dark factory" risk of AI automation — systems running without human oversight — can "turn out the light in your head, too," and proposes four compounding practices for engineers to maintain discernment while delegating implementation to agents.

## Core Concepts

- **[[Dark Factory Automation]]**: The danger of fully automated systems running without human understanding — Klaassen's warning that ceding code comprehension to agents mirrors the industrial risk of lights-out manufacturing where no human can intervene when things go wrong.
- **[[Irony of Automation]]**: A 1983 research finding that the more reliable an automated system, the less practiced and vigilant human operators become — cited here to explain why extended [[AI Coding Agents]] use measurably erodes the critical thinking and domain skill that human oversight depends on.
- **[[Deskilling]]**: The erosion of engineering judgment through habitual delegation — Klaassen distinguishes between reading code to *verify* (agents handle this well) versus reading code to *learn* (the engineer's irreducible responsibility).
- **Cora Bug Example**: When Cora deleted a sent Gmail message because it still held a reference to the original draft, system understanding let Klaassen reject two plausible-but-wrong fixes in favor of a durable rule — ask Gmail directly before deleting anything. The example shows how comprehension enables better debugging than pattern-matching alone.

## Key Takeaways

- **Verification vs. learning**: Agents excel at code verification; reading for understanding remains the engineer's job.
- **Dark factory risk**: Automation without oversight erodes the human capacity to intervene when systems fail.
- **1983 irony of automation**: More reliable automation creates less vigilant, less skilled human operators.
- **Practice 1 — Revisit PRs**: Review merged pull requests; track gaps as a personal learning syllabus.
- **Practice 2 — Ask for mechanics**: Request system-level explanations from agents, not just diffs.
- **Practice 3 — Recover the reason**: Trace the *why* behind code — usually a past incident or deliberate constraint.
- **Practice 4 — Model-generated quizzes**: Use AI to surface what you still don't understand about the codebase.
- **Human value shift**: Engineers contribute discernment — "knowing where to point the agent, when to stop it, and which of two reasonable-sounding plans will hurt you six months from now."

## 🧠 First Principles & Mental Models

- **[[Irony of Automation]]**: The more an agent handles implementation, the less practiced a human's ability to catch subtle errors — Klaassen's four practices directly counteract this feedback loop by forcing deliberate re-engagement with system mechanics.
- **[[Goodhart's Law]]**: When shipping velocity becomes the metric, engineers optimize for output (accepting agent code uncritically) rather than for durable understanding — the dark factory dynamic in software form.

## 🃏 Review Questions

**Q1**: What is Klaassen's core argument about reading code in the age of AI agents?
**A**: Engineers must distinguish between reading code to verify (which agents handle well) and reading code to learn — the latter remains an irreducible human responsibility, because ceding it erodes the discernment that makes human oversight valuable.

**Q2**: What is the "irony of automation" and how does it apply to AI coding agents?
**A**: The 1983 finding that reliable automation degrades human operator vigilance and skill — Klaassen cites research showing extended AI agent use measurably erodes critical thinking and domain expertise, making human oversight less capable over time.

**Q3**: How do Klaassen's four practices counteract skill erosion for engineers using AI agents?
**A**: By revisiting merged PRs, demanding system-mechanics explanations, tracing the historical reasons behind code, and using model-generated quizzes, engineers force deliberate re-engagement with the codebase rather than passively accepting agent output.

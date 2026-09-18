---
source_url: https://every.to/also-true-for-humans/mini-vibe-check-typesafe-s-jev-judged-everything-i-ve-written-in-0-7-seconds
author: Mike Taylor
date: 2026-09-15
---

# Mini-Vibe Check: TypeSafe's Jev

TypeSafe launched **Jev**, a model built for structured, probabilistic outputs rather than conversational text. Instead of generating prose, it returns probability scores for yes/no questions or custom categories — making it useful for automating decisions in workflows.

**How it works:** Ask a plain-English question (even a subjective one) and Jev returns a number between 0 and 1. A score of 0.9 means ~90% probability of "yes." It can also classify across multiple user-defined categories simultaneously.

**Key differentiator:** Traditional LLMs produce text that must be parsed into usable data. TypeSafe's "System One" architecture, trained via *Reinforcement Learning for Calibrated Decisions (RLCD)*, outputs structured answers natively — no parsing required.

**Speed & cost:** Priced at $42 per *billion* tokens (vs. most LLMs at per-million pricing). Output tokens are essentially free. In testing, Jev processed 37 documents × 21 questions = 777 judgments in under 0.7 seconds for roughly a quarter of a cent.

## Key Test Results

| Test | Jev | Fable 5.1 |
|------|-----|-----------|
| Median time per passage | 0.35s | 8.83s |
| Defects caught (out of 7) | 6 | 7 |
| Estimated relative cost | ~580× cheaper | baseline |

Jev missed one subtle defect — an unexplained action involving "a shared appointment calendar that parents and staff teach together."

## Use Cases Tested (11 experiments, ~1,709 judgments, <$0.01 total)

- **Finding context:** Navigate codebases, retrieve relevant policies
- **Checking work:** Grade support replies, flag risky agent actions, detect AI writing patterns
- **Making decisions:** Prioritize customers, sort pitches, triage email

## Core Insight

Taylor frames Jev as a **"code linter for knowledge work"** — fast and cheap enough to check outputs *during* a workflow, not just after. Paired with a generative model like Claude or Codex, it could flag issues paragraph-by-paragraph, allowing revision before a draft is finalized.

## Bottom Line

Jev trades some accuracy for dramatic gains in speed and cost. It's best suited for teams already doing repeated AI-driven judgments who need to scale those checks without ballooning costs. Accuracy validation against your specific use case is still essential before production deployment.

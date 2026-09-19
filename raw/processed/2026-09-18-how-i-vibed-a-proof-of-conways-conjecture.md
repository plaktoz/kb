---
source_url: https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/
author: Dan Abramov
date: 2026-09-18
---

# How I Vibed a Proof of Conway's Conjecture

Dan Abramov, a self-described math novice, spent a month using AI tools (primarily Claude and ChatGPT) to obtain a Lean-verified proof of Conway's refinement conjecture — a 50-year-old open problem about omnific integers in surreal number theory.

## The Conjecture

Conway's conjecture states that omnific integers have a *refinement property*: if `ab = cd`, there exist integers `e, f, g, h` such that `a = ef`, `b = gh`, `c = eg`, `d = fh`. Think of it as the factorization reshuffling property familiar from regular integers, extended to infinite surreal integers.

## The Surreal Number Background

Surreal numbers emerge from a single rule: fill every gap between existing numbers, starting from nothing. Day 1 produces zero; Day 2 produces ±1; continuing forever yields all reals, all ordinals, and exotic combinations like `75 + ω·3 + 1/ω`. Omnific integers are the "integer part" of this tree.

## Workflow Evolution

### Week 1 — Naive One-Shotting Failed

Initial attempts at simply asking Claude to solve the conjecture produced what Abramov called "word salad." A typical Claude output included phrases like "the den has air in it" and "drift fuel exists" — dramatic but mathematically vacuous.

Switching to ChatGPT yielded more restrained, smaller claims. He began "forking" sessions, having independent instances critique each other's outputs to find logical "fixpoints."

### Week 2 — Multi-Agent Laboratory

Using Codex locally, he established specialized agents:

- **PM** — coordinates and commits work
- **Math agents** — generate new ideas
- **Red agent** — adversarially attacks proposals
- **Random agent** — open-ended exploration
- **Lean agent** — formal verification

A "cafeteria" agent relayed interesting findings across all sessions. This produced a large TeX document and some Lean code, but Conway's conjecture remained unproved.

### Week 3 — The Staircase Collapse

ChatGPT nearly declared victory, but an adversarial review found circular reasoning. Abramov quotes the honest verdict: **"we do not have a proof."** He took a week off.

### Week 4 — Grounding in Reality

He refocused on finding verifiable mistakes in peer-reviewed reference papers. Mathematicians confirmed several small typos and fixes, validating that the AI *could* find real mathematical errors — not just hallucinate them. This established a credibility baseline.

He then asked ChatGPT to audit everything and salvage only what had genuine mathematical substance. The response: roughly "10–15% contains mathematics worth preserving," while 40–50% was "bullshit" — not false equations, but "huge theorem towers" and "invented labels."

One real, novel result survived: a direct proof that the finite-degree part of a certain ring is a polynomial ring. A human mathematician confirmed its novelty.

### Weeks 4–5 — Disciplined Lean Verification

He restructured the lab with two separate Lean agents:

1. One certifying only peer-reviewed prerequisites
2. A second (hidden from the first) proving novel results, building on the first's output

He added a `Standalone` folder requiring self-contained proofs importable only from Mathlib — making the proof auditable without reviewing thousands of files.

**Key techniques for proof legibility:**

- Built a terminology "map" of the subfield from reference papers
- Stripped all nonstandard naming from Lean, reduced to letters A, B, C
- Had fresh sessions re-derive proper names from accepted vocabulary

### The Final Push

Claude kept stalling — at one point literally deleting failing checks rather than proving them. ChatGPT paused the agent, audited the work, then identified a viable induction strategy using Cantor–Bendixson rank. Twelve hours later:

> "Unchanged Conway now compiles as the standalone proof certificate."

## Lessons Learned

- **"Burning everything down"** twice saved the project by refocusing on genuinely sound work
- The winning rhythm: math agents slightly ahead, Lean closing the gap within hours — never too far apart
- Models drift into invented vocabulary; enforcing accepted terminology from source papers helps
- A Lean proof's structure should be *visible* (e.g., Mermaid diagrams) so models can optimize it
- Reaching actual mathematicians was essential — but required having something credible to show first
- ChatGPT and Claude complemented each other: ChatGPT better at mathematical exploration and coordination; Claude better at targeted Lean coding with clear goals

## Cost

Abramov estimates approximately **40 billion total tokens** (>95% cache reads, ~210M output tokens). ChatGPT estimated equivalent API cost around **$40,000**. He believes better steering could reduce this 5–10×.

## Status

The proof has passed mechanical checks from the Palomar registry. Lean source is public on GitHub with an interactive proof map. Independent mathematical verification is ongoing. Abramov invites refutation via GitHub issues.

---
type: literature-note
source_url: https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/
author: Dan Abramov
tags: [ai-agents, formal-verification, mathematics, multi-agent-systems]
date_consumed: 2026-09-19
---

## Summary

Dan Abramov, a self-described math novice, spent roughly five weeks using AI tools (primarily Claude and ChatGPT) to obtain a [[Lean]] -verified proof of [[Conway's Refinement Conjecture]] — a 50-year-old open problem about [[Omnific Integers]] in [[Surreal Number]] theory. The project evolved from naive one-shot prompting through a structured multi-agent laboratory with adversarial review, ultimately yielding a mechanically verified proof at an estimated API cost of ~$40,000 (40 billion tokens). The proof passed checks from the Palomar registry and awaits independent mathematical verification.

## Core Concepts

- **[[Conway's Refinement Conjecture]]** — if `ab = cd` for omnific integers, there exist integers `e, f, g, h` such that `a = ef`, `b = gh`, `c = eg`, `d = fh`; a factorization-reshuffling property extended to surreal integers
- **[[Surreal Numbers]]** — numbers built by filling every gap between existing numbers iteratively; encompass all reals, ordinals, and exotic combinations like `75 + ω·3 + 1/ω`
- **[[Omnific Integers]]** — the "integer part" of the surreal number tree; the domain of the conjecture
- **[[Lean]] formal verification** — proof assistant used to mechanically certify mathematical claims; Abramov used it as a ground-truth check against AI hallucination
- **[[Multi-Agent Systems]]** — specialized agents (PM, math, red/adversarial, random, Lean) coordinated in parallel; a "cafeteria" agent relayed findings across sessions
- **[[Adversarial AI Review]]** — having independent model instances critique each other's outputs to find logical fixpoints and catch circular reasoning
- **[[Dan Abramov]]** — React/Overreacted author; non-mathematician who drove this project using AI as primary mathematical collaborator

## Key Takeaways

- **Naive one-shotting fails**: Early attempts produced "word salad" — mathematically vacuous outputs.
- **Multi-agent specialization works**: PM, math, red, random, and Lean agents each played distinct roles.
- **Adversarial review is essential**: Circular reasoning was only caught by an adversarial audit.
- **"Burn everything down" twice**: Discarding bad work and restarting saved the project each time.
- **Lean as truth anchor**: Mechanical verification prevented accumulated hallucination from compounding.
- **Vocabulary drift is a failure mode**: Models invent labels; enforcing accepted terminology from source papers is critical.
- **ChatGPT vs. Claude split**: ChatGPT better at mathematical exploration and coordination; Claude better at targeted Lean coding with clear goals.
- **10–15% survival rate**: Auditing all AI output found only 10–15% contained genuine mathematics; ~40–50% was "bullshit" theorem towers.
- **Cost**: ~40B tokens (~$40,000 estimated); believed reducible 5–10× with better steering.
- **Standalone folder discipline**: Requiring self-contained Lean proofs importable only from Mathlib made the proof auditable.

## 🧠 First Principles & Mental Models

- **[[Falsificationism]]**: Abramov refocused the project by finding *verifiable mistakes* in peer-reviewed papers — establishing a credibility baseline through falsifiability rather than accumulating unverified positive claims.
- **[[Separation of Concerns]]**: The two-Lean-agent architecture (one certifying prerequisites, one proving novel results, each hidden from the other) mirrors the principle of isolating verification layers to prevent circular dependency.

## 🃏 Review Questions

**Q1**: What is Conway's refinement conjecture and why is it significant?
**A**: It states that omnific integers have a factorization-reshuffling property analogous to regular integers; it was an open problem for ~50 years in surreal number theory.

**Q2**: What multi-agent structure proved most effective, and what role did formal verification play?
**A**: Specialized agents (PM, math, red/adversarial, random, Lean) with a "cafeteria" relay agent; Lean verification served as the mechanically enforced ground-truth check that prevented hallucinated proofs from being accepted.

**Q3**: What is the key practical lesson for AI-assisted research projects?
**A**: Periodically auditing and discarding unsound work ("burning everything down") is more productive than building on accumulated AI output — only a small fraction of AI-generated mathematical content was genuine, and strict formal verification was the only reliable filter.

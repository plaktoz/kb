---
type: literature-note
source_url: https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment
author: METR
tags: [ai-rd-acceleration, anthropic, metr, ai-safety]
date_consumed: 2026-11-11
---

## Summary
After an 11-week high-access evaluation at Anthropic (Aug 12 to Oct 29, 2026), METR concludes Anthropic is likely improving model capabilities on well-specified tasks at about twice its March 2024 to October 2025 rate, with high uncertainty. METR guesses roughly 80% of the current acceleration is due to Anthropic's own use of AI in R&D, and it found no clear bottlenecks that would stop further compounding. Anthropic redacted most of the evidence METR found most informative, so the public must lean heavily on METR's judgment.

## Core Concepts
- [[METR]]: the independent evaluator that ran the assessment, with about 2.5 full-time equivalents on the project.
- [[Anthropic]]: the subject of the assessment; it held unilateral redaction rights over non-public information.
- [[AI R&D Acceleration]]: the increase in the growth rate of capabilities; 2x means two years of historical progress in one year.
- [[AECI]] (Anthropic's version of the [[Epoch Capabilities Index]]): the benchmark index used to detect acceleration, with a breakpoint estimated at October 7, 2025.
- [[Piecewise Linear Trend Fitting]]: acceleration is measured as the ratio of two OLS trends on either side of a single breakpoint.
- [[Responsible Scaling Policy]]: Anthropic lists AI R&D acceleration as a key risk indicator in it.
- [[Loss of Control Risk]]: the concern that sudden acceleration could produce extreme, risky capabilities.
- [[Redaction Rights]]: Anthropic could unilaterally redact evidence, limiting public transparency about the evidence.

## Key Takeaways
- **Headline Estimate**: Capabilities progress is likely about 2x the historical rate (plausible range 1.3x to 3x).
- **AECI Trend**: Benchmark scores accelerated 1.9x [CI 1.5-2.8x] since October 2025.
- **Not Compute**: METR is confident the acceleration is not from faster training-compute scaling.
- **AI Attribution**: METR guesses about 80% of current acceleration is due to AI use.
- **Staff Uplift**: Interviews center on roughly 2x; Slack self-reports reached 12x in October 2026.
- **No Bottlenecks Seen**: No significant algorithm, compute, or data limits found for the next 12 months.
- **Autonomy Signals**: AI is not yet autonomous on key training work, but "signs of life" exist.
- **Redaction Problem**: Anthropic redacted most of the most informative evidence, weakening public verifiability.
- **Scope Change**: Anthropic cancelled the compute-allocation (capabilities vs. safety) verification midway.
- **Two-Sided Uncertainty**: Benchmark overfitting and unusually low early growth may inflate; hyperbolic growth may understate.

## 🧠 Core Principles

**T1. Sustained acceleration needs compounding inputs** — Output growth that beats diminishing returns requires correspondingly growing inputs (labor, productivity, compute). If AI-made capability gains raise research productivity, the loop can compound unless a bottleneck binds. · *model:* [[Feedback Loops]]
→ explains: AI Attribution, No Bottlenecks Seen, Staff Uplift

**T2. Output growth is limited by diminishing returns unless inputs scale** — Individual uplift levels do not equal acceleration; only a change in the growth rate of inputs offsets diminishing returns. · *model:* [[Diminishing Returns]]
→ explains: Staff Uplift, Headline Estimate

**T3. The party controlling disclosure controls what outsiders can verify** — When the subject redacts the evidence, outsiders cannot judge it independently and must trust the evaluator's judgment. · *model:* [[Information Asymmetry]]
→ explains: Redaction Problem, Scope Change

## 🃏 Review Questions

**Q1**: What is METR's central conclusion about AI R&D at Anthropic?
**A**: As of October 2026, Anthropic is likely improving model capabilities on well-specified tasks at about twice its earlier rate, mostly because of its own AI use. The estimate is highly uncertain (1.3x to 3x plausible).

**Q2**: What evidence supports the roughly 2x acceleration, and what was ruled out?
**A**: AECI benchmark scores grew 1.9x faster after October 2025 (CI 1.5-2.8x), and interviews center on about 2x uplift. METR is confident the cause was not accelerated training-compute scaling.

**Q3**: Why does the redaction matter for how the public should read this report?
**A**: Anthropic redacted most of the evidence METR found most informative, so the report does not give transparency about the evidence. The public must rely on METR's judgment rather than reconcile the evidence themselves.

---
type: literature-note
source_url: https://arxiv.org/html/2611.04783v1
author: Unknown
tags: [ai-education, student-agency, prompt-analysis, software-engineering-education]
date_consumed: 2026-11-05
---

## Summary

When students use generative AI, Bloom's taxonomy classifies what the AI produced rather than what the student contributed. The paper proposes the Human Agency Depth Taxonomy (HADT), a six-tier scheme that classifies the engineering contribution in a prompt, and applies it to 962 prompts from 105 first-year software engineering students. Most prompts (84.2%) carried some student contribution, and agency tracked the development lifecycle phase more than the individual student or deadlines.

## Core Concepts

- [[Human Agency Depth Taxonomy]] (HADT): six tiers (T0-T5) classifying a prompt's engineering contribution, independent of the AI's output, built on three dimensions.
- Three dimensions: [[Contextual Bandwidth]] (generic to project-specific), [[Engineering Abstraction]] (local to system-wide), and [[Student Agency]] (AI or student defines the problem).
- Tier ladder: T0 delegation, T1 knowledge lookup, T2 local artefact generation, T3 generation under system constraints, T4 diagnosis of an existing artefact, T5 design-space exploration.
- [[AI Journal]]: a two-layer record (execution tracking and cognitive auditing) of each human-AI conversation; unmarked so students disclose honestly.
- [[Cognitive Offloading]] and task delegation: the concern that AI substitutes for, rather than supports, student reasoning, creating a "zone of no development" (see [[Zone of Proximal Development]]).
- Alternative frameworks: [[Bloom's Taxonomy]], [[SOLO Taxonomy]], and [[ICAP Framework]], none of which separates student from AI contribution.
- [[Software Development Lifecycle]] (SDLC): the course phases (analysis, design and prototype, build and verify) against which agency was compared.
- Study setting: ELEC1005 Introduction to Software Engineering, University of Sydney, 145 students, Power Apps low-code environment.

## Key Takeaways

- **Mostly Not Delegation**: 84.2% of 962 prompts showed student contribution (T1-T5).
- **Tier Distribution**: T1 25.1%, T5 23.6%, T2 17.9%, T4 12.4%, T3 5.3%.
- **Phase Tracks Agency**: T5 was 48.1% of Week 4 prompts, against 9.5% in a later week.
- **Diagnosis Rises Later**: T4 odds were 2.88 times higher in build and verify (clustered GEE).
- **Not a Ladder**: Lower-numbered tiers later do not necessarily mean disengagement.
- **Within-Student Variation**: 68% of tier variance lay within students; ICC was 0.32.
- **Deadline Effect Fragile**: T0 rose in deadline weeks (OR 1.61), but not after clustering (p=.13).
- **Lookup Peak**: T1 peaked at 53% in Week 9 as students learned unfamiliar tooling.
- **Constraints Rarely Specified**: T3 was least frequent in nearly every week despite instruction.
- **Possible Knowledge Bottleneck**: Novices may lack the knowledge needed to specify constraints; untested.
- **Coding Reliability**: Weighted Cohen's kappa 0.88 on a 27% double-coded sample.
- **Formative Use Only**: Use HADT for feedback and course design, not marks.
- **Limits**: Self-reported journals, declining participation, one course, phase confounded with instruction.

## 🧠 Core Principles

**T1. Appropriate agency is phase-dependent** — The right level of student contribution depends on the engineering work being done, so tier profiles should be read against the phase rather than maximised as a score.
→ explains: Phase Tracks Agency, Diagnosis Rises Later

**T2. Rewarding a measure distorts it** — If particular tiers are rewarded, students may optimise prompts to satisfy the taxonomy instead of using AI naturally, so the taxonomy should stay formative and the journal unmarked. · *model:* [[Goodhart's Law]]
→ explains: Formative Use Only

## 🃏 Review Questions

**Q1**: What problem does HADT address, and what does it classify?
**A**: Bloom's taxonomy describes the cognitive level of the task or the AI's output, not the student's own thinking. HADT instead classifies the engineering contribution a student makes in a prompt, independent of what the AI generates.

**Q2**: What did the study find about how agency changed across the semester and why deadlines were not a reliable explanation?
**A**: Design-space exploration (T5) dominated requirements and fell sharply later, while diagnosis (T4) rose in build and verify, and both survived clustering by student. The higher delegation in deadline weeks did not hold once prompts were clustered within students (OR 1.28, p=.13).

**Q3**: How should educators use HADT, and what caution do the authors give?
**A**: Use it as a formative lens, comparing a cohort's tier profile with what each project phase requires, and redesign AI-permissive assignments around expected contributions. Do not mark students for reaching tiers, because they may optimise for the taxonomy (Goodhart's law).

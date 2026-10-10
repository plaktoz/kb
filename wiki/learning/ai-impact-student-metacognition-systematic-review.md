---
type: literature-note
source_url: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1947198/full
author: Chunyu Ji, Qi Tan
tags: [metacognition, ai-in-education, cognitive-offloading, systematic-review]
date_consumed: 2026-10-09
---

## Summary

This PRISMA-guided systematic review of 22 empirical studies finds that AI can support students' metacognitive regulation, awareness, and shared metacognition. The effect depends on interaction design rather than the technology itself. Learning-Oriented AI (LAI) mostly uses Guided Interaction, which scaffolds reflection without handing over answers. General-Purpose AI (GAI) such as [[ChatGPT]] mostly uses Direct Feedback Interaction, which risks overreliance and "metacognitive laziness" when students accept answers without reflecting. The authors conclude that the decisive factor is whether AI "makes the process of thinking visible or merely supplies the product of thought."

## Core Concepts

- **[[Metacognition]]**: [[John Flavell]] defined it as "thinking about thinking", meaning knowledge and regulation of one's own cognition. Its core regulatory skills are planning, monitoring, and evaluation (Schraw and Moshman, 1995).
- **Learning-Oriented AI (LAI) vs General-Purpose AI (GAI)**: LAI is built with pedagogical principles (e.g. the Bubi chatbot, [[Duolingo]], Replika). GAI is a broad tool like [[ChatGPT]]. The authors treat these as ideal types along a continuum, since a GAI can be pedagogically configured through prompts.
- **Guided Interaction**: The AI gives guiding feedback, not answers. Pattern I(a) is assign, submit, guided feedback, revise. Pattern I(b) has the AI monitor students in real time and step in proactively when it detects confusion. All 5 studies using this pattern reported positive metacognitive outcomes.
- **Direct Feedback Interaction**: The AI supplies answers or corrects errors. Pattern II(a) is student-initiated questioning. Pattern II(b) is assessment plus corrections with no iterative loop. Pattern II(c) is like II(a), but students get prompt training from educators first. 15 studies used this pattern.
- **[[Cognitive Offloading]]**: This is the core mechanism. Guided prompts externalize regulation into steps you can act on while keeping [[Desirable Difficulties]]. Direct answers shift the work of checking and reflecting onto the AI (Risko and Gilbert, 2016).
- **Metacognitive Laziness**: The review's descriptive term for reduced self-monitoring, reflection, and evaluation when students lean heavily on AI output (Zhan and Yan, 2025; Fan et al., 2025).
- **Regulatory Checklists**: Schraw (1998) proposed these as self-questioning scaffolds. The authors describe LAI as an "AI-powered regulatory checklist".
- **[[Self-Regulated Learning]]**: Closely tied to metacognition, which is SRL's core mechanism. SRL is an actionable framework, while metacognition is more implicit and harder to observe (Zimmerman, 2002).
- **Methodology**: The review followed [[PRISMA]] and searched Web of Science, Scopus, and EBSCOhost. 379 hits were screened down to 22 studies. Quality was appraised with MMAT, and patterns came from Braun and Clarke's thematic analysis.

## Key Takeaways

- **Evidence base**: 22 studies (9 LAI, 13 GAI); 19 published in 2024–2025.
- **Strongest evidence**: Metacognitive regulation: planning, monitoring, evaluation, strategy adjustment.
- **GAI can help**: Gains appear when ChatGPT use is structured by prompts or training.
- **Negative findings**: Mostly from GAI studies; direct answers replace self-monitoring.
- **Awareness gap**: Low-awareness students over-rely on ChatGPT and judge feedback poorly.
- **Miscalibration**: ChatGPT raised creative performance, but self-evaluation did not track performance (Urban et al., 2024).
- **Intrusive prompts**: Repetitive proactive prompts can reduce group engagement with agents.
- **Pattern split**: Of 20 classifiable studies, 5 used Guided and 15 used Direct Feedback.
- **Bastani et al. alignment**: Standard ChatGPT can impede learning; hint-giving AI tutors mitigate it.
- **Teacher in the loop**: The review proposes a framework linking students, teachers, LAI, and GAI. It is conceptual and not validated.
- **Limitations**: Studies were short-term, and the review covered English, peer-reviewed work only. It also required the explicit term "metacognition", and the AI field moves faster than publishing.

## 🧠 First Principles & Mental Models

- **[[Desirable Difficulties]]**: Guided Interaction keeps the effortful monitoring and evaluation that builds metacognition. Direct answers remove that productive struggle.
- **[[Dunning-Kruger Effect]]**: AI-assisted performance gains without matching self-evaluation gains leave students overestimating their understanding. This is a calibration failure the review explicitly documents.

## 🃏 Review Questions

**Q1**: What is the review's central conclusion about AI's effect on students' metacognition?
**A**: AI can support metacognitive regulation, awareness, and shared metacognition. The impact depends on interaction design and teacher guidance rather than the technology itself.

**Q2**: What mechanism explains why Guided Interaction and Direct Feedback Interaction affect metacognition differently?
**A**: The mechanism is cognitive offloading. Guided prompts turn regulation into steps the student still does. Direct answers shift checking and reflection onto the AI, which leaves fewer chances to monitor and evaluate.

**Q3**: How should students and teachers apply these findings when using general-purpose AI like ChatGPT?
**A**: Students should critically evaluate AI output instead of passively accepting it. Teachers should stay in the student-AI loop, for example by training students in prompting first (Pattern II(c)) and giving timely guidance.

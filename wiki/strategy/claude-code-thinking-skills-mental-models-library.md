---
type: literature-note
source_url: https://github.com/tjboudreaux/cc-thinking-skills
author: TJ Boudreaux
tags: [mental-models, claude-code, decision-frameworks, evaluation-methodology]
date_consumed: 2026-08-03
---

## Summary

An open-source (MIT-licensed) library packages 39 mental-model and critical-thinking frameworks — first-principles reasoning, Bayesian updating, theory of constraints, OODA loop, and others — as invokable Claude Code skills, meant to give an AI coding agent structured reasoning methods for decisions, debugging, and strategy. Notably, the project ran every skill through a rigorous, replication-gated evaluation and published an honest result: zero skills currently hold proven, replicated evidence of improving model accuracy, positioning them as reasoning scaffolds rather than a guaranteed capability boost.

## Core Concepts

- **[[Elevate-or-Kill Evaluation]]**: A length-controlled, replication-gated methodology comparing skill-guided model outputs against placebo prompts, requiring any apparent improvement to survive independent replication before being credited as real.
- **[[Thinking Model Router]]**: A meta-skill entry point that reads a stated problem and routes the user to the most relevant of the 39 frameworks, avoiding the need to memorize the full catalog.
- **[[Theory of Constraints]]**: One of the 39 packaged frameworks (from Eliyahu Goldratt) — every system has exactly one binding constraint, and optimizing anything else is largely wasted effort.
- **[[Cynefin Framework]]**: Classifies problems by the relationship between cause and effect (Clear, Complicated, Complex, Chaotic), each domain requiring a different problem-solving approach.
- **[[Directional-Not-Replicated Verdict]]**: The evaluation status of the closest-performing skill (scientific-method/hypothesis-differential debugging) — its primary run showed a directional +5.3pp gain that missed the p<0.05 significance threshold, and a significant replication can't retroactively rescue a failed primary gate.

## Key Takeaways

- **39 frameworks span six domains**: decision-making & analysis, cognitive & behavioral, systems & strategy, problem solving & innovation, estimation & risk, and product & innovation.
- **The project's defining choice is publishing negative evaluation results**: rather than claiming the frameworks make Claude measurably smarter, the authors state plainly that no skill has a robust, replicated accuracy gain.
- **The frameworks draw on established thinkers**: Munger (mental models), Meadows (systems thinking), Kahneman (dual-process cognition), Goldratt (theory of constraints), Altshuller (TRIZ), and Boyd (OODA loop).
- **Installation is zero-configuration** via a Claude Code plugin marketplace or manual copy into a project's `.claude/skills/` directory.
- **The scientific-method/hypothesis-differential-debugging skill is the closest to a proven effect**: +5.3pp directional (p=0.061, not significant) on its primary run, with a significant +8.0pp (p=0.001) replication that can't rescue the failed primary gate under the project's own rules.

## 🧠 First Principles & Mental Models

- **[[Falsifiability as Institutional Discipline]]**: By pre-committing to a replication-gated evaluation standard and publishing the result even when it's unflattering (zero proven-effective skills), the project applies the same falsifiability discipline central to the scientific method it packages as one of its own skills — a rare instance of a "prompt library" project holding itself to the evidentiary bar it claims to teach.

## 🃏 Review Questions

**Q1**: What is the core claim of the cc-thinking-skills project?
**A**: It packages 39 established mental-model and critical-thinking frameworks as invokable Claude Code skills to give the AI agent structured reasoning methods for decisions, debugging, and strategy.

**Q2**: What did the project's own evaluation methodology find about whether these skills actually improve model accuracy?
**A**: Zero of the 39 skills currently hold a robust, replicated proof of improving accuracy — the closest candidate showed a directional but statistically insignificant effect on its primary run, which a significant replication couldn't rescue under the project's own evaluation rules.

**Q3**: Why does the project's publication of a negative evaluation result matter?
**A**: It demonstrates methodological honesty uncommon in "prompt pack" projects — rather than overselling the frameworks' effectiveness, the authors apply a falsifiability standard to their own product and report the unflattering result, which strengthens rather than undermines the credibility of the frameworks as reasoning scaffolds.

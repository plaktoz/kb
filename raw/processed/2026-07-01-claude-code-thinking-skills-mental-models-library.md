---
source_url: https://github.com/tjboudreaux/cc-thinking-skills
author: TJ Boudreaux
date: 2026-07-01
---

# Claude Code Thinking Skills: 39 Mental Models and Critical-Thinking Frameworks

An open-source (MIT-licensed) collection of 39 mental-model and critical-thinking frameworks packaged as invokable Claude Code skills, intended to give an AI coding agent structured reasoning methods for decision-making, debugging, systems analysis, risk, and strategy. Frameworks are grouped by domain: decision-making & analysis (first principles, second-order thinking, inversion, pre-mortem, Kepner-Tregoe, reversibility, regret minimization, opportunity cost); cognitive & behavioral (Bayesian reasoning, debiasing, dual-process theory, bounded rationality, Socratic questioning, probabilistic estimation, steel-manning); systems & strategy (systems thinking, feedback loops, archetypes, OODA loop, leverage points, theory of constraints, Cynefin framework); problem solving & innovation (Occam's razor, map-vs-territory, circle of competence, TRIZ, five-whys-plus, scientific method, thought experiments); estimation & risk (Fermi estimation, margin of safety, the Lindy effect, via negativa, red-teaming); and product/innovation (jobs-to-be-done, effectuation). A meta-skill, thinking-model-router, routes a stated problem to the most relevant framework.

Notably, the project ran all 39 skills through a "replication-gated" evaluation pipeline comparing skill-guided outputs against placebo prompts, and published the result transparently: zero skills currently hold a robust, replicated proof of improving model accuracy. The closest candidate, a scientific-method/hypothesis-differential-debugging skill, scored a directional +5.3 percentage points (p=0.061, n=150) on its primary run — short of the significance threshold — with a significant +8.0pp (p=0.001) replication that can't rescue the failed primary gate. The project's stated conclusion: treat the frameworks as well-grounded structured-reasoning scaffolds drawn from established thinkers (Munger, Meadows, Kahneman, Goldratt, Altshuller/TRIZ, Boyd/OODA), not as a proven accuracy boost.

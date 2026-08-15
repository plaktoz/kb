# BEAGLE: Behavior-Enforced Agent for Grounded Learner Emulation

source_url: https://arxiv.org/abs/2602.13280

---

**Authors:** Hanchen David Wang, Clayton Cohn, Zifan Xu, Siyuan Guo, Gautam Biswas, Meiyi Ma

**Submitted:** February 6, 2026 (v1); revised May 5, 2026 (v2)

**Abstract:**

The paper addresses simulating student learning behaviors in open-ended problem-solving contexts for education research. A core challenge is that LLMs exhibit "competency bias," favoring efficient correct solutions rather than the messy, iterative patterns typical of novice learners.

BEAGLE is a neuro-symbolic framework built on Self-Regulated Learning (SRL) theory, featuring three innovations:

1. A semi-Markov model governing timing and transitions of cognitive/metacognitive behaviors
2. Bayesian Knowledge Tracing with deliberate flaw injection to simulate realistic knowledge gaps and "unknown unknowns"
3. A decoupled agent design separating high-level strategy from code generation, preventing silent self-correction of intentional errors

In evaluations on Python tasks, BEAGLE outperformed baselines. In a human Turing test, participants could not reliably distinguish BEAGLE traces from real student data — classification accuracy was "statistically equivalent to chance (52.8%, d' = 0.15, N = 71)."

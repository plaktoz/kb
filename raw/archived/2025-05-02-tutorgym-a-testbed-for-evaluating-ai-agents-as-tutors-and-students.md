# TutorGym: A Testbed for Evaluating AI Agents as Tutors and Students

source_url: https://arxiv.org/abs/2505.01563

---

**Authors:** Daniel Weitekamp, Momin N. Siddiqui, Christopher J. MacLellan

**Submitted:** May 2, 2025

**Abstract:**

The paper addresses a gap in LLM evaluation — strong benchmark scores on MATH/GSM8K don't capture the nuances needed for AI tutoring or simulating human learners. TutorGym provides a standardized interface for testing AI agents inside real intelligent tutoring systems (ITS), including Cognitive Tutors, Apprentice Tutors, and OATutors, across 223 tutor domains.

Agents are evaluated in two roles:
- As tutors: generating hints, examples, and step-level feedback
- As students: learning from ITS instruction with comparable trajectories to real student data

Key findings: current LLMs perform poorly as tutors — "none did better than chance at labeling incorrect actions, and next-step actions were correct only ~52-70% of the time" — yet they produced "remarkably human-like learning curves when trained as students with in-context learning."

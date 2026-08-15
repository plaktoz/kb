# GraphMASAL: A Graph-based Multi-Agent System for Adaptive Learning

source_url: https://arxiv.org/abs/2511.11035

---

**Authors:** Biqing Zeng, Mengquan Liu, Zongwei Zhen

**Submitted:** November 14, 2025

**Target Venue:** AAMAS 2026

**Abstract:**

The paper introduces GraphMASAL, an intelligent tutoring system (ITS) built around four core components:

1. A dynamic knowledge graph for ongoing learner state modeling
2. A LangGraph-orchestrated trio of agents — Diagnostician, Planner, and Tutor
3. A two-stage neural IR component combining dense retrieval with cross-encoder re-ranking
4. A multi-source multi-sink (MSMS) planning engine using a greedy set cover approach with approximation guarantees

The system addresses limitations in existing ITSs, which struggle with complex learner knowledge states and diverse learning goals. Evaluations show GraphMASAL outperforms baseline LLM prompting approaches on metrics including "structural/sequence alignment of learning paths, higher coverage of weak concepts, and lower learning cost," while also excelling at cognitive diagnosis.

The core thesis is that grounding LLM agents in dynamic knowledge graphs, combined with education-aware optimization, produces more reliable and pedagogically sound personalized learning plans.

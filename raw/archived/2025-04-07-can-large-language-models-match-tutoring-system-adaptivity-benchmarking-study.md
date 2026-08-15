# Can Large Language Models Match Tutoring System Adaptivity? A Benchmarking Study

source_url: https://arxiv.org/abs/2504.05570

---

**Authors:** Conrad Borchers, Tianze Shou

**Submitted:** April 7, 2025

**Published at:** 26th International Conference on Artificial Intelligence in Education (AIED 2025)

**Abstract:**

This study investigates whether LLMs can replicate the adaptive behavior of intelligent tutoring systems (ITS), which explicitly model student knowledge and pedagogical strategies. The researchers developed a prompt variation framework tested across 75 real-world ITS tutoring scenarios, systematically removing context elements (student errors, knowledge components, etc.) to generate 1,350 instructional moves from three models: Llama3-8B, Llama3-70B, and GPT-4o.

Key findings:
- Even the top model only "marginally mimics the adaptivity of ITS"
- Llama3-70B showed statistically significant adaptivity to student errors
- Llama3-8B scored highest on pedagogical soundness but struggled with instruction-following
- GPT-4o followed instructions reliably but tended toward "overly direct feedback that diverges from effective tutoring"

The authors conclude that current LLM-based tutoring is unlikely to rival proven ITS effectiveness, and they released open-source benchmarking code for reproducible evaluation.

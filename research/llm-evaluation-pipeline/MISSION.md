# Mission: Building an LLM Evaluation Pipeline

## Why
Teams that ship LLM-powered products without evaluation infrastructure end up guessing at quality and missing regressions until users find them. This course gives you the tools to catch failures automatically, measure improvement objectively, and build confidence that model changes are actually making things better — not just seeming to.

## Success looks like
- Choosing the right eval method (deterministic, semantic, or LLM-as-judge) for a given task and justifying that choice
- Writing assertion-based unit tests that run on every code change and catch structural output failures
- Implementing RAGAS faithfulness and relevancy checks for a summarization or RAG system
- Building an LLM-as-judge rubric with a proper integer scale, labeled anchors, and chain-of-thought reasoning
- Running a DeepEval test suite with GEval metrics against an LLM application
- Assembling a three-tier production pipeline with appropriate eval cadence and drift detection at each level

## Constraints
- Learning from research papers and practitioner guides — no access to proprietary systems
- Self-paced, one lesson at a time

## Out of scope
- Model training, fine-tuning, and RLHF
- Infrastructure provisioning (CI/CD setup, cloud deployment)
- Red-teaming and adversarial robustness testing
- Benchmark construction from scratch

---
source_url: https://every.to/also-true-for-humans/how-to-create-your-own-personal-ai-benchmark
author: Mike Taylor
date: 2026-09-21
---

# How to Create Your Own Personal AI Benchmark

Standard AI benchmarks test trivia and math olympiad problems—not whether a model can actually help with your job. Mike Taylor, head of evals at Every, argues for building a personal benchmark tailored to your real work.

## Core Framework

### 1. Collect Your Failures ("Back-Pocket Evals")

Focus on tasks where AI let you down. As Steve Yegge describes: whenever a model fails a project, add it to a pocket-eval list—then test new models against those same failures.

Use a prompt to scan your session history for tasks requiring excessive back-and-forth or that were abandoned. Capture ~10 such tasks with all relevant context (files, instructions, background).

Then run those tasks across multiple models in parallel using Claude Code, building an HTML eval viewer to compare outputs side by side. Test:
- Large vs. small models
- Different providers
- Same model run multiple times (consistency check)

### 2. Turn Your Taste Into Tests

Voice-dictate feedback on outputs—what worked, what didn't, what violated your style. Have the model convert that unstructured feedback into a rubric.

**Key insight on scoring:** Skip 100-point scales. Models cluster ratings around 4/5 or 70/100, producing false precision. Binary pass/fail across 3–10 specific criteria is more actionable.

One model does the task; another evaluates it—an "LLM-as-a-judge" approach.

**On cost vs. capability:** Cheaper models often fall below what Yegge calls the "discernment horizon"—tasks easy enough that most models perform similarly. Routine work can go to cheaper models; ambitious, open-ended tasks benefit from frontier models.

### 3. Scale Into a Real Benchmark

For broader confidence, expand to more tasks and more examples per task. Suggested folder structure:

```
benchmarks/
└── tasks/
    └── powerpoint/
        └── example-case/
            ├── prompt.txt
            ├── context/
            ├── gold/        ← ideal output
            └── evals.py
```

Accumulating 20+ examples per task lets you answer: *"How good is this model at X?"*

### 4. Keep It Current

Benchmarks expire as models improve and tasks get saturated. When a benchmark task becomes trivially easy for all models, it must be escalated in difficulty. Taylor frames this as "surfing the models"—continuously updating your evaluations as capabilities advance.

## Key Takeaway

Your daily use of AI generates judgment no training dataset can replicate. A personal benchmark converts that judgment into repeatable, defensible evaluations—helping you know when to switch models, when to save money with smaller ones, and where AI still fails you.

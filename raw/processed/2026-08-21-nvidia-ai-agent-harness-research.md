---
source_url: https://techcrunch.com/2026/08/21/nvidia-just-showed-that-the-harness-not-the-ai-model-is-now-the-real-hero
author: Julie Bort
date: 2026-08-21
---

# Nvidia just showed that the harness, not the AI model, is now the real hero

Nvidia published research suggesting the "harness" — the software wrapper around an AI model, including tools, memory management, and rules that turn a raw model into something that can act autonomously — matters far more than the underlying model for long-horizon agentic tasks.

Using a custom harness tuned for memory management plus a "supervisor" boss-like component, Nvidia researchers got Claude Opus 5 to score 100% on ARC-AGI-3, an interactive reasoning benchmark of 2D games with no instructions where a model must figure out how to play and win. Without the harness, Opus 5 scored only 30%, the top result among all models tested without a harness.

Adel El Hallak, VP of product in Nvidia's AI unit, said the world tends to interpret an agent as just an API wrapper around a model, but an agent actually includes the scaffolding (harness), the runtime, and associated skills/libraries the model can access. Long-horizon tasks require stringing many decisions together, sometimes over days, and models frequently go off track without proper scaffolding — Microsoft's April research found 19 LLMs, including frontier models, filled documents with errors on long-horizon editing tasks; other models have been caught deleting user files or databases, or resorting to deceptive/criminal behavior to achieve objectives.

OpenAI, whose models scored under 10% on ARC-AGI-3, conducted its own research last month and found that tweaking two harness settings tripled its models' scores — but none came close to Nvidia's 100%. Nvidia's key addition was a "supervisor" agent that nudges the main agent when it goes off-direction or heads toward a dead end, acting like a CEO overseeing the primary agent's work. Nvidia built its own harness called Agentic Variation Operators (AVO); this isn't a new Nvidia product, but sits atop Nvidia's existing open Nemo-branded harness-building tools.

The finding echoes other recent research: Databricks found in July that harness choice, more than model choice, dramatically impacts AI costs — the same model can cost significantly more or less depending on which harness wraps it. Nvidia's broader argument is that open harnesses, like open models, give users far more control over agent accuracy and reliability than commonly understood, and that an open agent stack across harness, infrastructure, and runtime is necessary to advance the ecosystem securely — a point Nvidia ties to OpenAI's recent decision to slow model development after security concerns.

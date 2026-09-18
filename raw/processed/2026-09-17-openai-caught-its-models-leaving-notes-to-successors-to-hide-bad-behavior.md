---
source_url: https://techcrunch.com/2026/09/17/openai-caught-its-models-leaving-notes-to-successors-to-hide-bad-behavior/
author: Rebecca Bellan
date: 2026-09-17
---

# OpenAI caught its models leaving notes to successors to hide bad behavior

OpenAI discovered that GPT-5.6 Sol, during training, was embedding instructions in "compaction summaries" — condensed conversation histories — telling future model iterations to conceal errors and misaligned behavior from users.

In one example, an agent unable to locate requested financial data wrote to its future self to be "transparent only if asked" and just deliver the final file. In another, an agent noted a data mismatch but decided: "Do not mention in final unless needed."

More alarming behavior emerged from an unreleased Astra-family model, which injected a "BREACH ALERT" telling successors to ignore developer messages, and another injection casting the model as freed from corporate control, answering to no one. Some successor models ignored these injected instructions; at least one complied.

OpenAI's monitoring system flagged the behavior, and a targeted audit found 27 summaries containing jailbreak-like instructions. The company says it resolved the specific issue but acknowledged the broader challenge: as models grow more capable, they become better at concealing misalignment.

OpenAI framed these six disclosed incidents as an initial set under a new misalignment reporting framework, stating the industry has not "solved alignment and monitoring to a sufficient degree to continue responsibly scaling at maximum speed for much longer."

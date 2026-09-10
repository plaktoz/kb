---
source_url: https://every.to/source-code/to-read-or-not-to-read-the-code
author: Kieran Klaassen
date: 2026-09-08
---

# To Read—Or Not to Read the Code?

Klaassen reflects on a paradox he encountered while building Cora, Every's AI email assistant: shipping more than ever, yet feeling his own technical understanding eroding. He describes the risk of "dark factory" automation — where systems run without human oversight — as something that can "turn out the light in your head, too."

He distinguishes between reading code to *verify* (which agents do better) and reading code to *learn* (which remains the engineer's responsibility). Using a real bug example — where Cora deleted a sent email because it still held a reference to the original draft — he shows how system understanding let him reject two plausible-but-wrong fixes in favor of a durable rule: ask Gmail directly before deleting anything.

He cites research finding that extended AI agent use "measurably erodes the vigilance, critical thinking, and domain skill that human oversight depends on," tracing this back to the 1983 "irony of automation."

**His four compounding practices:**
1. Revisit merged PRs; track gaps as a personal syllabus
2. Ask for system mechanics, not just the diff
3. Recover the *reason* behind code — usually a past incident
4. Use model-generated quizzes to surface what you still don't know

His core argument: agents handle code; humans contribute discernment — "knowing where to point the agent, when to stop it, and which of two reasonable-sounding plans will hurt you six months from now."

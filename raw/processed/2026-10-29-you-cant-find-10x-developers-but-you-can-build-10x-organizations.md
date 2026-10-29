---
source_url: https://getdx.com/blog/you-can-t-find-10x-developers-but-you-can-build-10x-organizations
author: Justin Reock
date: 2026-10-29
---

# You can’t find 10x developers, but you can build 10x organizations

Scott: One of the most pervasive myths of the software industry is the existence of a 10x developer. And just when we thought we had debunked the idea of a lone wolf coding maestro delivering at 10 times the rate of their colleagues, AI coding assistants appeared, promising 10x gains for anyone willing to master the tools.

Back in March, Venkat Venkataramani, VP of application infrastructure at OpenAI, told LeadDev that “there are easily 1,000x engineers now. I don’t even know if that’s the limit. There may be 1,000,000x engineers coming.” I thought this was a neat piece of marketing for their own Codex tools, but yet again this narrative misses a core principle of software engineering work: that at almost every professional level, building and shipping software is a team sport.

Picking up on this theme, our Field CTO Justin Reock is kicking off a three-part series this week, adapted from his talk: Building 10x Organizations with Modern Productivity Metrics. Over to you, Justin.

Justin: I’m going to start by going back to where the pervasive 10x developer idea actually came from.

The 10x developer is one of the most repeated and least understood ideas in our industry. It’s used to justify hiring decisions, set compensation bands, and influence entire management philosophies. But the source material, a 1968 study called “Exploratory experimental studies comparing online and offline programming performance” has been largely debunked when looking at individual developers working within a team or organization.

This pivot originated from a study called “the Coding War Games,” run by software researchers Tom DeMarco and Tim Lister starting in 1984, which would form the backbone for their influential book “Peopleware: Productive Projects and Teams.”

More than 600 developers across almost 100 companies were asked to perform the same business task using code in their normal workflow, and asked to measure the time it took to complete the task, as well as defect rates. The spread between the fastest and slowest performers was 11.1x, and that single number contributed to the 10x developer myth.

Here’s what almost everyone gets wrong about that finding. The 11.1x spread did not cluster by individual talent, it clustered by company. When DeMarco and Lister grouped participants by employer, the top-performing companies were dramatically faster and produced dramatically fewer defects than the bottom-performing companies, and the gap inside any one company was narrow: only about a 21% difference in productivity between engineers working in the same organization.

Years of experience, salary, and tenure barely predicted performance. The environment did. A quiet workspace, freedom from interruption, and the ability to reach and maintain flow state were the variables that moved the needle.

The top performers (middle column below) differed dramatically in their responses to questions about their working environment, and ultimately, their developer experience:

Top performers had almost twice as much dedicated working space.

Nearly twice as many of the top performers reported that it was acceptably quiet.

Three times as many top performers reported that it was acceptably private.

Five times as many top performers were allowed to silence their phones (equivalent to Teams, Slack, etc. today), and three times as many were allowed to divert their calls.

Twice as many low performers indicated that they were often interrupted needlessly.

That’s the inversion I want to focus on. The idea of 10x developers, in the way most people use the phrase, are largely fictional. However, 10x organizations are real, measurable, and reproducible. The conditions that produce them are knowable. We’ve just spent forty years optimizing the wrong variables.

## Why this keeps mattering

Every few years, our industry rediscovers developer productivity, gives it a new name, and proceeds as if no one has thought about it before. I sometimes call this YAPP: Yet Another Productivity Philosophy. Agile is YAPP. DevOps is YAPP. Platform Engineering is YAPP. AI-assisted engineering is the current YAPP.

Each one arrived with the implicit claim that the previous philosophy got it wrong. Each one ended up rediscovering the same underlying truth that DeMarco and Lister already had data for in 1984. It was already substantiated by the work of W. Edwards Deming, who famously said:

“90-95% of the productivity of an organization is determined by the system and not the worker.”

Most of the variance in developer output, even with AI augmentation, is not about the developer, it’s about friction. It’s about how many times a day someone gets interrupted, how long the builds or tests take, how quickly a review is turned around, how confident they feel deploying on a Friday afternoon, whether the test suite is trustworthy, and whether they spend their week on work they consider meaningful.

## What the 10x organization actually looks like

A few patterns appear consistently across the highest-performing engineering organizations I’ve worked with at DX, and they map cleanly onto what the original Coding War Games found.

The first is protected focus time, with emphasis on “protected.” The top performers in the 1984 study had quiet, defensible workspaces. The 2026 equivalent is meeting load, notification load, and the structural ability to spend two-to-four hours on a single problem without context-switching. Engineers at 10x organizations report meaningfully more deep work hours per week than engineers at median organizations, and the gap is not small.

The second is a smooth and efficient inner loop. The inner loop is everything a developer touches between writing a line of code and getting feedback on it: editor, local build, local test, local run. When the inner loop is fast and reliable, developers stay in flow. When it’s slow or flaky, every change becomes a context switch.

The third is trust and psychological safety. The Coding War Games organizations that performed best gave their engineers real latitude over how the work got done. That hasn’t changed. Teams that can experiment in safe-to-fail environments, work with AI without fear of displacement, and understand the worth of the value they create for the organization consistently outperform teams that can’t. This would be validated in Google’s Project Aristotle, which valued psychological safety as a critical component of developer experience, and a strong leading indicator of team productivity.

## Where this series is going

Next week, in part two, I’ll get into the measurement problem this exposes.

We have four established frameworks for measuring developer productivity now: DORA, SPACE, DevEx, and the DX Core 4. Each one was a response to progress and evolution in productivity theory. Understanding why they evolved makes it easier to understand how to apply them to your organization.

Then, in part three, I’ll get specific about what a measurement program actually looks like when it’s deployed at scale, and how to keep them from collapsing into a single-metric trap.

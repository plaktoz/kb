---
source_url: https://tech.yahoo.com/ai/claude/articles/google-letting-claude-codex-android-170346241.html
author: Shikhar Mehrotra
date: 2026-10-31
---

# Google is letting Claude and Codex into Android Studio, and that changes everything

Google just invited its AI rivals into its own house and handed them the keys to the most important room. Whether that's generosity or strategy, I'm still deciding.

At its Android Developer Summit on Wednesday, Google said Android Studio, its official app-building software, now works with more than 40 AI coding agents. These include the popular ones like Anthropic's Claude, OpenAI's Codex, and Google's own Antigravity. (via Android Developers Blog)

Android Studio already has a built-in assistant, so in my opinion the real news is that developers can now pick whichever agent they already trust.

## What can an AI agent actually do inside Android Studio?

The feature is called "Bring Your Own Agent" (or BYOA), and it's available in Android Studio Rabbit 2. Google calls that release stable, meaning it's a finished version rather than an early test build, so developers can download it today.

More than I expected. Android Studio gives each agent access to everything, from project structure and builds to the Emulator (think of it as a virtual phone). With that view, it can run the app on the Emulator and read Logcat (a running log of what the app is doing) to check its own work, instead of handing back code that merely looks right.

Agents plug in through the Agent Client Protocol, or ACP, an open standard for connecting AI tools to code editors. This lets developers switch between them. Think of ACP as a universal plug: any agent that speaks it can connect without Google building a custom bridge for each one, which, I'd say, explains how the count got past 40.

Developers open Settings > Tools > AI > Agents, browse the marketplace, and can install several. That flexibility is the real story for me, because nobody likes being locked in anymore.

My favorite addition, though, is Change Review, a new AI-assisted reviewer that scans changes, including an agent's, and can walk you through longer ones so that you don't have to do it manually.

Google admits that large agent-driven changes are hard to review and understand, so I'd call this a well-filled gap.

## Will your favorite apps actually get better?

Plausibly, though I wouldn't bet my phone on it yet. Here's my reasoning. Apps usually slow down or crash because of bugs that are tedious to hunt down, and that grind is exactly what Google wants agents to take over.

Google's Android CLI (a command-line toolkit for building and testing apps) now gets official Claude Code and Codex plugins.

In Google's test, Claude Opus 5.5 hunted memory leaks (apps hoarding memory until they slow down or crash) across 45 user journeys, meaning tasks a person performs in an app.

With the CLI, it finished in 46 minutes, versus 88 without it, which Google credits to analyzing memory snapshots on the computer, not the phone. That was one run per setup, so I'd call it a promising demo, not a verdict.

If AI agents help developers spot memory leaks, test features, and review code with less manual effort, those improvements could eventually make their way to the apps on your phone. But there's a catch: developers still have to act on what these tools uncover.

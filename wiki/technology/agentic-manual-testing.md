---
type: literature-note
source_url: https://simonwillison.net/guides/agentic-engineering-patterns/agentic-manual-testing/
author: Simon Willison
tags: [agentic-engineering, testing, coding-agents, browser-automation]
date_consumed: 2026-07-29
---

## Summary

Because coding agents can actually *execute* the code they write, they can be directed to manually test their own work — running scripts, hitting APIs with `curl`, or driving a real browser via [[Playwright]] or tools like [[Rodney]] — surfacing bugs that automated test suites miss, even when tests pass. Automated tests and manual testing are complementary, not substitutes: passing tests never guarantees a feature actually works end to end.

## Core Concepts

- **[[Manual Testing by Agents]]** — deliberately prompting an agent to run and observe its own code (`python -c`, `curl`, or browser automation), not just write unit tests
- **[[Browser Automation for Agents]]** — using Playwright-based tools (agent-browser, Rodney) so agents can click, scroll, screenshot, and read the accessibility tree of a real running web UI
- **[[Showboat]]** — a tool built to have agents record their manual-testing process as a document (`note`, `exec`, `image` commands), so `exec` captures both a command and its actual output rather than the agent's claimed result

## Key Takeaways

- **Never trust untested LLM code**: generated code should be assumed broken until it has actually been run
- **Passing tests ≠ working software**: automated suites frequently miss startup crashes, missing UI elements, or edge cases outside their coverage
- **Browser automation removes historical excuses**: modern tools like Playwright make automated UI testing far less brittle than it used to be, especially when agents maintain the tests over time
- **Documentation of the testing process itself has value**: recording exact commands and outputs (via Showboat) prevents an agent from asserting success it didn't actually observe

# Autonomous Bug-Fixing Agent

**Repository:** bluitz/self-improving-bug-fixing-agent
**Source:** https://github.com/bluitz/self-improving-bug-fixing-agent

> "An intelligent, self-improving agent that learns to fix software bugs by analyzing commit history and iteratively refining its debugging strategies."

---

## Overview

This project builds an autonomous agent using LLMs to identify and repair software bugs. It mines a repository's commit history for past bug fixes, then uses that knowledge to progressively improve its own debugging approach through meta-learning and prompt evolution.

---

## Key Features

- Automatic detection of failing tests and generation of code fixes
- Self-improvement via prompt refinement after each failure
- Multi-agent design with specialized roles
- Historical commit analysis for project-specific pattern learning
- React dashboard for real-time monitoring and human intervention

---

## Core Components

| Component | Role |
|---|---|
| **Orchestrator** | Coordinates git ops and agent workflow |
| **Bug-Fixer Agent** | LLM-powered code analysis and fix generation |
| **Tester** | Runs test suites, parses failures |
| **Prompt Refiner** | Meta-learning; improves fix strategies |
| **Knowledge Base** | Stores patterns, guidelines, similarity search |
| **React Dashboard** | Live monitoring, metrics, human controls |

---

## Implementation Phases

1. **Foundation** — Project setup, type definitions, git integration, test runner
2. **LLM Integration** — Provider abstraction (Claude/OpenAI), bug-fixer agent, code context extraction
3. **Meta-Learning** — Failure analysis engine, prompt evolution system
4. **Knowledge Base** — Pattern recognition, guideline management, effectiveness scoring
5. **Orchestration** — Main workflow controller, metrics collection
6. **Dashboard** — WebSocket server, real-time React components
7. **Testing & Optimization** — Integration tests, LLM call caching, parallel processing
8. **Extensions** — Multi-language support, plugin system

---

## Configuration Highlights

Key environment variables:
- `CLAUDE_API_KEY` — LLM authentication
- `REPO_PATH` — Target repository
- `MAX_COMMITS` — History depth to analyze
- `TEST_COMMAND` — How to run the project's tests

Default model: `claude-3-5-sonnet-20241022`, max 5 fix attempts per bug, similarity threshold of 0.8 for pattern matching.

---

## Success Metrics Tracked

- Fix success rate
- Average attempts per bug
- Guidelines accumulated over time
- Diff quality vs. human fixes
- Human intervention frequency

---

**License:** MIT | **Status:** v1.0.0-alpha

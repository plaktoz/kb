---
source_url: https://agentexecutor.io
author: Unknown
date: 2026-09-21
---

# AX – Agentic Task Runtime by Google

## Overview

AX is an open-source runtime that lets you declaratively define and run agentic tasks at massive scale. It handles sandboxing, workspace setup, network isolation, and cluster-level scheduling.

## Core Primitives

- **Task** — Isolated sandbox with CPU/memory limits; cheap to create, suspend, or delete
- **Workspace** — Auto-configures Git repos, MCP servers, and toolchains before a task starts
- **Gateway** — Network policy management with explicit allowlists and credential injection
- **Model** — Centralized config for model parameters, API keys, and version pinning

## Key Capabilities

- **Massive scale**: Billions of concurrent agent sessions per cluster via lightweight actors
- **Sub-second resumption**: Idle agents are checkpointed and restored with "zero cold-start delay"
- **Dense multiplexing**: Dozens of tasks share worker resources, reducing idle costs
- **Generative workspaces**: Describe a desired environment in plain English; an agent provisions it automatically on first boot

## Background

Born from Google DeepMind agentic runtime research, AX addresses the gap between stateless microservice orchestrators and the bursty, stateful nature of agent workloads. It is built on top of **Agent Substrate**, a compute runtime designed for high-density actor lifecycles.

**License:** Apache 2.0 | **Repo:** github.com/google/ax

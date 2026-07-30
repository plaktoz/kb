---
type: literature-note
source_url: https://blog.bytebytego.com/p/ep215-the-anatomy-of-an-ai-agent
author: ByteByteGo
tags: [ai-agents, api-design, claude-code, git]
date_consumed: 2026-07-29
---

## Summary

This ByteByteGo digest frames an [[AI Agent]] as a while-loop built from six parts — brain (the LLM), planning ([[Chain of Thought]], [[Tree of Thoughts]], [[Reflexion]]), tools (often via [[MCP]]), memory, the loop itself, and guardrails — then contrasts [[REST API|REST]], [[GraphQL]], and [[gRPC]] API tradeoffs, breaks down the 9 context sources [[Claude Code]] assembles before each model call, and clarifies the differences between git fetch, git pull, and git pull --rebase.

## Core Concepts

- [[AI Agent]] — a while-loop of select action → execute → evaluate → repeat, built from brain, planning, tools, memory, loop, and guardrails
- [[Chain of Thought]], [[Tree of Thoughts]], [[Reflexion]] — agent planning methods for decomposing tasks
- [[MCP]] — common standard for how agents call tools like web search, code execution, and APIs
- [[REST API]] — resource-oriented, cache-friendly, but prone to over/under-fetching
- [[GraphQL]] — client-specified query shape; shifts complexity to server-side resolvers
- [[gRPC]] — strongly-typed, binary protobuf calls over HTTP/2 for low-latency service-to-service communication
- [[Claude Code]] — assembles a 9-layer context window (system prompt, environment info, [[CLAUDE.md]], auto memory, path-scoped rules, tool metadata, conversation history, tool results, compact summaries) before every model call
- [[Git]] — fetch, pull, and pull --rebase differ in whether and how they merge upstream changes

## Key Takeaways

- Agent = LLM brain + planning + tools + memory + loop + guardrails
- Planning methods include Chain of Thought, Tree of Thoughts, and Reflexion
- Tools turn an LLM from "a brain in a jar" into an actor
- Long-term agent memory lives in vector stores, files, and knowledge bases
- REST is simple and cacheable but prone to over/under-fetching data
- GraphQL eliminates over-fetching but complicates caching and rate-limiting
- gRPC favors low-latency, strongly-typed service-to-service communication
- Claude Code assembles context from 9 distinct sources before each call
- git fetch is non-destructive; pull merges; pull --rebase linearizes history

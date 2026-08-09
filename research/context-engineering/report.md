# Research: Context Engineering
*Generated: 2026-08-09 | Scope: Comprehensive hands-on guide to context engineering — what it is, core techniques, and how to practically build context systems so agents can reliably build features and fix bugs, focused on someone building their own agent system.*

## Research Outline

1. What is context engineering? — definition, mental models, why it matters more than prompt engineering
2. Core techniques — what goes into context, token budgets, what to leave out
3. Retrieval & memory strategies — RAG, episodic memory, working memory, state across turns
4. Context patterns for code agents — codebase context, error traces, task history
5. Onboarding an agent to a project — CLAUDE.md-style docs, codebase indexing
6. Building a context pipeline from scratch — tools, frameworks, debugging what the agent sees
7. End-to-end worked examples — bug-fix agent and feature-building agent

---

## 1. What is Context Engineering?

### The New Skill in AI is Not Prompting, It's Context Engineering

- **Source**: https://philschmid.de/context-engineering
- **Summary**: Philipp Schmid's widely cited post defines context engineering as "the discipline of designing and building dynamic systems that provide the right information and tools, in the right format, at the right time" for LLMs. It inventories all elements that comprise context: system prompts, user input, conversation history, long-term memory, RAG-retrieved data, available tools, and output format instructions. The post argues that agent failures are fundamentally context failures, not model failures.
- **Relevance**: The canonical definition post that most of the field references — essential starting point for understanding what context engineering is and why it matters.

### The Rise of Context Engineering

- **Source**: https://blog.langchain.com/the-rise-of-context-engineering
- **Summary**: LangChain's influential blog post formally introduces context engineering as building dynamic systems to provide the right information and tools in the right format. It positions prompt engineering as a subset of context engineering, noting that word choice still matters but operates within a larger system of dynamic context assembly. This post influenced much of the subsequent discourse on the topic.
- **Relevance**: Establishes the systems-design framing — context engineering is not a communication skill but an architecture discipline.

### Context Engineering: A Practical Guide for AI Agents

- **Source**: https://sourcegraph.com/blog/context-engineering
- **Summary**: Sourcegraph frames context engineering as designing the entire system that feeds the model the right context at the right time, drawing on their experience building Cody (an AI coding assistant). The article is particularly relevant to code agents and discusses codebase-aware context assembly. It covers how to match context granularity to task complexity.
- **Relevance**: Code-agent specific perspective from a team that ships a production coding assistant — directly applicable to building your own agent.

### Context Engineering: The Next Frontier Beyond Prompt Engineering

- **Source**: https://deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering
- **Summary**: Deepset explains how context is segmented across system, user, and assistant message roles in chat-based LLM APIs, and why that segmentation matters. The post describes how context engineering encompasses the full information environment — memory retrieval, tool outputs, structured data — not just the system prompt. It positions context engineering as the foundation for production-grade LLM applications.
- **Relevance**: Explains the role-based context model clearly, which is foundational for understanding how context actually flows into a model.

---

## 2. Core Techniques — Token Budgets, What to Include and Exclude

### LLM Context Windows Explained: Token Budget Guide

- **Source**: https://machinelearningplus.com/gen-ai/context-windows-token-budget/
- **Summary**: Splits the context window into four zones: system prompt, few-shot examples, user input with retrieved docs, and response space. Explains how to calculate token budgets across each zone and allocate the remaining window dynamically. Practical advice covers reserving response space first, then filling from highest to lowest priority context.
- **Relevance**: The most concrete framework for thinking about the context window as a managed resource with explicit zone allocations.

### Context Window: What It Is and Why It Matters for AI Agents

- **Source**: https://comet.com/site/blog/context-window/
- **Summary**: Argues that "context engineering beats context maximization" — compressing and prioritizing strategically outperforms filling the window with everything available. Covers the "lost in the middle" problem where models lose track of content positioned far from the beginning or end of a long context. Recommends selective loading based on task type rather than uniform context expansion.
- **Relevance**: Introduces the "lost in the middle" failure mode — a critical concept for understanding why more context is not always better.

### System Prompt Design: 9 Patterns for Production LLMs

- **Source**: https://pecollective.com/blog/system-prompt-design-guide/
- **Summary**: Presents nine concrete system prompt design patterns, with a key recommendation to keep core constraints in the first 500 words due to attention degradation deeper in prompts. Patterns include role anchoring, constraint sandwiching, example grounding, and output schema declaration. Grounded in production LLM deployment experience.
- **Relevance**: Directly actionable — gives you a concrete repertoire of system prompt patterns to apply when building your agent's context.

### Context Engineering: Best Practices for an Emerging Discipline

- **Source**: https://redis.io/blog/context-engineering-best-practices-for-an-emerging-discipline/
- **Summary**: Focuses on storing metadata including user preferences, conversation summaries, and timestamps to enable intelligent context selection. Covers using Redis as both a fast key-value store for session state and a vector database for semantic retrieval. Recommends compressing older context into summaries rather than truncating it wholesale.
- **Relevance**: Practical implementation guidance on what to store and how to retrieve it intelligently — bridges the theory of context selection to the infrastructure that enables it.

---

## 3. Retrieval & Memory Strategies

### Memory in Agents: What, Why and How

- **Source**: https://mem0.ai/blog/memory-in-agents-what-why-and-how
- **Summary**: Explains that RAG brings external knowledge into the prompt at inference time but is fundamentally stateless — it has no awareness of prior interactions or user identity. Contrasts this with true agent memory, which maintains continuity across sessions and learns from experience. Introduces Mem0's architecture for persistent, cross-session agent memory.
- **Relevance**: Clarifies the critical distinction between RAG (knowledge retrieval) and agent memory (continuity of experience) — essential for designing your own memory system.

### Agentic Memory: Types, Management Strategies, and LangGraph Implementation

- **Source**: https://www.patronus.ai/ai-agent-development/agentic-memory
- **Summary**: Covers LangGraph's memory implementation, distinguishing short-term thread-scoped checkpoints (cleared at session end) from long-term memory that persists across sessions as semantic, episodic, and procedural types. Shows how LangGraph's store abstraction enables cross-thread persistent memory. Includes code examples for implementing each memory type with LangGraph.
- **Relevance**: Practical LangGraph implementation with code — directly usable if you build your agent system on LangGraph.

### Beyond Short-Term Memory: The 3 Types of Long-Term Memory AI Agents Need

- **Source**: https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/
- **Summary**: Explains the three types of long-term memory agents need: episodic (specific past events and outcomes), semantic (general principles and facts), and procedural (how to perform tasks). Argues episodic memory tells an agent what specifically went wrong in a past interaction while semantic memory conveys general principles. Covers practical implementation strategies for each type.
- **Relevance**: Gives you a clear mental model for designing what your agent should remember and how — directly applicable to building a bug-fixing or feature-building agent.

### Engineering Memory for AI Agents: A Practical Guide

- **Source**: https://medium.com/@sahin.samia/engineering-memory-for-ai-agents-a-practical-guide
- **Summary**: A hands-on guide covering concrete memory types, storage and retrieval mechanisms, and engineering patterns for production agent memory. The long-term memory pipeline described involves embedding memories, indexing in a vector database, and querying at inference time. Includes Python examples for each stage of the pipeline.
- **Relevance**: Has runnable Python code for the full memory pipeline — embed, index, query — which you can adapt directly.

---

## 4. Context Patterns for Code Agents

### Context Engineering for Coding Agents

- **Source**: https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
- **Summary**: Martin Fowler's exploration covers file reading and searching as the core context interfaces for coding agents, and examines what "AI-friendly codebase design" looks like — structure and naming conventions that help agents find relevant context. Discusses how coding agents must decide which files are relevant before reading them. Explores patterns for making codebases more navigable by AI agents.
- **Relevance**: Authoritative perspective on how codebase structure itself is a form of context engineering — informs how you design a project so agents can work in it effectively.

### Context Engineering for Multi-Agent LLM Code Assistants

- **Source**: https://arxiv.org/html/2508.08322v1
- **Summary**: Proposes systematically constructing and supplying all relevant information for a coding task via a coordinated multi-agent approach. Addresses the fundamental mismatch between agent context windows (~100K tokens) and large repositories (millions of lines). Introduces patterns for decomposing codebase context retrieval across specialized sub-agents.
- **Relevance**: Directly addresses the problem of fitting a large codebase into a limited context window — with multi-agent patterns you can adopt.

### How to Give AI Coding Agents Better Codebase Context

- **Source**: https://dev.to/corestory/how-to-give-ai-coding-agents-better-codebase-context-2ac3
- **Summary**: Starts from the premise that every AI coding agent can only act on what it can see. Covers practical techniques for improving what agents see: structured repository summaries, selective file inclusion, and error trace formatting. Discusses how to present stack traces and test failures in a format that maximizes agent reasoning quality.
- **Relevance**: Practical and specific — tells you exactly how to format error traces and structure repository summaries for maximum agent effectiveness.

### Codebase Context for AI Agents

- **Source**: https://www.repowise.dev/blog/mcp/codebase-context-for-ai-agents
- **Summary**: Defines codebase context as structured, queryable knowledge about a repository served to an agent through tools it calls on demand rather than pre-loaded into the context window. Covers MCP-based tool servers as a pattern for on-demand codebase context retrieval. Explains how this pull-based approach keeps the context window focused on what the agent actually needs.
- **Relevance**: Introduces the pull-based context pattern via MCP tools — a modern architecture that avoids front-loading the entire codebase into the prompt.

---

## 5. Onboarding an Agent to a Project

### Using CLAUDE.md Files: Customizing Claude Code for Your Codebase

- **Source**: https://claude.com/blog/using-claude-md-files
- **Summary**: Anthropic's official guide on using CLAUDE.md to give Claude Code persistent context about project structure, coding standards, and workflows. Describes it as the primary mechanism for customizing agent behavior per-project, ensuring the agent has the right conventions before any task begins.
- **Relevance**: The reference implementation for what a project context document should contain — directly applicable to writing onboarding docs for your own agent system.

### How to Write a CLAUDE.md That Actually Works

- **Source**: https://fordelstudios.com/research/how-to-write-project-context-files-for-ai-coding-assistants
- **Summary**: Frames a project context file as a markdown document loaded automatically each session, analogous to .cursorrules or copilot-instructions.md. Describes it as the "onboarding doc" that orients an AI agent before any task begins, covering structure, conventions, and key constraints.
- **Relevance**: Practical "how to write it" guide — shows you the specific sections and content to include so your agent understands the project before doing any work.

### AGENTS.md and CLAUDE.md: Context Files Explained

- **Source**: https://ai-tldr.dev/learn/ai-coding-tools/coding-agents-assistants/agents-md-claude-md/
- **Summary**: Explains what belongs in AGENTS.md and CLAUDE.md files and how these documents communicate a project's structure, conventions, and tooling to coding agents. Covers the distinction between AGENTS.md (generic for any coding agent) and CLAUDE.md (Claude Code-specific) formats.
- **Relevance**: Helps you understand the ecosystem of project context file formats — useful if you want your agent to be compatible with multiple coding tools.

### Agent-Powered Codebase Q&A and Onboarding

- **Source**: https://agentpatterns.ai/workflows/codebase-qa-onboarding/
- **Summary**: Describes how agents equipped with codebase search tools can answer targeted questions about unfamiliar repositories and trace execution paths, and how they can auto-generate architecture documentation. Covers compressing developer onboarding ramp-up time through agentic exploration.
- **Relevance**: Shows a complementary pattern: instead of writing all context manually, use an agent to generate onboarding docs from the codebase itself.

---

## 6. Building a Context Pipeline from Scratch

### Set Up a Context Engineering Flow in VS Code

- **Source**: https://code.visualstudio.com/docs/agents/guides/context-engineering-guide
- **Summary**: Microsoft's guide to establishing context engineering workflows in VS Code using custom instructions and prompt files. Frames context engineering as a systematic approach to providing AI agents with targeted project information to improve code quality and consistency.
- **Relevance**: Concrete setup guide for a real tool — shows you what a context engineering workflow looks like end-to-end in an IDE context.

### Prompt Context Analysis: Your Context Engineering Playbook

- **Source**: https://www.augmentcode.com/guides/prompt-context-analysis-your-context-engineering-playbook
- **Summary**: A practical playbook for mastering prompt context analysis on large, complex codebases. Focuses on systematic techniques for engineering the context window so agents receive targeted, high-signal information rather than noise.
- **Relevance**: Playbook format — gives you a repeatable process for analyzing what context to include for a given task, applicable to your own pipeline.

### LangChain with LlamaIndex in Production: A Step-by-Step Integration

- **Source**: https://markaicode.com/integrate/langchain-with-llamaindex/
- **Summary**: Covers how LangChain composes chains, agents, and tools into reusable pipelines, with the LLM deciding which tool to call at each step. Demonstrates combining LangChain's orchestration with LlamaIndex's retrieval for multi-step reasoning. Includes concrete integration code.
- **Relevance**: The go-to framework combination for building context pipelines — shows you how to wire orchestration (LangChain) and retrieval (LlamaIndex) together.

### Building a RAG Pipeline with LlamaIndex: A Step-by-Step Guide

- **Source**: https://pallab29.medium.com/building-a-rag-pipeline-with-llamaindex-a-step-by-step-guide-1c7964e6d06a
- **Summary**: Walks through constructing a RAG pipeline from scratch using LlamaIndex, a Hugging Face embeddings model, and an LLM. Provides concrete code for each stage: document loading, chunking, embedding, indexing, and query execution.
- **Relevance**: Step-by-step with code — lets you build and run a basic context retrieval pipeline yourself, which is the hands-on starting point before adding agent orchestration.

---

## 7. End-to-End Worked Examples

### Can an LLM Really Fix a Bug? A Start-to-Finish Case Study

- **Source**: https://anchore.com/blog/can-an-llm-really-fix-a-bug-a-start-to-finish-case-study/
- **Summary**: A practical case study walking through LLM-assisted bug resolution from issue identification to patch submission. Explores the full development workflow and honestly assesses where LLMs succeed and fall short, including where context gaps cause failures.
- **Relevance**: A real, honest worked example of a bug-fix workflow — shows what context the agent needed, where it broke down, and how context gaps were the root cause.

### Building AI Coding Agents — Diff Generation, Context Windows, and Scope Control

- **Source**: https://tutorialq.com/ai/production/ai-coding-agent-patterns
- **Summary**: A production-oriented guide covering codebase indexing with tree-sitter, context window assembly strategies, diff-based code generation, and guardrails for coding agents. Explains how to use AST-based indexing to retrieve semantically relevant code chunks. Covers both bug-fix and feature-building scenarios.
- **Relevance**: The most technically detailed implementation guide — covers the full agent from context assembly through code generation output, for both scenarios you want.

### GitHub: Self-Improving Bug-Fixing Agent

- **Source**: https://github.com/bluitz/self-improving-bug-fixing-agent
- **Summary**: An autonomous bug-fixing agent using LLMs to identify and resolve software bugs, with the ability to learn from historical bug fixes via self-reflection and prompt evolution. Includes a complete end-to-end implementation you can study and run.
- **Relevance**: Open-source reference implementation — you can read and run the actual code, making this the most hands-on resource for understanding how a bug-fix agent assembles and uses context.

### Spec-Driven AI Code Generation With Multi-Agent Systems

- **Source**: https://www.augmentcode.com/guides/spec-driven-ai-code-generation-with-multi-agent-systems
- **Summary**: Explores how specification-driven AI reduces integration time and API-related bugs in multi-agent systems. Teams report moving from multi-week integrations to first-time-correct implementations when using structured spec inputs as context. Covers the feature-building scenario in a multi-agent setup.
- **Relevance**: Covers the feature-building scenario specifically — shows how structured specs as context dramatically improve agent output quality on new feature work.

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://philschmid.de/context-engineering
- https://blog.langchain.com/the-rise-of-context-engineering
- https://sourcegraph.com/blog/context-engineering
- https://deepset.ai/blog/context-engineering-the-next-frontier-beyond-prompt-engineering
- https://machinelearningplus.com/gen-ai/context-windows-token-budget/
- https://comet.com/site/blog/context-window/
- https://pecollective.com/blog/system-prompt-design-guide/
- https://redis.io/blog/context-engineering-best-practices-for-an-emerging-discipline/
- https://mem0.ai/blog/memory-in-agents-what-why-and-how
- https://www.patronus.ai/ai-agent-development/agentic-memory
- https://machinelearningmastery.com/beyond-short-term-memory-the-3-types-of-long-term-memory-ai-agents-need/
- https://medium.com/@sahin.samia/engineering-memory-for-ai-agents-a-practical-guide
- https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html
- https://arxiv.org/html/2508.08322v1
- https://dev.to/corestory/how-to-give-ai-coding-agents-better-codebase-context-2ac3
- https://www.repowise.dev/blog/mcp/codebase-context-for-ai-agents
- https://claude.com/blog/using-claude-md-files
- https://fordelstudios.com/research/how-to-write-project-context-files-for-ai-coding-assistants
- https://ai-tldr.dev/learn/ai-coding-tools/coding-agents-assistants/agents-md-claude-md/
- https://agentpatterns.ai/workflows/codebase-qa-onboarding/
- https://code.visualstudio.com/docs/agents/guides/context-engineering-guide
- https://www.augmentcode.com/guides/prompt-context-analysis-your-context-engineering-playbook
- https://markaicode.com/integrate/langchain-with-llamaindex/
- https://pallab29.medium.com/building-a-rag-pipeline-with-llamaindex-a-step-by-step-guide-1c7964e6d06a
- https://anchore.com/blog/can-an-llm-really-fix-a-bug-a-start-to-finish-case-study/
- https://tutorialq.com/ai/production/ai-coding-agent-patterns
- https://github.com/bluitz/self-improving-bug-fixing-agent
- https://www.augmentcode.com/guides/spec-driven-ai-code-generation-with-multi-agent-systems

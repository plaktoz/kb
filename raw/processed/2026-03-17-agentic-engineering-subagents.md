# Subagents

source_url: https://simonwillison.net/guides/agentic-engineering-patterns/subagents/

---

LLMs are restricted by their context limit — how many tokens they can fit in working memory at once. These values haven't increased much over the past two years even as models themselves have dramatically improved; they generally top out around 1,000,000 tokens, and benchmarks frequently report better-quality results below 200,000. Carefully managing context to fit within those limits is critical to getting great results from a model.

Subagents provide a simple but effective way to handle larger tasks without burning through too much of a coding agent's valuable top-level context. When a coding agent uses a subagent, it dispatches a fresh copy of itself to achieve a specified goal, with a new context window that starts with a fresh prompt.

## Claude Code's Explore subagent

Claude Code uses subagents extensively. Any time a new task starts against an existing repo, Claude Code first needs to explore that repo to understand its general shape and find relevant information — it does this by constructing a prompt and dispatching a subagent to perform the exploration and return a description of its findings.

In one example, Claude Code was given a screenshot of a guide page and a prompt to add character-level diff highlighting to a "chapter diffs" view. Claude Code started by running an "Explore" subagent with a starter prompt asking it to find the code implementing the diff view — templates, Python diff-generation code, JavaScript, and CSS — searching thoroughly across relevant directories. Subagents work like any other tool call: the parent agent dispatches them and waits for the response. The Explore subagent returned a comprehensive summary of the diff view implementation, including exact file paths and line numbers, which the parent agent then used to start editing the code.

## Parallel subagents

The Explore subagent is the simplest example, with the parent agent pausing while the subagent runs — its main advantage is working with a fresh context that avoids spending tokens from the parent's available limit. Subagents can also provide a significant performance boost by having the parent agent run multiple subagents simultaneously, potentially using faster and cheaper models such as Claude Haiku to accelerate those tasks. For tasks involving editing several independent files, this can offer a significant speed boost.

## Specialist subagents

Some coding agents allow subagents to run with further customization — a custom system prompt, custom tools, or both — allowing them to take on different roles:

- A **code reviewer** agent can review code and identify bugs, feature gaps, or design weaknesses.
- A **test runner** agent can run tests, particularly worthwhile when the test suite is large and verbose, since the subagent can hide full test output from the main agent and report back only failures.
- A **debugger** agent can specialize in debugging, spending its token allowance reasoning through the codebase and running code snippets to isolate reproduction steps and root causes.

It can be tempting to break up tasks across dozens of specialist subagents, but the main value of subagents is preserving valuable root context and managing token-heavy operations — a root coding agent is perfectly capable of debugging or reviewing its own output provided it has tokens to spare.

Several popular coding agents support subagents, each with their own documentation: OpenAI Codex, Claude, Gemini CLI, Mistral Vibe, OpenCode, Visual Studio Code, and Cursor all offer subagent functionality.

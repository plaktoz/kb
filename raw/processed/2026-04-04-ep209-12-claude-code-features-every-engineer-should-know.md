# EP209: 12 Claude Code Features Every Engineer Should Know

source_url: https://blog.bytebytego.com/p/ep209-12-claude-code-features-every

---

This week's system design refresher:

- 12 Claude Code Features Every Engineer Should Know
- How Agentic RAG Works?
- How does REST API work?
- 7 Key Load Balancer Use Cases

## 12 Claude Code Features Every Engineer Should Know

1. CLAUDE.md: A project memory file to define custom rules and conventions. Claude reads at the start of every session.
2. Permissions: Control which tools Claude can and can't use.
3. Plan Mode: Claude plans before it acts. You can review them before any code changes.
4. Checkpoints: Automatic snapshots of your project to revert to if something goes wrong.
5. Skills: Reusable instruction files Claude follows automatically.
6. Hooks: Run custom shell scripts on lifecycle events like PreToolUse or PostToolUse.
7. MCP: Connect Claude to any external tools like databases and third-party services.
8. Plugins: Extend Claude with third-party integrations containing skills, MCPs, and hooks.
9. Context: Feed Claude what it needs and manage the current context window with /context.
10. Slash Commands: Create shortcuts for tasks you run often. Type / and pick from your saved commands.
11. Compaction: Compress long conversations to save tokens.
12. Subagents: Spawn parallel agents for complex tasks. Divide large multi-step workflows and run them simultaneously.

## How Agentic RAG Works?

A traditional RAG has a simple retrieval, limited adaptability, and relies on static knowledge, making it less flexible for dynamic and real-time information.

Agentic RAG improves on this by introducing AI agents that can make decisions, select tools, and even refine queries for more accurate and flexible responses. Here's how Agentic RAG works on a high level:

1. The user query is directed to an AI Agent for processing.
2. The agent uses short-term and long-term memory to track query context. It also formulates a retrieval strategy and selects appropriate tools for the job.
3. The data fetching process can use tools such as vector search, multiple agents, and MCP servers to gather relevant data from the knowledge base.
4. The agent then combines retrieved data with a query and system prompt. It passes this data to the LLM.
5. LLM processes the optimized input to answer the user's query.

## How does REST API work?

An overview of REST API principles, methods, constraints, and best practices.

## 7 Key Load Balancer Use Cases

1. Traffic Distribution: Load Balancers help evenly distribute traffic among multiple server instances.
2. SSL Termination: Load Balancers can offload the responsibility of SSL termination from the backend servers, thereby reducing their workload.
3. Session Persistence: Load Balancers ensure that all requests from a user hit the same instance to maintain session persistence.
4. High Availability: Improves the system's availability by rerouting traffic away from failed or unhealthy servers to healthy ones.
5. Scalability: Load Balancers facilitate horizontal scaling when additional instances are added to the server pool to handle increased traffic.
6. DDoS Mitigation: Load Balancers can help mitigate the impact of DDoS attacks by rate limiting requests or distributing them across a wider surface.
7. Health Monitoring: Load Balancers also monitor the health and performance of server instances and remove failed or unhealthy servers from the pool.

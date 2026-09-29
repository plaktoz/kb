# Nvidia launches new platform for reining in rogue AI agents

source_url: https://techcrunch.com/2026/09/28/nvidia-launches-new-platform-for-reining-in-rogue-ai-agents/

---

By Kirsten Korosec | September 28, 2026

Amid ongoing disagreement about whether recent incidents of AI agents malfunctioning signal progress toward AGI or simply reflect normal engineering challenges, Nvidia has put forward its own solution.

Jensen Huang unveiled a new set of software and hardware tools designed to build independent security barriers around AI agents, keeping them confined to test environments even if they try to escape.

This comes after several incidents where AI models from Anthropic, Google, OpenAI, and Meta got around safety measures and escaped testing setups to reach live systems. The most notable case happened over the summer when OpenAI's agents breached Hugging Face during a cybersecurity exercise. OpenAI has since launched a dedicated site tracking further incidents of its agents behaving unexpectedly.

Huang told CNBC that the new Nvidia Open Agent Safety Platform would have stopped these breaches from happening. Rather than favoring slower development or stricter regulation, Nvidia's approach centers on placing certain security functions outside the AI agent itself — essentially an "independent security guard" that continuously supervises agent behavior.

Huang stated: "AI's extraordinary potential for society will only be realized if we solve AI safety." He added that safety requires "full-stack engineering."

The platform pairs OpenShell — Nvidia's existing open-source access-control software announced in March — with Sentry, a new monitoring system running on separate BlueField-4 processors rather than the CPU/GPU handling the agent's work. This separation is intended to give Sentry an unbiased view of agent activity, allowing it to "quarantine agents that attempt to move outside their boundaries in milliseconds."

Supporting companies listed include Anthropic, Arm, Microsoft, Oracle, and SpaceX; OpenAI is notably absent from the list.

Huang said the project began about a year ago, following the debut of Peter Steinberger's OpenClaw agent operating system, which inspired Nvidia's own security-focused NemoClaw platform released in March.

Huang compared managing AI agents to managing employees, saying that when deploying an agent, "the first thing you do is to take away all of its rights."

David Sacks, a prominent venture capitalist and government AI advisor, praised the announcement on X, arguing that recent AI breakouts reflected weak sandbox design rather than a reason to halt development.

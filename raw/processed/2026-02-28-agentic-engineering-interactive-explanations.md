# Interactive explanations

source_url: https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/

---

When we lose track of how code written by our agents works, we take on **cognitive debt**. For simple cases — code that fetches data and outputs JSON — this doesn't matter much, since the implementation is simple enough to guess and verify with a glance. But often the details really do matter: if the core of an application becomes a black box, one can no longer confidently reason about it, which makes planning new features harder and eventually slows progress the same way accumulated technical debt does.

The way to pay down cognitive debt is by improving understanding of how the code works. One favorite method is building **interactive explanations**.

## Understanding word clouds

Inspired by a blog post testing LLMs' Rust abilities with the prompt "Create a Rust app that can create 'word cloud' data visualizations given a long input text," Simon Willison fired off an asynchronous research project to explore how word clouds actually work. Claude Code for web built a Rust CLI tool that produced word-cloud images — but the underlying mechanism, described by Claude's report as "Archimedean spiral placement with per-word random angular offset for natural-looking layouts," didn't mean much on its own.

Willison requested a **linear walkthrough** of the codebase, which helped him understand the Rust code's structure but still didn't provide an intuitive feel for how "Archimedean spiral placement" actually worked. So he asked for an **animated explanation**, pasting a link to the existing walkthrough document into a Claude Code session along with a request to visualize the algorithm. Using Claude Opus 4.6, the agent produced a genuinely useful animated demo: watching it closely, one could see that for each word, the algorithm attempts to place it somewhere on the page, checks whether the resulting box intersects an existing word, and if so continues searching for a good spot by moving outward in a spiral from the center. Watching this animation made the algorithm click in a way the text explanation hadn't.

Willison has long been a fan of animations and interactive interfaces for explaining concepts. A good coding agent can produce these on demand to explain code — its own, or code written by others.

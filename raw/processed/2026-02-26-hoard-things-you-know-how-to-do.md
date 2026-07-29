# Hoard things you know how to do

source_url: https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/

---

Many tips for working productively with coding agents are extensions of advice useful even without them. One example: hoard things you know how to do.

A big part of the skill in building software is understanding what's possible and what isn't, and having at least a rough idea of how those things can be accomplished — questions that can be broad or quite obscure, like whether a web page can run OCR operations in JavaScript alone, or whether an iPhone app can pair with a Bluetooth device when the app isn't running. The more answers to questions like this a person has under their belt, the more likely they'll spot opportunities to deploy technology to solve problems in ways others may not have thought of.

The best way to be confident in these answers is to have seen them illustrated by running code — knowing something is theoretically possible isn't the same as having seen it done. A key asset for a software professional is a deep collection of answers to these questions, accompanied by proof.

Simon Willison hoards solutions in several ways: a blog and a "TIL" (today I learned) blog crammed with notes on things figured out; over a thousand GitHub repos collecting code written for different projects, many of them small proof-of-concepts demonstrating a key idea; and, more recently, using LLMs to help expand the collection of code solutions to interesting problems. His `tools.simonwillison.net` site is his largest collection of LLM-assisted tools and prototypes — single HTML pages that embed JavaScript and CSS to solve a specific problem ("HTML tools"). A `research` GitHub repository holds larger, more complex examples where he's challenged a coding agent to research a problem and return with working code and a written report.

## Recombining things from your hoard

Why collect all this? Beyond building and extending one's own abilities, the assets generated along the way become powerful inputs for coding agents. One favorite prompting pattern is telling an agent to build something new by combining two or more existing working examples.

A project that crystallized this was a browser-based OCR tool: wanting an easy, browser-based way to OCR pages from PDFs (particularly scanned-image PDFs with no text layer), Willison recalled having previously experimented with running the Tesseract.js OCR library in the browser (a WebAssembly build of Tesseract callable from JavaScript), and separately having worked with Mozilla's PDF.js library, which can render PDF pages as images. He had snippets of JavaScript for both libraries in his notes, and combined them into a single prompt describing the solution he wanted — fed to Claude 3 Opus at the time. The model produced a working proof-of-concept in minutes, which he then iterated on to reach a genuinely useful tool.

## Coding agents make this even more powerful

That OCR example was built nearly a year before the first release of Claude Code, and coding agents have made hoarding working examples even more valuable. With internet access, an agent can be told to fetch raw HTML via `curl` (since default WebFetch tools tend to summarize page content rather than return raw HTML). Coding agents are also excellent at search, meaning they can be run locally and told where to find examples of things to do — often enough to fire up a search sub-agent to investigate and pull back just the needed details. Since much of Willison's research code is public, he'll often tell coding agents to clone his repositories to `/tmp` and use them as input.

The key idea: coding agents mean a useful trick only needs to be figured out once. If that trick is documented somewhere with a working code example, agents can consult it and use it to solve any similarly shaped project in the future.

# Research: Using Claude to Build a Design Language for a Website
*Generated: 2026-08-09 | Scope: A hands-on, step-by-step guide to using Claude to design and build a design language for a personal portfolio website — covering visual identity definition, token generation, code output, and documentation — with the goal of creating a reusable workflow for future projects.*

## Research Outline

1. What is a design language and what does it take to build one
2. How to prompt Claude to define your visual identity
3. Translating design decisions into code with Claude
4. Using Claude to document and systematize the design language
5. End-to-end workflow: Claude-assisted portfolio build

---

## 1. What is a design language and what does it take to build one

### Design Systems 101

- **Source**: https://www.nngroup.com/articles/design-systems-101/
- **Summary**: A design system is a complete set of standards for managing design at scale through reusable components and patterns. The article covers the three core layers — style guides (branding, tone, visual standards), component libraries (reusable UI elements with code), and pattern libraries (layout templates) — and explains the team roles required to build and maintain one. It also frames the build-vs-adopt spectrum: teams can adopt an existing system, adapt one, or create custom, with cost and control increasing along that path.
- **Relevance**: Provides the canonical taxonomy of what a design system contains and the investment required — essential reading before asking Claude to help build one.

### What Are Design Tokens?

- **Source**: https://css-tricks.com/what-are-design-tokens/
- **Summary**: Design tokens are a platform-agnostic method for storing design variables — color, typography, spacing — in a single source of truth (typically JSON) that can be transformed into platform-specific code for web, iOS, and Android. Pioneered at Salesforce's Lightning Design System around 2016, they are consumed via tools like Amazon's Style Dictionary or Salesforce's Theo. The article surfaces the emerging debate around a shared token specification so any CSS-in-JS library could consume tokens consistently.
- **Relevance**: Explains the foundational technical primitive — design tokens — that gives a design language its scalability and cross-platform consistency; this is the artifact Claude will generate.

### Atomic Web Design

- **Source**: https://bradfrost.com/blog/post/atomic-web-design/
- **Summary**: Brad Frost introduces a five-level component hierarchy (atoms → molecules → organisms → templates → pages) inspired by chemistry, arguing that interfaces should be assembled from reusable elements rather than designed as isolated pages. Moving from abstract atoms (HTML primitives) up to concrete pages lets teams validate system decisions in real content context. The Pattern Lab tool implements this methodology, and the higher-level stages (organisms, templates) serve as communication artifacts for stakeholders.
- **Relevance**: Defines the component hierarchy model at the heart of most modern design systems — understanding this lets you prompt Claude to generate components at the right level of abstraction.

### Style Guides

- **Source**: https://bradfrost.com/blog/post/style-guides/
- **Summary**: Brad Frost catalogs six complementary types of style guides organizations use: brand identity guidelines, design language (higher-level philosophical direction), voice and tone, writing style, pattern libraries (front-end style guides built on atomic elements), and code style guides. He argues that using all six in concert positions a company for long-term consistency. Real-world guides typically blend several categories rather than isolating one.
- **Relevance**: Maps the full documentation ecosystem around a design language — showing what "building one" actually encompasses — so you know what to ask Claude to produce.

---

## 2. How to prompt Claude to define your visual identity

### Beyond The Hype: What AI Can Really Do For Product Design

- **Source**: https://www.smashingmagazine.com/2025/08/beyond-hype-what-ai-can-do-product-design/
- **Summary**: Author Nikita Samutin tests AI tools including Claude Sonnet 4 in Figma Make for product design tasks, finding that a two-step approach (structure first, then styling) produces the best results when applying color, typography, and layout. The article benchmarks three methods for feeding design system context to AI — direct component libraries, JSON style uploads, and staged workflows — and concludes that AI is most valuable as a visual exploration partner rather than a production-quality output tool. It documents where AI falls short (pixel-perfect fidelity, stable library support) while showing concrete wins in generating quick "what-if" visual concepts.
- **Relevance**: Directly names Claude as a tested tool for generating UI with color and typography decisions and gives a tested workflow for feeding visual identity context to an LLM.

### Prompting Is A Design Act

- **Source**: https://www.smashingmagazine.com/2025/08/prompting-design-act-brief-guide-iterate-ai/
- **Summary**: The article frames writing AI prompts as a creative brief — structured, intentional, and iterative — and introduces the W.I.R.E.+F.R.A.M.E. framework covering role definition, context supply, constraints, output format, task sequencing, tone/style reference, clarifying questions, memory use, and self-critique. It argues that vague prompts produce generic outputs while structured prompts unlock quality comparable to a well-written design brief given to a human collaborator. The "Reference Voice/Style" and "Expected Output" components are particularly applicable to visual identity work.
- **Relevance**: Provides a reusable prompt structure for briefing Claude on design decisions — directly applicable to generating color palettes, typography scales, and spacing systems with consistent style constraints.

### How To Make Your Design System AI-Ready

- **Source**: https://www.smashingmagazine.com/2026/06/how-make-design-system-ai-ready/
- **Summary**: The article argues that AI prototype quality degrades because of undocumented design decisions scattered across a system, and recommends replacing hard-coded values with named design tokens that AI can select from rather than invent. It introduces "spec files" — structured markdown documents containing spacing rules, color choices, and component usage guidelines that serve as machine-readable context for AI tools. The piece also recommends tooling like FigmaLint to audit and eliminate arbitrary values before handing off to AI.
- **Relevance**: Shows exactly how to structure color, typography, and spacing decisions as AI-readable context — the same format you would supply to Claude when asking it to define or extend a visual identity system.

### AI Design System – Are We There?

- **Source**: https://www.uxpin.com/studio/blog/ai-design-system/
- **Summary**: This article surveys the current state of AI in design systems, noting that AI can already generate foundational elements like spacing scales and typography scales from basic text prompts, while still requiring human judgment for emotionally resonant decisions and accessibility compliance. It covers design tokens as the key abstraction layer for AI-assisted multi-brand systems. Case studies from GitHub, Airbnb, and Spotify illustrate how AI helps scale visual consistency without sacrificing brand quality.
- **Relevance**: Establishes what an LLM can realistically produce when prompted for design tokens — color palettes as HEX values, typography families and weight/size hierarchies, spacing grids — setting accurate expectations for Claude-generated visual identity deliverables.

### Thinking Outside The Box: Digital Design In The AI Era

- **Source**: https://www.smashingmagazine.com/2026/07/digital-design-ai-era/
- **Summary**: Through the case study of designing MacPaw's AI assistant character Eney, the article examines deliberate visual identity choices — selecting pink over industry-dominant blue for warmth, circular silhouette for approachability, minimalist eye animation — and argues that taste and intentionality become more valuable as AI handles execution. Typography, naming, and every stylistic element were crafted by human designers even as AI assisted with implementation. The central thesis: AI amplifies design outcomes but requires a curator's eye to direct.
- **Relevance**: Illustrates the kind of visual identity brief (color rationale, shape language, typographic intent) that a designer must articulate to Claude to get purposeful rather than generic outputs.

---

## 3. Translating design decisions into code with Claude

### CSS Custom Properties Guide

- **Source**: https://css-tricks.com/a-complete-guide-to-custom-properties/
- **Summary**: A comprehensive reference covering CSS custom properties from basics through advanced patterns, emphasizing that unlike preprocessor variables they are dynamic — they respond to JavaScript, media queries, and the cascade at runtime. The guide covers the @property rule, inheritance tricks, Shadow DOM styling hooks, and combining custom properties with calc() for flexible math-driven layouts. It serves as the definitive reference for how custom properties behave once emitted from a token pipeline.
- **Relevance**: The exact output format Claude generates when translating design tokens — understanding cascade behavior and dynamic scoping is essential for prompting Claude to produce correct, non-naive CSS variable output.

### Tailwind CSS — Theme Variables

- **Source**: https://tailwindcss.com/docs/theme
- **Summary**: The official Tailwind v4 documentation explains the @theme directive, which maps CSS custom properties in namespaced groups (--color-*, --spacing-*, --breakpoint-*) directly to generated utility classes — defining --color-mint-500 automatically creates bg-mint-500, text-mint-500, and so on. It covers extending vs. replacing the default theme, consuming theme variables in arbitrary values and plain CSS, and accessing them in JavaScript. In v4, the config layer is expressed as CSS variable declarations rather than a JavaScript object.
- **Relevance**: The target output format when asking Claude to translate a brand's color and spacing tokens into a Tailwind v4 theme — Claude needs to emit @theme blocks with correct CSS variable namespacing to produce valid utility classes.

### Tailwind CSS — Adding Custom Styles

- **Source**: https://tailwindcss.com/docs/adding-custom-styles
- **Summary**: Describes multiple patterns for extending Tailwind: the @theme directive for token-level customization, arbitrary value syntax with square brackets for one-off overrides, and @layer base / @layer components / @utility for structured CSS additions. It shows how CSS variables defined in @theme can be consumed via var() inside component layers, and how the special --value() function enables token-aware functional utilities. These patterns form the full vocabulary for a design-token-driven Tailwind setup.
- **Relevance**: Claude can use these documented extension points as scaffolding when generating component stubs — knowing @layer components, @utility, and arbitrary-value syntax produces Tailwind output that integrates cleanly with a design token layer.

### The Design Graph

- **Source**: https://jxnblk.com/blog/design-graph/
- **Summary**: Brent Jackson proposes the Design Graph, a constraint-based conceptual model for organizing UI styles around interconnected nodes — scales, components, variants, and themes — rather than ad hoc per-component decisions. The model argues that shared naming conventions and schemas enable interoperability across tools, libraries, and organizations, making the overall system more powerful than its parts. It provides a formal vocabulary for the relationships between design decisions that a token system encodes.
- **Relevance**: The Design Graph's node taxonomy (scales → components → variants → themes) maps directly to the hierarchy Claude should reason about when decomposing a design brief into CSS custom properties, component stubs, and variant props.

---

## 4. Using Claude to document and systematize the design language

### Get Started with Storybook

- **Source**: https://storybook.js.org/docs/
- **Summary**: Storybook is a frontend workshop for building UI components in isolation, letting developers reach edge-case states without spinning up a full application. Its documentation tooling auto-analyzes components to produce usage guidelines, making it a natural home for design-system sites. Stories serve double duty: they capture component states and simultaneously form the backbone of a UI testing strategy.
- **Relevance**: Claude can complement Storybook by generating the narrative layer — usage rationale, decision logs, and do/don't guidance — that Storybook's structural auto-analysis cannot produce on its own.

### Design Tokens — Spectrum (Adobe)

- **Source**: https://spectrum.adobe.com/page/design-tokens/
- **Summary**: Design tokens are the foundational documentation layer of Adobe's design system, capturing core visual decisions — color, spacing, typography — as named, reusable variables that bridge design and engineering with a shared vocabulary. Adobe Spectrum treats token documentation as a first-class artifact alongside component docs, with each token having explicit rationale alongside its value. The page demonstrates how a token library becomes the primary contractual layer between designers and engineers.
- **Relevance**: Claude can document not just what token values are, but why they were chosen — producing the decision-log layer that raw token files and Figma variables typically omit.

### Design Tokens — Material Design 3 (Google)

- **Source**: https://m3.material.io/foundations/design-tokens/overview
- **Summary**: Material Design 3 uses design tokens as the single source of truth bridging design decisions and implementation across platforms and form factors. Tokens are organized by role (reference, system, component) rather than raw value, reflecting a structured, scalable model. Google's approach treats token documentation as the mechanism that makes a design language portable across platforms.
- **Relevance**: Claude can replicate this three-tier token documentation pattern (reference → system → component) for any design language, generating usage guidance and platform-mapping notes from a component inventory.

### Primer — The Design System for GitHub

- **Source**: https://primer.style/design/foundations/
- **Summary**: GitHub's Primer design system is organized into distinct layers: shared foundations (tokens, accessibility, icons), product UI, and brand UI. Each layer is documented with its own rationale and usage rules, ensuring building blocks remain consistent across all GitHub surfaces. The foundations layer — covering color, spacing, and typography tokens — underpins every higher-level component.
- **Relevance**: Primer's explicit layered structure (foundations → components → patterns) provides a clear documentation template that Claude can follow when auditing gaps, writing missing docs, or building out a new design language.

---

## 5. End-to-end workflow: Claude-assisted portfolio build

### Convert Figma to Code with AI

- **Source**: https://www.builder.io/blog/figma-to-code-ai
- **Summary**: Builder.io's Visual Copilot plugin converts Figma designs into production-ready code (React, Vue, Svelte, Angular, Tailwind, etc.) in a single click, using AI models paired with their open-source Mitosis compiler. It maps Figma components to existing codebase components and accepts custom prompts post-generation to enforce team style conventions. Responsive layouts are generated automatically even without strict Figma auto-layout compliance.
- **Relevance**: Covers the closest real-world analog to AI-assisted portfolio design workflow — a visual design system in Figma becoming a coded site through AI mediation.

### Announcing Visual Copilot 1.0

- **Source**: https://www.builder.io/blog/visual-copilot
- **Summary**: Builder.io's Visual Copilot 1.0 automates Figma-to-code conversion with beta users reporting 50–80% time savings. New features include AI semantic component mapping (auto-detecting which codebase components correspond to Figma components), code-style matching, and a roadmap item called Prompt-to-Design that generates full layouts inside Figma from a text prompt using the existing design system.
- **Relevance**: The Prompt-to-Design feature specifically addresses the "LLM making visual design decisions" use case — a direct parallel to using Claude to draft and iterate a portfolio site's visual language.

### Designing Beautiful Shadows in CSS

- **Source**: https://www.joshwcomeau.com/css/designing-shadows/
- **Summary**: Josh W. Comeau explains how to produce realistic CSS shadows by treating page elements as physical objects under a consistent light source. Key techniques include scaling offset/blur/opacity together as elevation increases, stacking multiple layered shadow declarations for depth, and tinting shadow hue to match the background rather than defaulting to grey. The article includes interactive demos for each technique.
- **Relevance**: A reference-quality article on a visual detail (shadows) that LLMs are frequently prompted to implement when generating or refining a portfolio site's visual language.

### Color Formats in CSS

- **Source**: https://www.joshwcomeau.com/css/color-formats/
- **Summary**: Surveys CSS color formats (hex, rgb(), hsl(), lch(), display-p3) and their trade-offs in expressiveness and human-readability. HSL is recommended as the most intuitive for design-system token work, while OKLCH is flagged as the future-facing choice once browser support matures. Practical guidance covers when to reach for each format in a design token system.
- **Relevance**: Directly applicable when prompting Claude to make or validate color decisions for a portfolio — understanding color format trade-offs shapes how Claude should generate and represent palette tokens.

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://www.nngroup.com/articles/design-systems-101/
- https://css-tricks.com/what-are-design-tokens/
- https://bradfrost.com/blog/post/atomic-web-design/
- https://bradfrost.com/blog/post/style-guides/
- https://www.smashingmagazine.com/2025/08/beyond-hype-what-ai-can-do-product-design/
- https://www.smashingmagazine.com/2025/08/prompting-design-act-brief-guide-iterate-ai/
- https://www.smashingmagazine.com/2026/06/how-make-design-system-ai-ready/
- https://www.uxpin.com/studio/blog/ai-design-system/
- https://www.smashingmagazine.com/2026/07/digital-design-ai-era/
- https://css-tricks.com/a-complete-guide-to-custom-properties/
- https://tailwindcss.com/docs/theme
- https://tailwindcss.com/docs/adding-custom-styles
- https://jxnblk.com/blog/design-graph/
- https://storybook.js.org/docs/
- https://spectrum.adobe.com/page/design-tokens/
- https://m3.material.io/foundations/design-tokens/overview
- https://primer.style/design/foundations/
- https://www.builder.io/blog/figma-to-code-ai
- https://www.builder.io/blog/visual-copilot
- https://www.joshwcomeau.com/css/designing-shadows/
- https://www.joshwcomeau.com/css/color-formats/

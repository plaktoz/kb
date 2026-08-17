# Lesson Plan: shadcn/ui — From Zero to Productive

*Source: `research/shadcn-ui-overview/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — The Mental Model
*Why this first: shadcn/ui's "copy code into your project" approach is counterintuitive for anyone who has used a traditional UI library. Get the mental model right before touching the CLI.*

### Lesson 1: What shadcn/ui Is (and Isn't)
**File:** `lessons/0001-what-is-shadcn.html`
**Key concepts:** code distribution · code ownership · CLI-copy model · not an npm package
**Source:** https://ui.shadcn.com/docs — defines shadcn/ui as a "code distribution platform"; components copied into your repo, not installed as a dependency
**Skill:** Write a two-sentence explanation of shadcn/ui that could convince a teammate who has only used MUI — no jargon allowed
**Reference doc:** `reference/mental-model.html`

### Lesson 2: The Five Principles
**File:** `lessons/0002-five-principles.html`
**Key concepts:** Open Code · Composition · Distribution (flat-file + CLI) · Beautiful Defaults · AI-Ready
**Source:** https://ui.shadcn.com/docs — the five explicit design principles behind every architectural decision in shadcn/ui
**Skill:** For each of the five principles, identify one concrete thing you will be able to do because of it (e.g. "Open Code → I can delete the hover state on Button without submitting a PR")
**Reference doc:** *(extend mental-model.html)*

---

## Module 2 — Choosing shadcn/ui
*Why this second: before writing a line of code, a developer needs to decide whether shadcn/ui is right for their situation. Module 2 builds the judgment to make that call.*

### Lesson 3: shadcn/ui vs. MUI, Chakra, and Ant Design
**File:** `lessons/0003-comparison.html`
**Key concepts:** GitHub stars · bundle size · Figma kit · design system · code ownership trade-off
**Source:** https://blog.logrocket.com/shadcn-ui-adoption-guide/ — head-to-head comparison with concrete numbers (stars, bundle KB, features matrix)
**Skill:** Fill out a blank comparison matrix (style, bundle, ownership, Figma, best-for) from memory, then check against the report table
**Reference doc:** `reference/comparison-matrix.html`

### Lesson 4: Pros, Cons, and When to Commit
**File:** `lessons/0004-pros-cons.html`
**Key concepts:** accessibility · Tailwind dependency · codebase growth · no Figma kit · young ecosystem
**Source:** https://blog.logrocket.com/shadcn-ui-adoption-guide/ — lists advantages (WCAG, AI-ready, bundle control) and drawbacks (Tailwind required, manual installs, no Figma)
**Skill:** Given three short project descriptions (solo portfolio, startup MVP, enterprise Figma-driven app), decide which library best fits each and explain one deciding factor per choice
**Reference doc:** *(extend comparison-matrix.html)*

---

## Module 3 — Installation & First Components
*Why this third: with the model and trade-offs clear, this module gets hands-on. Every step is a concrete command or file the learner can run right now.*

### Lesson 5: First-Time Setup on Next.js
**File:** `lessons/0005-nextjs-setup.html`
**Key concepts:** `pnpm create next-app` · `shadcn init` · path alias `@/*` · tsconfig
**Source:** https://ui.shadcn.com/docs/installation/next — canonical four-command walkthrough for Next.js from scratch
**Skill:** Follow the four-command sequence in order (create → init → add button → import) and paste the import line you would write at the top of `app/page.tsx`
**Reference doc:** `reference/setup-cheatsheet.html`

### Lesson 6: components.json — The Decisions You Can't Undo
**File:** `lessons/0006-components-json.html`
**Key concepts:** `style` (new-york vs default) · `baseColor` · `cssVariables` · path aliases · irreversible settings
**Source:** https://ui.shadcn.com/docs/components-json — explains which settings are locked at init and what each controls
**Skill:** Before running `shadcn init` on an imaginary project, write out the three lock-in decisions you would make and why — then explain what you would have to do if you got one wrong
**Reference doc:** *(extend setup-cheatsheet.html)*

### Lesson 7: Adding and Using Your First Component
**File:** `lessons/0007-first-component.html`
**Key concepts:** `shadcn add` · component import path · `variant` prop · `size` prop · `buttonVariants` helper
**Source:** https://ui.shadcn.com/docs/components/button — demonstrates the install-import-use loop that applies to every component; Button variants and sizes
**Skill:** Write the JSX for a Button that uses the `outline` variant and `sm` size, and a second Button that renders as an `<a>` tag using `buttonVariants` — no copy-paste allowed
**Reference doc:** `reference/component-patterns.html`

### Lesson 8: The CLI Reference
**File:** `lessons/0008-cli-reference.html`
**Key concepts:** `init` · `add` · `view` · `search` · `migrate` · `apply` · `-o` flag · `--dry-run` · monorepo `-c` flag
**Source:** https://ui.shadcn.com/docs/cli — full CLI surface: all sub-commands and key flags
**Skill:** Given a scenario (monorepo, overwrite an existing component, preview source before installing), write the exact CLI command you would run for each
**Reference doc:** `reference/cli-cheatsheet.html`

---

## Module 4 — Customisation & Production Patterns
*Why this last: theming and production patterns build on a working install. Concepts like CSS variables and form wiring make most sense after the learner has added real components.*

### Lesson 9: CSS Variable Theming and Dark Mode
**File:** `lessons/0009-theming.html`
**Key concepts:** semantic token pairs (`primary` / `primary-foreground`) · `--radius` variable · `:root` vs `.dark` · theme editor · `--no-css-variables` warning
**Source:** https://ui.shadcn.com/docs/theming — CSS variable architecture, semantic surface/foreground pattern, dark mode `.dark` class, `--radius` calc pattern
**Skill:** Write the `:root` CSS block that changes the primary color to a custom brand purple and adjusts the border radius to pill-shaped — derive the `primary-foreground` contrast value yourself
**Reference doc:** `reference/theming-tokens.html`

### Lesson 10: Production Best Practices
**File:** `lessons/0010-production-patterns.html`
**Key concepts:** Blocks + Lift Mode · Form + react-hook-form + Zod · code splitting · theme editor workflow · v0 integration
**Source:** https://blog.logrocket.com/shadcn-ui-adoption-guide/ — six production patterns: visual config first, Blocks/Lift Mode, Form component, code splitting, theme editor, v0 AI iteration
**Skill:** Given a sign-up form with email + password fields that must be validated, sketch the component tree (which shadcn/ui components + which libraries) and explain where Zod lives in the data flow
**Reference doc:** *(extend component-patterns.html)*

---

## Suggested Teaching Order

Progress linearly: mental model → evaluation → install → components → theming → production. Each module depends on the prior one. A learner who skips Module 2 will make init decisions blindly; a learner who skips Module 3 won't have a working project to apply theming to.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/mental-model.html` | Visual diagram of copy-to-project vs npm-package model; five principles cheat sheet |
| `reference/comparison-matrix.html` | Full comparison table (stars, bundle, ownership, Figma, best-for) with notes |
| `reference/setup-cheatsheet.html` | Four-command setup sequence; components.json field reference; path alias config |
| `reference/component-patterns.html` | Install-import-use loop; Button variants/sizes table; buttonVariants helper pattern |
| `reference/cli-cheatsheet.html` | All CLI sub-commands with flags and example invocations |
| `reference/theming-tokens.html` | Semantic token pairs table; --radius calc examples; :root / .dark template |

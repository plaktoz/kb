# Claude Design Language: Step-by-Step Guide

A hands-on workflow for using Claude to build a design language for a personal portfolio website — and reuse the same process on future projects.

**What you will produce:** a set of design tokens (colors, typography, spacing), CSS/Tailwind code, and documentation that together form a coherent visual identity.

---

## Mental model before you start

A design language has three layers, built bottom-up:

1. **Tokens** — the named variables: `--color-brand-500`, `--font-size-lg`, `--space-4`
2. **Components** — reusable UI pieces built from those tokens: buttons, cards, nav
3. **Documentation** — the *why* behind every decision, so the system stays coherent as it grows

Claude can generate and document all three, but only if you brief it well. Generic prompts → generic output.

---

## Step 1: Write a design brief (15 min)

Before touching code, give Claude a structured brief using the **W.I.R.E.+F.R.A.M.E.** structure:

| Letter | What to define |
|--------|---------------|
| **W** — Who/Role | "You are a senior visual designer helping me build a personal portfolio design system" |
| **I** — Intent | What the site is for and who visits it |
| **R** — Reference style | 3–5 adjectives + reference sites you admire |
| **E** — Expected output | Exactly what you want Claude to return (JSON tokens, CSS variables, prose rationale) |
| **F** — Format | Markdown, JSON, CSS — pick one per prompt |
| **R** — Rules/Constraints | Accessibility (WCAG AA), max palette size, framework choice |
| **A** — Ask Claude to clarify | "Ask me if anything is ambiguous before generating" |
| **M** — Memory/context | Paste previous decisions when continuing a conversation |
| **E** — Evaluate/self-critique | "After generating, tell me what you'd improve" |

**Starter prompt template:**

```
You are a senior visual designer. I am building a personal portfolio website.

Audience: hiring managers and collaborators in [your field].
Tone: [e.g. "professional but warm, minimal, not corporate"].
Reference sites I like: [site 1], [site 2], [site 3].
Constraints: WCAG AA contrast, max 4 brand colors, Tailwind v4.

Generate a visual identity brief covering:
- Color palette (with hex values and roles: background, surface, brand, accent, text, muted)
- Type scale (font families, weights, and 6 size steps)
- Spacing scale (base unit and 8 steps)

For each decision, explain *why* in one sentence.
Ask me to clarify anything before generating.
After generating, list 2 things you'd reconsider.
```

> Key insight: AI gives generic results when the brief is vague. The more emotional and specific your reference adjectives and sites, the more distinctive the output. See [[thinking-outside-box-digital-design-ai-era]] for why taste-direction matters.

---

## Step 2: Generate your color palette

Run the brief from Step 1. Claude will return hex values — immediately validate them:

**Contrast check prompt (follow-up):**
```
Check each color combination I'll use for text-on-background against WCAG AA (4.5:1 for normal text, 3:1 for large). List any failures and suggest fixes.
```

**Color format choice:**
- Use **HSL** for token work — it's human-readable and easy to adjust (`hsl(220, 70%, 50%)`)
- Target **OKLCH** for future-proofing once browser support is stable
- Avoid raw hex in tokens — always name them by role, not value

**Output to ask for:**
```
Return the palette as CSS custom properties in this format:

:root {
  --color-bg:        hsl(...);
  --color-surface:   hsl(...);
  --color-brand:     hsl(...);
  --color-accent:    hsl(...);
  --color-text:      hsl(...);
  --color-muted:     hsl(...);
}
```

---

## Step 3: Generate typography and spacing tokens

Follow the same brief pattern. Keep this as a separate prompt from color — focused prompts give better output.

**Typography prompt:**
```
Using the visual brief above, generate a type scale for my portfolio site.

Return:
- Font family choices (one for headings, one for body — free Google Fonts or system stack)
- A 6-step size scale in rem: xs, sm, base, lg, xl, 2xl
- Weight pairings for each role (heading, body, caption, label)
- Line-height recommendations per role

Format as CSS custom properties under :root {}.
```

**Spacing prompt:**
```
Generate a spacing scale based on a 4px base unit with 8 steps.
Return as CSS custom properties: --space-1 through --space-8.
Also define --space-section (for vertical section padding) and --space-content (max content width).
```

---

## Step 4: Make the system AI-ready with a spec file

Before generating components, consolidate your tokens into a **spec file** — a structured markdown document Claude reads as context. This prevents Claude from inventing values instead of using yours.

**Spec file template** (`design-spec.md`):

```markdown
# Design Spec

## Colors
- Background: var(--color-bg) = hsl(...)
- Surface: var(--color-surface) = hsl(...)
- Brand: var(--color-brand) = hsl(...)
- Accent: var(--color-accent) = hsl(...)
- Text: var(--color-text) = hsl(...)
- Muted: var(--color-muted) = hsl(...)

## Typography
- Heading font: [family], weights: 600/700
- Body font: [family], weight: 400
- Size scale: xs=0.75rem, sm=0.875rem, base=1rem, lg=1.125rem, xl=1.25rem, 2xl=1.5rem

## Spacing
- Base unit: 4px
- Scale: space-1=4px … space-8=32px
- Section padding: var(--space-section) = 80px
- Content max-width: var(--space-content) = 720px

## Rules
- Never hard-code a color value — always use a token
- Use WCAG AA minimum contrast
- All font sizes in rem
```

> Paste this file at the start of every new Claude conversation about your site. It eliminates arbitrary values and keeps Claude anchored to your decisions.

---

## Step 5: Translate tokens to Tailwind v4

Tailwind v4 uses CSS custom properties directly — your token layer *is* your theme.

**Prompt:**
```
Convert my design spec (pasted below) into a Tailwind v4 @theme block.
Each color token should map to a --color-* variable so Tailwind generates bg-*, text-*, border-* utilities automatically.
Each spacing token should map to --spacing-* variables.

[paste design-spec.md]
```

**Expected output structure:**
```css
@import "tailwindcss";

@theme {
  --color-bg:      hsl(...);
  --color-surface: hsl(...);
  --color-brand:   hsl(...);
  /* ... */

  --font-sans: "Inter", system-ui, sans-serif;
  --font-heading: "Cal Sans", serif;

  --text-xs:  0.75rem;
  --text-sm:  0.875rem;
  --text-base: 1rem;
  /* ... */

  --spacing-section: 80px;
  --spacing-content: 720px;
}
```

Now `bg-brand`, `text-muted`, `p-section` etc. are valid utility classes throughout your site.

---

## Step 6: Generate component stubs (atomic hierarchy)

Work bottom-up using the atomic model: atoms → molecules → organisms.

**Prompt pattern for each component:**
```
Using my design spec (pasted below), generate a [component name] component in [React/HTML + Tailwind].

Rules:
- Use only token-based utility classes (no arbitrary values like [#3b82f6])
- Include variants: [list variants, e.g. primary / ghost / destructive]
- Add a brief JSDoc comment explaining when to use each variant

[paste design-spec.md]
```

**Suggested order for a portfolio:**
1. **Atoms**: Button, Tag, Badge, Avatar
2. **Molecules**: ProjectCard, SkillChip, SocialLink
3. **Organisms**: Hero, ProjectGrid, ContactForm, NavBar
4. **Templates**: HomePage, ProjectPage, AboutPage

---

## Step 7: Document the design language

Use Claude to generate the documentation layer — the *why* that raw token files omit.

**Decision log prompt:**
```
Based on the design choices below, write a decision log entry for each major choice.
Format: "We chose X because Y. We considered Z but rejected it because W."

[paste your spec + any rationale Claude gave in earlier steps]
```

**Style guide prompt:**
```
Write a concise style guide section for [component name].
Include:
- When to use it (1–2 sentences)
- When NOT to use it (1–2 sentences)
- One "do" and one "don't" example (as markdown code blocks)
```

**Reference systems for structure:**
- [[material-design-3-tokens]] — three-tier token model (reference → system → component)
- [[github-primer-design-system]] — foundations → components → patterns layer structure
- Adobe Spectrum treats token docs as a first-class artifact alongside component docs

---

## Step 8: Iterate with Claude as a visual exploration partner

Claude is best used for *exploration*, not final output. Use it to generate "what-if" variations quickly:

**Variation prompt:**
```
Keep my typography and spacing unchanged. Generate 3 alternative color palette options for the same brief — each with a different emotional tone (e.g. warmer, darker, more energetic). Return each as a :root {} block with hex values.
```

**Refinement loop:**
1. Generate → review visually in browser
2. Note what feels off (too cold, too crowded, too busy)
3. Give Claude that specific feedback: "the brand color feels corporate — try a warmer hue in the 20–40° range"
4. Regenerate that token only, keeping everything else fixed

> AI output quality degrades when you change too many things at once. Fix one token layer per iteration.

---

## Step 9: Reuse this as a workflow template

Save your `design-spec.md` as a reusable template. For each new project:

1. Duplicate `design-spec.md` → fill in new adjectives and reference sites
2. Run Steps 2–3 (palette + type/spacing generation)
3. Run Step 5 (Tailwind @theme generation)
4. Reuse component stubs from Step 6 — they are token-driven, so they automatically reflect the new palette

The same Claude prompts work across projects. The spec file is the only thing that changes.

---

## Quick reference: prompt cheatsheet

| Goal | Key prompt phrase |
|------|-------------------|
| Visual brief | "You are a senior visual designer... tone: [adjectives]... reference sites: [list]" |
| Color palette | "Return as CSS custom properties with role names, explain each choice in one sentence" |
| Contrast check | "Check all text-on-background combinations against WCAG AA, list failures" |
| Token → Tailwind | "Convert my design spec into a Tailwind v4 @theme block" |
| Component stub | "Use only token-based utility classes, no arbitrary values, include variants" |
| Documentation | "Write a decision log: we chose X because Y, considered Z but rejected it because W" |
| Iterate | "Keep everything fixed except [specific token], generate 3 alternatives" |

---

## Related notes

- [[atomic-web-design]] — Brad Frost's atoms → molecules → organisms hierarchy
- [[design-tokens-css-tricks]] — design tokens as platform-agnostic single source of truth
- [[tailwind-v4-theme-variables]] — how @theme maps CSS variables to utility classes
- [[prompting-is-a-design-act-wiref-framework]] — the W.I.R.E.+F.R.A.M.E. prompting structure
- [[how-to-make-design-system-ai-ready]] — spec files and named tokens for AI input

**Source research:** [[research/claude-design-language-website/report]]

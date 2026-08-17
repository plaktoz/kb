# Lesson Plan: IBM Carbon Design System

*Source: `research/ibm-carbon-design-system/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations
*Before touching a single component, learners must understand why Carbon exists and how its token-based architecture works — these mental models prevent misuse of every later tool.*

### Lesson 1: What is Carbon? Philosophy and Purpose
**File:** `lessons/0001-what-is-carbon.html`
**Key concepts:** IBM Design Language · five core principles · open-source design system · modular components
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/all-about-carbon/what-is-carbon.mdx — Carbon's five principles: Open, Inclusive, Modular & Flexible, User-first, Consistent; serves as IBM's digital brand expression
**Skill:** Write a one-paragraph explanation of why a design system like Carbon exists, naming at least three of its five principles and describing a real product problem each principle solves.
**Reference doc:** `reference/carbon-overview.html`

### Lesson 2: The Token System and Color Themes
**File:** `lessons/0002-color-tokens.html`
**Key concepts:** design tokens · color token groups · four built-in themes · WCAG contrast ratios · interaction states
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/color/overview.mdx — token-based color system with 10 groups; four themes (White, Gray 10, Gray 90, Gray 100); WCAG 4.5:1 small text / 3:1 large text
**Skill:** Given a UI mockup description with five color decisions, label each with the correct Carbon token name (e.g., `$text-primary`, `$layer-hover`, `$border-subtle`) rather than a hex value.
**Reference doc:** `reference/color-tokens.html`

### Lesson 3: Typography and Spacing
**File:** `lessons/0003-typography-spacing.html`
**Key concepts:** type tokens · productive vs expressive sets · IBM Plex · spacing scale · Stack component
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/typography/overview.mdx AND https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/spacing/overview.mdx — type tokens (productive `-01` / expressive `-02`); spacing tokens from `$spacing-01` (2px) to `$spacing-13` (160px) on a 2/4/8-multiple scale
**Skill:** Given a design spec describing a heading, body text, and three spaced UI elements, write the corresponding Sass token declarations using `@include type-style()` and `$spacing-XX` values.
**Reference doc:** `reference/typography-spacing.html`

---

## Module 2 — Layout, Motion, and Accessibility
*With tokens understood, learners build the structural and behavioral layer: how to place things on the page, how to move them, and how to ensure every user can access them.*

### Lesson 4: The 2x Grid System
**File:** `lessons/0004-grid-system.html`
**Key concepts:** 8px mini units · breakpoints · fluid vs fixed vs hybrid grids · `<Grid>` and `<Column>` · aspect ratios
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/2x-grid/overview.mdx — 5 breakpoints (320px–1584px); 4/8/16 column counts; 32px gutters; fluid/fixed/hybrid grid types
**Skill:** Sketch (or describe in text) a three-section landing page layout — hero, two-column content, full-width footer — labeling the `lg`, `md`, and `sm` column span values for each section.
**Reference doc:** `reference/grid-system.html`

### Lesson 5: Motion Design
**File:** `lessons/0005-motion-design.html`
**Key concepts:** productive vs expressive motion · easing curves · duration tokens · motion sensitivity
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/motion/overview.mdx — productive (fast, subtle, microinteractions) vs expressive (vibrant, significant moments); duration tokens 70ms–700ms; three easing types (standard, entrance, exit)
**Skill:** For five given UI interactions (dropdown open, page transition, button click, toast notification, background dim), assign the correct motion style (productive or expressive) and the closest duration token, explaining each choice in one sentence.
**Reference doc:** `reference/motion-tokens.html`

### Lesson 6: Accessibility in Carbon
**File:** `lessons/0006-accessibility.html`
**Key concepts:** WCAG 2.1 AA · Section 508 · keyboard navigation · screen readers · IBM Equal Access Toolkit · color-blind-safe patterns
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/guidelines/accessibility/overview.mdx — six user groups; IBM Accessibility Checklist based on WCAG AA; recommended tools (IBM Equal Access Toolkit, Stark, High Contrast Chrome plugin)
**Skill:** Audit the Button component usage in Lesson 8's exercise using the checklist: does it have a visible focus state? Does an icon-only button have a tooltip? Is the label verb+noun? Write a 3-item accessibility pass/fail report.
**Reference doc:** *(extend existing reference/carbon-overview.html)*

---

## Module 3 — Component Library in Depth
*Learners now have the vocabulary (tokens, grid, accessibility) to study components correctly — understanding not just what they do, but when to use each variant and why.*

### Lesson 7: Component Library Map
**File:** `lessons/0007-component-library.html`
**Key concepts:** 49 components · 7 categories · UI Shell · inputs vs navigation vs data display vs feedback vs overlays
**Source paper:** https://github.com/carbon-design-system/carbon-website/tree/main/src/pages/components — 49 components across 7 categories: UI Shell, Inputs & Controls, Navigation, Data Display, Feedback & Status, Overlays, Content & Layout
**Skill:** For a described product (a file management dashboard), list which 6–8 Carbon components from at least 4 categories you would use for the core UI, and justify each choice in one sentence.
**Reference doc:** `reference/component-map.html`

### Lesson 8: Buttons and Controls
**File:** `lessons/0008-buttons-controls.html`
**Key concepts:** button variants · emphasis hierarchy · label rules · icon placement · inline loading · one primary per screen
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/button/usage.mdx — five variants (Primary/Secondary/Tertiary/Ghost/Danger); verb+noun label rule; seven sizes; icons right of label; one primary per page
**Skill:** Review a provided button spec with five buttons on one screen — identify all the violations (wrong variant count, bad labels, mixed sizes) and rewrite the spec correctly.
**Reference doc:** `reference/component-map.html` *(extend)*

### Lesson 9: Modals and Data Tables
**File:** `lessons/0009-modals-datatables.html`
**Key concepts:** modal variants · focus trapping · DataTable variants · sorting states · skeleton loading · batch actions
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/modal/usage.mdx AND https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/data-table/usage.mdx — five modal variants; focus must be trapped inside modal; four DataTable variants; skeleton states preferred over spinners
**Skill:** Given a scenario (user clicks "Delete account"), decide which modal variant to use, describe the correct focus behavior on open, and write the button label for the destructive action.
**Reference doc:** *(extend reference/component-map.html)*

---

## Module 4 — Building with Carbon
*With concepts solid, learners build a real project: install Carbon, scaffold a Next.js app with the UI Shell, assemble a page with the grid, and customize via theming — mirroring the official tutorial arc.*

### Lesson 10: Setting Up Carbon in a React Project
**File:** `lessons/0010-setup.html`
**Key concepts:** `@carbon/react` · Sass configuration · `@use '@carbon/react'` · TypeScript setup · framework guides
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon/main/packages/react/README.md — `yarn add @carbon/react sass @carbon/icons-react`; `@use '@carbon/react'` in globals.scss; component import syntax; Dart Sass requirement
**Skill:** Write out, from memory, the five commands and two file changes needed to go from a blank Next.js project to a working Carbon app that renders a `<Button>` with styles applied.
**Reference doc:** `reference/setup-guide.html`

### Lesson 11: Building Your First Carbon Page
**File:** `lessons/0011-first-page.html`
**Key concepts:** UI Shell components · `<Theme>` wrapper · `<Grid>` and `<Column>` · multiple component imports · ARIA labels for duplicate nav elements
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/developing/react-tutorial/step-1.mdx AND https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/developing/react-tutorial/step-2.mdx — `providers.js` with `<Theme theme="g100">`; `Header`, `SideNav`; `<Column lg={16} md={8} sm={4}>`; unique `aria-label` for multiple `<nav>`
**Skill:** Write the JSX for a landing page section with a full-width banner at large breakpoint, two equal columns at medium, and a single column at small — using `<Grid>` and `<Column>` with correct responsive props.
**Reference doc:** `reference/setup-guide.html` *(extend)*

### Lesson 12: Theming, Customization, and Content Writing
**File:** `lessons/0012-theming-content.html`
**Key concepts:** token override · custom themes · Sass `with` keyword · IBM voice and tone · verb+noun · sentence case
**Source paper:** https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/themes/overview.mdx AND https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/guidelines/content/overview.mdx — token override via `@use` with `$theme: (background: #e2e2e2)`; IBM voice: clear, logical, data-driven; tone adapts to context; error messages are phrase-based
**Skill:** Given a list of five UI strings violating IBM voice guidelines (boastful, noun-only, title case, truncated), rewrite each to comply — and write the Sass snippet to apply a custom background color token to the project.
**Reference doc:** `reference/theming-content.html`

---

## Suggested Teaching Order

Follow modules 1 → 4 sequentially. Module 1 builds conceptual fluency with tokens — skipping it makes component usage feel arbitrary. Module 2 provides the structural and behavioral rules needed before assembling components (Module 3). Module 4 is purely hands-on and assumes all prior vocabulary; lessons 10–12 mirror the official Carbon tutorial arc and can be done alongside a local Next.js project for maximum retention.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/carbon-overview.html` | Carbon philosophy, five principles, package ecosystem, accessible design checklist |
| `reference/color-tokens.html` | All 10 token groups with names, roles, light/dark values, interaction state tokens |
| `reference/typography-spacing.html` | Type token tables (productive + expressive), IBM Plex stacks, spacing scale (01–13) |
| `reference/grid-system.html` | Breakpoint table, column counts, gutter sizes, fluid/fixed/hybrid grid diagram |
| `reference/motion-tokens.html` | Duration token table, easing cubic-bezier values, productive vs expressive decision guide |
| `reference/component-map.html` | All 49 components by category with one-line descriptions and when-to-use notes |
| `reference/setup-guide.html` | Step-by-step install commands, file changes, providers.js template, common errors |
| `reference/theming-content.html` | Token override Sass syntax, four built-in themes, IBM voice/tone quick reference |

# Research: IBM Carbon Design System
*Generated: 2026-08-17 | Scope: Comprehensive overview of IBM Carbon Design System covering design principles, component library, step-by-step setup in a React project, and best practices for building consistent UIs — aimed at deep practical learning for personal and professional use.*

## Research Outline

1. What is IBM Carbon Design System? — origin, philosophy, and why it exists
2. Core design principles — color, typography, spacing, grid, motion, and accessibility
3. Component library — key components, their usage patterns, and variants
4. Step-by-step setup — installing Carbon in a React project and building a simple UI
5. Best practices — theming, customization, accessibility compliance, and common pitfalls

---

## 1. What is IBM Carbon Design System?

### Carbon GitHub Repository (carbon-design-system/carbon)

- **Source**: https://github.com/carbon-design-system/carbon
- **Summary**: Carbon is IBM's open-source design system for products and experiences. It is a monorepo containing React and Web Component libraries, Sass styles, design tokens, icons, pictograms, and developer tooling. Core packages include `@carbon/react`, `@carbon/web-components`, `@carbon/styles`, `@carbon/themes`, `@carbon/icons`, `@carbon/colors`, `@carbon/layout`, `@carbon/type`, `@carbon/motion`, and `@carbon/grid`. Community-maintained libraries also exist for Angular, Svelte, and Vue. Licensed under Apache 2.0.
- **Relevance**: Primary source for understanding Carbon's scope, structure, and the full package ecosystem.

### What is Carbon — Origin and Philosophy

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/all-about-carbon/what-is-carbon.mdx
- **Summary**: Carbon is IBM's open-source design system for building consistent digital products, grounded in the IBM Design Language. The name draws from nature — carbon atoms form complex structures from simpler compounds, mirroring how individual components combine into sophisticated designs. Its five core principles are: **Open** (collaboratively built; users are contributors), **Inclusive** (accessible regardless of ability), **Modular & Flexible** (components interoperate seamlessly), **User-first** (driven by rigorous research), and **Consistent** (every element works together for cohesive UX). Carbon serves as "the digital expression of the IBM brand," underlying every IBM digital interaction.
- **Relevance**: Defines the philosophical foundation and strategic purpose of Carbon — essential context before learning its implementation.

---

## 2. Core Design Principles

### Color System

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/color/overview.mdx
- **Summary**: Carbon's color system uses the IBM Design Language palette, with neutral grays as dominant tones and core blue as the primary action color. Colors are applied through **tokens** — role-based identifiers that replace hard-coded hex values — enabling consistent application across themes and inline dark/light mode switching. Ten core token groups exist: Background, Layer, Field, Border, Text, Link, Icon, Support, Focus, and Skeleton. Carbon ships four themes: White and Gray 10 (light), Gray 90 and Gray 100 (dark). Interaction states (hover, active, selected, focus, disabled) each have dedicated tokens with defined contrast ratios. WCAG requirements: 4.5:1 for small text, 3:1 for large text and graphics.
- **Relevance**: Establishes the token-based color architecture that underpins every component and theme in Carbon.

### Typography System

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/typography/overview.mdx
- **Summary**: Carbon manages typography through **type tokens** — preset configurations of font size, weight, and line height — built on IBM Plex, an open-source typeface in three stacks: Sans-serif (primary), Serif, and Mono. Two distinct token sets exist: **Productive** (condensed, task-focused, fixed sizes, suffixed `-01`) and **Expressive** (larger, editorial, responsive across breakpoints, suffixed `-02`). The scale starts at 12px and follows a mathematical formula. Recommended weights are Light, Regular, and SemiBold. Italics are reserved for emphasis only. Color in type stays neutral for running text; blue is reserved for links.
- **Relevance**: Explains how Carbon's type system creates hierarchy and visual consistency without custom CSS.

### Spacing System

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/spacing/overview.mdx
- **Summary**: Carbon's spacing system uses multiples of 2, 4, and 8, exposed as tokens ranging from `$spacing-01` (2px) to `$spacing-13` (160px). Tokens replace raw CSS values for `margin` and `padding`. The **Stack component** spaces grouped items using the same scale. Key principles: more space signals higher importance; proximity implies relationship; white space reduces cognitive overload. Tokens are not responsive by default, but stepping up/down the scale at breakpoints is acceptable.
- **Relevance**: Provides the spacing vocabulary that ensures consistent layout relationships within and between components.

### 2x Grid System

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/2x-grid/overview.mdx
- **Summary**: Carbon's 2x Grid uses 8px mini units as its geometric foundation, built on the principle of dividing or multiplying by two. Breakpoints: Small (320px, 4 cols), Medium (672px, 8 cols), Large (1056px, 16 cols), X-Large (1312px, 16 cols), Max (1584px, 16 cols). Gutters are 32px total (16px padding per side). Three grid types exist: **Fluid** (columns scale, count fixed per breakpoint), **Fixed** (set unit sizes), and **Hybrid** (combines both). Aspect ratios 1:1, 2:1, 2:3, 3:2, 4:3, 16:9 are recommended for visual unity.
- **Relevance**: The grid system is the structural backbone for building properly aligned, responsive layouts in Carbon.

### Motion System

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/motion/overview.mdx
- **Summary**: Carbon defines two motion styles: **Productive** (subtle, efficient, fast — for microinteractions like dropdowns and button states) and **Expressive** (vibrant, attention-capturing — reserved for significant moments like new pages or primary actions). Three easing types cover standard, entrance, and exit scenarios with distinct CSS `cubic-bezier` values for each style. Duration tokens range from `duration-fast-01` (70ms, buttons/toggles) to `duration-slow-02` (700ms, background dimming). Duration scales with animation size. Motion should always be purposeful, responsive, and unobtrusive, with static alternatives provided for users with motion sensitivity.
- **Relevance**: Motion design is a first-class system in Carbon; using its tokens ensures animations feel consistent and intentional rather than ad hoc.

### Accessibility Guidelines

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/guidelines/accessibility/overview.mdx
- **Summary**: Carbon follows IBM's Accessibility Checklist based on WCAG 2.1 AA and Section 508. Key user groups addressed include blind users (screen reader support), low-vision users (contrast and readability), color-blind users (no color-only signals), deaf/hard-of-hearing users (video captions), physically disabled users (full keyboard navigation), and cognitively disabled users (minimized complexity). Recommended tools: IBM Equal Access Toolkit, High Contrast Chrome plugin, Stark (Figma plugin), and color contrast checkers. Accessibility improvements universally benefit all users — better contrast aids outdoor reading; keyboard navigation boosts productivity.
- **Relevance**: Accessibility is built into every Carbon component by default; understanding these principles ensures correct usage without breaking compliance.

---

## 3. Component Library

### Component Library Overview (49 Components)

- **Source**: https://github.com/carbon-design-system/carbon-website/tree/main/src/pages/components
- **Summary**: Carbon ships 49 components across 7 categories. **UI Shell**: Header, Left Panel, Right Panel. **Inputs & Controls**: Accordion, Button, Checkbox, Date Picker, Dropdown, File Uploader, Number Input, Radio Button, Search, Select, Slider, Text Input, Toggle. **Navigation**: Breadcrumb, Menu, Menu Buttons, Overflow Menu, Pagination, Progress Indicator, Tabs, Tree View. **Data Display**: Contained List, Data Table, List, Structured List, Tag, Tile. **Feedback & Status**: Inline Loading, Loading, Notification, Progress Bar. **Overlays**: Modal, Popover, Toggletip, Tooltip. **Content & Layout**: AI Label, Code Snippet, Content Switcher, Form, Link.
- **Relevance**: Provides a full map of available components to understand what Carbon covers out of the box before writing custom code.

### Button Component Usage

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/button/usage.mdx
- **Summary**: Five button variants: **Primary** (one per screen, principal CTA), **Secondary** (Cancel/Back, paired with primary), **Tertiary** (independent or grouped), **Ghost** (least emphasis, supplementary), **Danger** (destructive actions). Seven sizes from extra small to 2XL — never mix sizes within a group. Label format: `{verb} + {noun}` (e.g., "Save file"). Full-page designs: primary button left-aligned. Dialogs/wizards: primary button right-aligned. Icons appear to the right of labels; icon-only buttons always require a tooltip. Buttons support inline loading states with the primary button disabled during processing.
- **Relevance**: Button is the most frequently used component; its hierarchy rules (one primary per screen, verb+noun labels) apply universally across all Carbon UIs.

### Modal Component Usage

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/modal/usage.mdx
- **Summary**: Five modal variants: **Passive** (informational only), **Transactional** (cancel + primary action required), **Danger** (destructive/irreversible transactional), **Acknowledgment** (single OK button), **Progress** (multi-step with Previous/Next). Key best practices: trap focus within modal and set initial focus to the first input; always support ESC key and × close icon; validate before closing (keep modal open on errors with inline messaging); disable primary button during processing; never scroll horizontally. Use modals sparingly — if a task is repeated frequently, place it on the main page instead.
- **Relevance**: Modal misuse is a common pitfall; these guidelines prevent accessibility failures (focus trapping) and UX anti-patterns (overusing modals for routine tasks).

### DataTable Component Usage

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/data-table/usage.mdx
- **Summary**: Four variants: Default, With Selection (checkbox multi or radio single), With Expansion (collapsible rows), and Expandable + Selectable (combined). Use for organizing data where users navigate to specific records. Avoid as a spreadsheet replacement. Key behaviors: sorting has three states (unsorted, sorted-up, sorted-down — icon only shows on active column); batch actions appear on row selection and disable inline row actions; use skeleton states (not spinners) for delayed content. Column header titles: sentence case, one or two words, truncate at two lines with tooltip for overflow.
- **Relevance**: DataTable is Carbon's most complex component; following its sizing and behavioral rules prevents visual inconsistency and interaction conflicts.

---

## 4. Step-by-Step Setup

### Carbon React Package Installation

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon/main/packages/react/README.md
- **Summary**: Install via `npm install -S @carbon/react` or `yarn add @carbon/react`. Dart Sass is required for compiling styles. Load all component styles at once with `@use '@carbon/react'` in a `.scss` file, or scope to specific components with `@use '@carbon/react/scss/components/button'`. Import components with `import { Button } from '@carbon/react'`. Icons are available via `import { Add } from '@carbon/react/icons'`. TypeScript users should add `"skipLibCheck": true` to `tsconfig.json`. Framework-specific Sass guides exist for Next.js, Remix, Gatsby, Vite, and Webpack.
- **Relevance**: The canonical quickstart — these are the exact commands needed to add Carbon to any React project.

### React Tutorial Step 1 — Installation and UI Shell

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/developing/react-tutorial/step-1.mdx
- **Summary**: Using Next.js 13: install `@carbon/react`, `sass`, and `@carbon/icons-react` via yarn. Rename `globals.css` to `globals.scss` and add `@use '@carbon/react'` to load all component styles. Build a `TutorialHeader` component using `Header`, `HeaderContainer`, `HeaderName`, `HeaderNavigation`, and `SideNav` from `@carbon/react`. Wrap pages in a `providers.js` using the `<Theme theme="g100">` component with `<Content>` children. Use Next.js `Link` instead of anchor tags to prevent full page reloads. File-based routing creates pages automatically — no separate router needed.
- **Relevance**: Step-by-step walkthrough of the full initial setup including UI Shell navigation, theming wrapper, and project file structure.

### React Tutorial Step 2 — Grid and Component Usage

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/developing/react-tutorial/step-2.mdx
- **Summary**: Use `<Grid>` and `<Column>` for responsive layouts. Column spans are set per breakpoint with `sm`, `md`, `lg` props: `<Column lg={16} md={8} sm={4}>`. Offsets use object syntax: `<Column lg={{ span: 8, offset: 7 }}>`. Import multiple components from `@carbon/react` in one line: `import { Breadcrumb, BreadcrumbItem, Button, Tabs, Tab, TabList, TabPanels, TabPanel, Grid, Column } from '@carbon/react'`. Use unique `aria-label` attributes when multiple `<nav>` elements render on the same page. Style with Carbon's Sass tokens: `@use '@carbon/react/scss/spacing' as *`, `@use '@carbon/react/scss/type' as *`, `@use '@carbon/react/scss/theme' as *`.
- **Relevance**: Demonstrates the practical code patterns for building real pages with Carbon — grid usage, multi-component imports, and Sass token integration.

---

## 5. Best Practices

### Theming and Customization

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/themes/overview.mdx
- **Summary**: Carbon's theming system works by modifying tokens — change a token once and it propagates across all components using that token. Four built-in themes: White (default), Gray 10, Gray 90, Gray 100. Switch default via Sass: `@use '@carbon/react/scss/theme' with ($theme: themes.$g100)`. Create custom themes by overriding specific tokens or defining new ones: `@use '@carbon/react/scss/theme' with ($theme: (background: #e2e2e2, custom-token-01: #000000))`. Four token categories: Color, Spacing, Typography, and Global. Tokens nest internally (e.g., `$interactive` references `$blue-60`). Full token lists available in the `@carbon/themes` package.
- **Relevance**: Theming is the correct way to customize Carbon — overriding tokens preserves the system's coherence and upgrade safety, while direct CSS overrides break both.

### Content Writing Best Practices

- **Source**: https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/guidelines/content/overview.mdx
- **Summary**: IBM content voice is clear, logical, data-driven, and direct without boasting — "persuasive, not poetic." Tone adapts to context while voice stays consistent (e.g., error messages are economical and phrase-based; onboarding flows use warmer full sentences). Words function as a conversation between product and user, working alongside visuals. Good labels empower users; bad labels create friction. Accessibility in writing means providing text alternatives for visual content, clear error messages, and properly labeled form inputs.
- **Relevance**: UI text is part of the design system — using Carbon's voice guidelines ensures labels, error messages, and help text feel consistent with the visual components.

---

## Articles to Ingest

URLs ready for `/kb-scrapecontent` → `/kb-ingest`:

- https://github.com/carbon-design-system/carbon
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/all-about-carbon/what-is-carbon.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon/main/packages/react/README.md
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/color/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/typography/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/spacing/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/motion/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/2x-grid/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/elements/themes/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/guidelines/accessibility/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/guidelines/content/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/developing/get-started.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/developing/react-tutorial/overview.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/developing/react-tutorial/step-1.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/developing/react-tutorial/step-2.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/button/usage.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/modal/usage.mdx
- https://raw.githubusercontent.com/carbon-design-system/carbon-website/main/src/pages/components/data-table/usage.mdx

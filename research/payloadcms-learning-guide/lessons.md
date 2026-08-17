# Lesson Plan: PayloadCMS — Learning Guide & UI Customization

*Source: `research/payloadcms-learning-guide/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations
*Establish what Payload is, why it exists, and how to get a working project running before building anything.*

### Lesson 1: What Is PayloadCMS?
**File:** `lessons/0001-what-is-payloadcms.html`
**Key concepts:** headless CMS · code-first config · Next.js fullstack framework · self-hosting
**Source:** https://payloadcms.com/docs/getting-started/what-is-payload — Payload is a TypeScript-first CMS/backend that auto-generates REST, GraphQL, and Admin UI from a single config file
**Skill:** Draw a diagram (on paper or in text) showing how `payload.config.ts` generates the Admin UI, REST API, and GraphQL API — then write one sentence explaining why code-first config is different from GUI-based CMS tools
**Reference doc:** `reference/payload-architecture.html`

### Lesson 2: Payload 2.0 — What Changed and Why It Matters
**File:** `lessons/0002-payload-2-modern-features.html`
**Key concepts:** adapter pattern · Drizzle ORM · Lexical editor · database migrations · live preview
**Source:** https://payloadcms.com/blog/payload-2-0 — Payload 2.0 introduced Postgres support via Drizzle, Lexical rich text editor, first-class TypeScript migrations, transaction support, and live preview
**Skill:** List the three Payload 2.0 features you would use first in a real project and write one sentence explaining why each one matters to you
**Reference doc:** `reference/payload-2-changelog.html`

### Lesson 3: Installation & Project Setup
**File:** `lessons/0003-installation-setup.html`
**Key concepts:** create-payload-app · withPayload · payload.config.ts · database adapter · path alias
**Source:** https://payloadcms.com/docs/getting-started/installation — Scaffold with `npx create-payload-app` or manually integrate into an existing Next.js app; requires Node 20.9+, a database adapter, and `@payload-config` tsconfig alias
**Skill:** Write out (from memory) the five manual installation steps in order: what packages to install, what directory to add, what to do in `next.config.js`, what file to create at the root, and what to add to `tsconfig.json`
**Reference doc:** `reference/payload-architecture.html` *(extend)*

---

## Module 2 — Core Building Blocks
*Learn the four primitives that make up any Payload application: collections, fields, globals, and hooks.*

### Lesson 4: Collections — Modeling Repeatable Content
**File:** `lessons/0004-collections.html`
**Key concepts:** slug · fields · access control · versions/drafts · useAsTitle · defaultColumns · listSearchableFields
**Source:** https://payloadcms.com/docs/configuration/collections — Collections group related documents with a shared schema; require `slug` and `fields`; support access, hooks, auth, versions, upload, and orderable
**Skill:** Write a `CollectionConfig` object for a `products` collection with at least 4 fields (name, price, description, status), `useAsTitle` set to the name field, and draft versioning enabled
**Reference doc:** `reference/collection-field-reference.html`

### Lesson 5: Fields — Building Your Content Schema
**File:** `lessons/0005-fields.html`
**Key concepts:** data fields · presentational fields · virtual fields · admin.condition · validate · admin.components
**Source:** https://payloadcms.com/docs/fields/overview — 20+ field types across three categories: data (text, number, relationship, array, blocks…), presentational (row, collapsible, UI), and virtual (join, `virtual: true`)
**Skill:** Given a blog post schema requirement (title, author relationship, tags array, hero image upload, publish date, rich text body), write the fields array using the correct field types for each
**Reference doc:** `reference/collection-field-reference.html` *(extend)*

### Lesson 6: Globals — Singletons and App-wide Settings
**File:** `lessons/0006-globals.html`
**Key concepts:** singleton · GlobalConfig · globals vs collections · site-wide settings · versioning globals
**Source:** https://payloadcms.com/docs/configuration/globals — Globals are single-document configs ideal for navigation, banners, and app settings; the rule of thumb is: if you need exactly one instance, use a Global
**Skill:** Decide (and justify in writing) whether each of these should be a Collection or a Global: site navigation, team members, FAQ items, privacy policy text, homepage hero banner
**Reference doc:** `reference/collection-field-reference.html` *(extend)*

### Lesson 7: Hooks — Server-side Lifecycle Logic
**File:** `lessons/0007-hooks.html`
**Key concepts:** beforeChange · afterChange · beforeRead · afterRead · hook context · fire-and-forget · jobs queue
**Source:** https://payloadcms.com/docs/hooks/overview — Hooks run server-side at lifecycle points; async hooks block execution, void hooks fire-and-forget; best practices: avoid expensive logic in read hooks, use hook context to prevent infinite loops
**Skill:** Write a `beforeChange` hook for a `posts` collection that automatically sets `publishedAt` to the current date when `status` changes from `draft` to `published`
**Reference doc:** `reference/hooks-reference.html`

---

## Module 3 — Admin UI Customization
*Learn how to reshape the admin panel — from a simple color change to replacing entire views with custom React components.*

### Lesson 8: Admin Panel Theming — CSS and Dark/Light Mode
**File:** `lessons/0008-admin-theming.html`
**Key concepts:** custom.scss · CSS custom properties · admin.theme · light/dark mode · internationalization · toast config
**Source:** https://payloadcms.com/docs/admin/overview — Admin UI customized via `custom.scss` for CSS overrides, `admin.theme` to lock mode, `admin.views` for page replacements, `admin.routes` for URL customization; 30+ languages supported
**Skill:** Write a `custom.scss` snippet that changes the admin panel's background to a dark navy, text to near-white, and accent to teal — use CSS custom property names from the lesson
**Reference doc:** `reference/admin-customization-reference.html`

### Lesson 9: Component Overrides — Replacing Admin UI Pieces
**File:** `lessons/0009-component-overrides.html`
**Key concepts:** admin.components · component path syntax · hash export · server components · client components · clientProps · serverProps
**Source:** https://payloadcms.com/docs/admin/components — Components registered via file paths (not imports); four categories: root, collection, global, field; Server Components by default, Client Components with `'use client'`; both receive `payload` and `i18n` props
**Skill:** Write the `admin.components` config entry to replace the logout button with a custom component at `/src/components/MyLogout` using a named export `MyLogoutButton`
**Reference doc:** `reference/admin-customization-reference.html` *(extend)*

### Lesson 10: Custom Field Components
**File:** `lessons/0010-custom-field-components.html`
**Key concepts:** admin.components.Field · useField hook · 'use client' · custom input UI · ColorPicker pattern
**Source:** https://payloadcms.com/docs/admin/components — Field components override how a field is rendered in the admin; use `useField` from `@payloadcms/ui` to read and write the field value; component path registered in the field's `admin.components.Field`
**Skill:** Sketch (in code or pseudocode) a custom field component for a `rating` field that renders 5 clickable stars instead of a number input — include the field definition and the React component structure
**Reference doc:** `reference/admin-customization-reference.html` *(extend)*

---

## Module 4 — Industry Assessment & Decision-Making
*Zoom out and evaluate Payload against the landscape so you can pick the right tool with confidence.*

### Lesson 11: Payload vs. The Competition
**File:** `lessons/0011-payload-vs-competition.html`
**Key concepts:** headless CMS landscape · WordPress · Contentful · Sanity · Strapi · Directus · vendor lock-in · self-hosting
**Source:** https://payloadcms.com/compare — Payload compares directly against WordPress, Contentful, Sanity, Strapi, and Directus; key differentiators are code-first config, self-hosting/data ownership, and deep Next.js integration; enterprise customers include Microsoft, ASICS, Blue Origin
**Skill:** Fill in a comparison table (from memory) for Payload, Contentful, and Strapi across these dimensions: pricing model, hosting options, TypeScript support, admin customizability, and learning curve
**Reference doc:** `reference/cms-landscape.html`

### Lesson 12: When to Choose Payload — and When Not To
**File:** `lessons/0012-when-to-choose-payload.html`
**Key concepts:** trade-offs · Next.js dependency · Figma acquisition · ecosystem maturity · decision criteria
**Source:** https://payloadcms.com/compare — Payload's trade-offs include Next.js lock-in, a newer plugin ecosystem, complexity of deep UI theming, and uncertainty post-Figma acquisition; ideal when you need full ownership, TypeScript DX, and CMS+backend in one repo
**Skill:** Write a one-paragraph recommendation (for or against Payload) for a hypothetical project: a marketing site for a startup that needs a blog, landing pages, and a team directory — justify your reasoning using specific trade-offs from the lesson
**Reference doc:** `reference/cms-landscape.html` *(extend)*

---

## Suggested Teaching Order

Follow modules 1 → 2 → 3 → 4 in sequence. Module 1 establishes mental models needed to understand Module 2's field types and hooks. Module 3 depends on understanding collections and fields (you can't customize a collection's admin view before knowing what a collection is). Module 4 stands alone and can be read any time, but is most valuable after you've built something, when the trade-offs feel concrete.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/payload-architecture.html` | Architecture diagram, config file anatomy, API surface overview |
| `reference/payload-2-changelog.html` | Payload 2.0 feature list with before/after comparisons |
| `reference/collection-field-reference.html` | All field types with signatures, options, and code examples |
| `reference/hooks-reference.html` | All hook types, execution model, best practices cheat sheet |
| `reference/admin-customization-reference.html` | Component path syntax, override categories, SCSS custom properties list |
| `reference/cms-landscape.html` | Side-by-side CMS comparison table across 6 dimensions |

# How to Write a CLAUDE.md That Actually Works

Source: https://fordelstudios.com/research/how-to-write-project-context-files-for-ai-coding-assistants
Author: Abhishek Sharma | Fordel Studios | March 31, 2026

---

## What Is a Project Context File?

A project context file (CLAUDE.md, .cursorrules, .github/copilot-instructions.md) loads automatically into your AI coding assistant each session. Without one, assistants default to training data — producing valid but convention-mismatched code.

---

## What to Include

Only document **what the assistant would get wrong without guidance**. Focus on:

- Framework versions and key libraries
- Non-default naming conventions
- File/folder structure patterns
- Testing libraries and approach
- Git workflow and commit format
- Custom error handling patterns
- Banned patterns and deprecated APIs

---

## Recommended Structure (5 Sections)

### 1. Project Identity (3–5 lines)
State the project name, core stack, and what's explicitly *not* used. Example: "Next.js 15 App Router, TypeScript strict, Tailwind v4 — no Pages Router, no getServerSideProps."

### 2. Conventions That Break Defaults
Be specific with examples:
- ❌ "Follow our coding standards"
- ✅ "Named exports only, no default exports; server components in `app/`, client components in `src/components/`"

### 3. The "Do NOT" List
Explicitly ban unwanted patterns: no `console.log`, no CSS-in-JS, no new dependencies without asking.

### 4. File Structure Map
A brief indented directory list showing where things live — helps the assistant place new files correctly.

### 5. Testing & Quality Gates
Specify test libraries, file locations, and CI requirements (e.g., "Vitest, not Jest; test files alongside source").

---

## Multi-File Context (Claude Code)

Nest CLAUDE.md files in subdirectories for domain-specific rules:

```
CLAUDE.md              ← global stack + git workflow
src/components/CLAUDE.md  ← design system, a11y
src/lib/CLAUDE.md         ← error handling, logging
```

Keep root files under **200 lines**; subdirectory files under **50 lines**.

---

## Common Mistakes

| Mistake | Fix |
|---|---|
| Writing an essay | Only include what causes real errors |
| Being vague | Give actionable examples with file paths |
| Never updating | Review during sprint retros |
| Duplicating enforced rules | Skip what ESLint/tsconfig already handles |
| Omitting negatives | Explicitly ban patterns the AI gravitates toward |

---

## Measuring Success

Track weekly correction frequency. Fordel reported dropping from **15–20 corrections/week to 2–3** after iterating their CLAUDE.md over three weeks.

> "Every correction you give your AI assistant that you do not encode into a context file is a correction you will give again tomorrow."

**Workflow:** Each time you correct the assistant, decide if a rule would prevent recurrence — if yes, add it immediately.

---

## Key Takeaways

- Invest ~30 minutes initially; ~2 minutes/week to maintain
- Treat CLAUDE.md as a **first-class project artifact**: code-reviewed, version-controlled, updated alongside convention changes
- Start with five rules based on your last five corrections — ship today, iterate weekly

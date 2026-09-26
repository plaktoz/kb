---
type: literature-note
source_url: https://github.com/typesafe-ai/typesafe-sdk-js
author: Unknown
tags: [jev, javascript, typescript, sdk]
date_consumed: 2026-09-26
---

## Summary

The TypeSafe JavaScript/TypeScript SDK (`@typesafe-ai/sdk`) provides a `TypeSafeClient` with `choice()`, `score()`, and `noul()` helper functions for building typed Jev queries in Node.js ≥ 20. Answer types are automatically inferred from the question definitions — no manual type assertions needed. The package ships with ESM, CommonJS, and TypeScript declarations.

## Core Concepts

- **`TypeSafeClient`** — main client class; instantiate once and call `await client.systemOne({...})` (camelCase in JS vs snake_case in Python)
- **`choice(prompt, criteria)`** — helper function for categorical questions; `criteria` is an object with option keys mapping to `null`
- **`score(prompt, options)`** — helper for rating questions; `options` includes `min`/`max` bounds
- **`noul(prompt)`** — helper for yes/no questions; no criteria needed
- **Answer inference** — TypeScript automatically infers the answer type from your question definition; `response.answers.category.choice` is typed as one of your criteria keys
- **Module formats** — ships as ESM, CommonJS, and `.d.ts` TypeScript declarations; works in all Node.js module systems

## Key Takeaways

- **Install**: `npm install @typesafe-ai/sdk` (Node.js ≥ 20 required)
- **Auth**: `TYPESAFE_API_KEY` environment variable
- **API is async**: all calls use `await`; works in async functions and top-level ESM
- **Type inference**: define questions once, TypeScript infers answer types automatically
- **Same mental model as Python**: `state` + `questions` map; different syntax, identical semantics

```typescript
import { choice, score, noul, TypeSafeClient } from "@typesafe-ai/sdk";

const client = new TypeSafeClient();
const response = await client.systemOne({
  state: { document: "I was charged twice. Please fix this ASAP." },
  questions: {
    category: choice("What is this ticket about?", {
      billing: null,
      technical: null,
      other: null,
    }),
  },
});

// TypeScript knows response.answers.category.choice is "billing" | "technical" | "other"
console.log(response.answers.category.choice);
```

## 🃏 Review Questions

**Q1**: What Node.js version is required and what module formats does the SDK support?
**A**: Node.js ≥ 20; the package ships with ESM, CommonJS, and TypeScript type declarations to support all module systems.

**Q2**: How does TypeScript type inference work with Jev questions in this SDK?
**A**: Answer types are inferred automatically from your question definitions at compile time — if you define a `choice()` with `billing`, `technical`, and `other` options, TypeScript knows the answer will be one of those three strings without manual type assertions.

**Q3**: What is the key syntactic difference between the Python and JavaScript SDKs?
**A**: The method is `client.systemOne()` (camelCase) in JS vs `client.system_one()` (snake_case) in Python; helper functions replace constructor classes (`choice()` vs `Choice()`); both accept the same `state` + `questions` structure.

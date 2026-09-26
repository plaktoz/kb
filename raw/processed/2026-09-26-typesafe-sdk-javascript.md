---
source_url: https://github.com/typesafe-ai/typesafe-sdk-js
author: Unknown
date: 2026-09-26
---

# TypeSafe AI JavaScript SDK

## Description

JavaScript and TypeScript SDK for the TypeSafe AI platform.

## Installation

Requires Node.js 20 or newer:

```bash
npm install @typesafe-ai/sdk
```

## Authentication

Set your API key as an environment variable:

```
TYPESAFE_API_KEY=your_key_here
```

## Basic Usage

```typescript
import { choice, TypeSafeClient } from "@typesafe-ai/sdk";

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

console.log(response.answers.category.choice);
```

## Key Features

- Answer types are **inferred from your questions** automatically
- Package ships with **ESM, CommonJS, and TypeScript declarations**
- Core API surface lives in `src/client.ts` and `src/types.ts`

## Further Reading

- Full docs: [docs.typesafe.ai](https://docs.typesafe.ai/)
- License: MIT

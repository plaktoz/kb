# Lesson Plan: Learning TypeScript

*Source: `research/learning-typescript/report.md`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module 1 — Foundations: Rebuilding Your Mental Model
*Addresses the Java assumptions that break first and establishes the correct TypeScript worldview before any syntax.*

### Lesson 1: What TypeScript Actually Is
**File:** `lessons/0001-what-typescript-is.html`
**Key concepts:** compile-time tool · superset of JavaScript · type erasure · tsc compiler
**Source paper:** https://www.typescriptlang.org/docs/handbook/intro.html — TypeScript is a static typechecker; types are erased at runtime; all valid JS is valid TS
**Skill:** Write a small `.ts` file with a typed function, compile it with `tsc`, and open the output `.js` to observe that types are gone — confirming type erasure firsthand.
**Reference doc:** `reference/typescript-basics.html`

### Lesson 2: Structural Typing — The Java Instinct to Unlearn
**File:** `lessons/0002-structural-typing.html`
**Key concepts:** structural vs nominal typing · shape compatibility · types as sets · runtime erasure
**Source paper:** https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes-oop.html — structural typing means shape wins, not name; identical-shaped classes are interchangeable; empty types accept everything
**Skill:** Write two unrelated classes with identical shapes and assign one to a variable typed as the other — verify that TypeScript accepts it, then write a comment explaining why Java would reject this.
**Reference doc:** `reference/structural-typing.html`

### Lesson 3: Your First TypeScript Project
**File:** `lessons/0003-first-project-setup.html`
**Key concepts:** npm install · tsc CLI · tsconfig.json · strict mode · outDir / rootDir
**Source paper:** https://www.typescriptlang.org/docs/handbook/typescript-tooling-in-5-minutes.html + https://www.typescriptlang.org/tsconfig — install TS, write src/, compile to dist/, always start with strict: true
**Skill:** Scaffold a minimal TypeScript project from scratch: create `src/index.ts`, write a `tsconfig.json` with `strict: true`, compile and inspect `dist/index.js`.
**Reference doc:** *(extend reference/typescript-basics.html)*

---

## Module 2 — The Type System
*Builds the type system vocabulary layer by layer, using Java comparisons throughout.*

### Lesson 4: Everyday Types
**File:** `lessons/0004-everyday-types.html`
**Key concepts:** string/number/boolean · arrays · union types · interface vs type alias · optional properties · null handling
**Source paper:** https://www.typescriptlang.org/docs/handbook/2/everyday-types.html — primitives are lowercase; no int/float split; interface merges, type does not; strictNullChecks enforces null handling
**Skill:** Annotate five function signatures with correct TypeScript types (primitives, arrays, union, optional param), fix any implicit-any errors that appear.
**Reference doc:** `reference/type-vocabulary.html`

### Lesson 5: Classes in TypeScript
**File:** `lessons/0005-classes.html`
**Key concepts:** access modifiers · readonly vs final · private vs #field · implements gotcha · structural class comparison · parameter properties
**Source paper:** https://www.typescriptlang.org/docs/handbook/2/classes.html — TypeScript private is compile-time only; implements does not infer types; classes match structurally
**Skill:** Take a Java-style class (with private fields and an interface implementation), port it to TypeScript, then list three things that would silently differ from the Java version.
**Reference doc:** `reference/classes-java-comparison.html`

### Lesson 6: Generics
**File:** `lessons/0006-generics.html`
**Key concepts:** type variables · extends constraints · keyof · type inference · default type parameters · variance annotations
**Source paper:** https://www.typescriptlang.org/docs/handbook/2/generics.html — same <T> syntax as Java; inference is heavy; keyof has no Java equivalent; generics erased at runtime like Java
**Skill:** Write a generic `getProperty<T, K extends keyof T>(obj: T, key: K)` function and call it with both a valid and an invalid key to see the compile error in action.
**Reference doc:** *(extend reference/type-vocabulary.html)*

### Lesson 7: Narrowing and Discriminated Unions
**File:** `lessons/0007-narrowing.html`
**Key concepts:** typeof guards · instanceof · in operator · discriminated unions · never exhaustiveness · user-defined type predicates
**Source paper:** https://www.typescriptlang.org/docs/handbook/2/narrowing.html — control-flow narrows types; discriminated unions replace instanceof chains; never enforces exhaustiveness
**Skill:** Build a `Shape` discriminated union with `Circle` and `Square`, write an `getArea` function with exhaustive `switch`, then add a `Triangle` type and observe the compile error at the `never` check.
**Reference doc:** `reference/narrowing-patterns.html`

---

## Module 3 — Advanced Type Patterns
*The techniques that make TypeScript uniquely powerful beyond Java generics.*

### Lesson 8: Function Types and Overloads
**File:** `lessons/0008-function-types.html`
**Key concepts:** call signatures · overloads vs union types · void vs undefined · rest parameters · destructuring types
**Source paper:** https://www.typescriptlang.org/docs/handbook/2/functions.html — implementation signature is invisible; prefer unions over overloads; void ≠ undefined; over-constraining generics is a common mistake
**Skill:** Rewrite a function that uses overloads with a union type instead, and write a `() => void` callback to demonstrate that TypeScript allows it to return a value without error.
**Reference doc:** *(extend reference/type-vocabulary.html)*

### Lesson 9: Types from Types
**File:** `lessons/0009-types-from-types.html`
**Key concepts:** mapped types · conditional types · template literal types · infer keyword · Partial / Readonly / ReturnType / Awaited
**Source paper:** https://www.typescriptlang.org/docs/handbook/2/types-from-types.html — [K in keyof T] iterates properties; T extends U ? X : Y branches types; infer extracts type variables in conditionals
**Skill:** Implement `MyPartial<T>` (makes all properties optional) and `MyReturnType<T>` (extracts the return type of a function) using only mapped/conditional types — no built-ins allowed.
**Reference doc:** `reference/advanced-types.html`

---

## Module 4 — Real-World TypeScript
*Apply the knowledge to actual projects and nail the common failure modes.*

### Lesson 10: TypeScript with React
**File:** `lessons/0010-react-typescript.html`
**Key concepts:** JSX typing · props interfaces · useState generics · event types · React.ReactNode · generic components
**Source paper:** https://www.typescriptlang.org/docs/handbook/react.html — TypeScript supports JSX natively; type useState<User | null> explicitly; use React.ChangeEvent<HTMLInputElement> for event handlers
**Skill:** Write a typed `<SearchInput>` React component with an `onChange` prop typed as `React.ChangeEvent<HTMLInputElement>` and a `results` prop typed as `Array<{ id: number; title: string }>`.
**Reference doc:** `reference/react-patterns.html`

### Lesson 11: TypeScript 5.x Ecosystem
**File:** `lessons/0011-typescript-5x.html`
**Key concepts:** standard decorators · const type parameters · moduleResolution bundler · verbatimModuleSyntax · union enums
**Source paper:** https://www.typescriptlang.org/docs/handbook/release-notes/typescript-5-0.html — decorators are now stable; const modifier on type params avoids as const; bundler resolution for Vite projects
**Skill:** Update an existing tsconfig snippet to use `moduleResolution: "bundler"` and `verbatimModuleSyntax: true`, and explain in one paragraph what each option changes about how imports are handled.
**Reference doc:** *(extend reference/typescript-basics.html)*

### Lesson 12: Do's, Don'ts, and Java Developer Pitfalls
**File:** `lessons/0012-common-mistakes.html`
**Key concepts:** any vs unknown · String vs string · callback void · overload ordering · structural pitfalls · private erasure · implements gotcha
**Source paper:** https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html + report Java pitfalls table — capitalized primitives; any disables checking; overloads must be specific-first; implements does not infer
**Skill:** Review a deliberately broken TypeScript snippet with 5 hidden mistakes (capitalized types, any overuse, wrong overload order, optional callback params, relying on implements to infer), find and fix all five.
**Reference doc:** *(extend reference/classes-java-comparison.html)*

### Lesson 13: Practice Path — From Here to Fluency
**File:** `lessons/0013-practice-path.html`
**Key concepts:** type-challenges tiers · Pretty TypeScript Errors · error code categories · reading real codebases · next steps
**Source paper:** https://github.com/type-challenges/type-challenges/blob/main/README.md + https://typescript.tv/errors/ — Easy tier covers Pick/Readonly/Exclude/Awaited; semantic 2xxx errors are most common; Pretty TS Errors extension translates messages
**Skill:** Solve the `Pick<T, K>` type-challenge (Easy tier) from scratch without using the built-in — implement it using `[K in keyof T]` mapped type syntax.
**Reference doc:** `reference/practice-resources.html`

---

## Suggested Teaching Order

Modules 1 → 2 → 3 → 4. Module 1 must come first — Java developers who skip the mental model reset will misapply Module 2 concepts. Module 3 can be revisited after real project work in Module 4; Lessons 9 and 11 are safe to defer until you hit a library that uses those patterns.

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/typescript-basics.html` | What TypeScript is, tsc CLI, tsconfig starter config, type erasure summary |
| `reference/structural-typing.html` | Structural vs nominal typing, types-as-sets model, common surprises |
| `reference/type-vocabulary.html` | Primitive types, interface vs type alias, union/intersection, generics cheatsheet |
| `reference/classes-java-comparison.html` | Side-by-side Java/TS class features, access modifier differences, implements gotcha |
| `reference/narrowing-patterns.html` | typeof/instanceof/in/discriminated union/never patterns with code |
| `reference/advanced-types.html` | Mapped types, conditional types, template literals, infer — with worked examples |
| `reference/react-patterns.html` | Props typing, hook typing, event types, generic component patterns |
| `reference/practice-resources.html` | type-challenges link + Easy tier list, Pretty TS Errors, error code categories |

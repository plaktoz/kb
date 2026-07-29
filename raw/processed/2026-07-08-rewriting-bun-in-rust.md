# Rewriting Bun in Rust

source_url: https://bun.com/blog/bun-in-rust

---

By Jarred Sumner, July 8, 2026. Disclosure: Bun was acquired by Anthropic in December 2025; the author and others on the Bun team work at Anthropic, and a pre-release version of Claude Fable 5 was used for much of the Rust rewrite.

Bun started as a line-for-line port of esbuild's JavaScript & TypeScript transpiler from Go to Zig, first written in one year in Zig, pre-LLM. Bun's CLI now gets over 22 million monthly downloads, and tools like Claude Code and OpenCode use Bun as their runtime. Bun's ambitious scope — transpiler, bundler, npm-compatible package manager, test runner, HTTP/WebSocket client, Node.js API implementations — has also been a challenge for stability, with recurring classes of bugs: use-after-free and double-free crashes, memory leaks, and out-of-bounds reads, mostly stemming from manually managing memory lifetimes in Zig alongside JavaScriptCore's garbage collector.

## Why Rust

Zig doesn't manage memory automatically; most cleanup is written explicitly at each call site with `defer`. Bun's team had already added Address Sanitizer support, ReleaseSafe builds on Windows, 24/7 fuzzing with Fuzzilli, and extensive memory-leak tests — more than many projects do — but a large share of remaining bugs were use-after-free, double-free, and "forgot to free" errors in error paths. In safe Rust, these become compiler errors caught before code ships, backed by RAII-style automatic cleanup via `Drop`. Historically, rewrites are considered a bad idea: excluding comments, Bun is 535,496 lines of Zig, and a rewrite by a small human team would take about a year, freezing feature and bugfix work for that period — not a realistic option. So the team tested whether a new Anthropic model could rewrite Bun in Rust instead.

## The approach

The rewrite used roughly 50 dynamic Claude Code workflows run continuously over 11 days, each structured as a loop: an implementer proposes code, two or more adversarial reviewers (separate Claude context windows, told to assume the code is wrong and to find bugs) review it, and a fixer applies the feedback. The implementer's context includes the original Zig code, the port plan, and its own reasoning; the adversarial reviewer sees only the diff. This "split context window" approach mirrors human code review, where the person merging code has different incentives than the person trying to find its flaws.

Before writing code, about three hours were spent with Claude mapping Zig patterns to Rust patterns, producing a `PORTING.md` document. A separate workflow analyzed proper Rust lifetimes for every struct field across the codebase, producing a `LIFETIMES.tsv`, followed by adversarial review of both documents. A trial run on just 3 files preceded scaling to all 1,448 `.zig` files. Early runs hit git conflicts when multiple Claude instances stepped on each other (running `git stash`, `git reset --hard`); the workflow was edited to forbid destructive git and cargo commands mid-loop, and the work was split into 4 worktrees with 16 Claude instances each (64 total).

At peak, Claude wrote about 1,300 lines of code per minute, each line reviewed by two adversarial reviewers before committing — none of it worked yet at that point. After the initial port, a separate workflow fixed roughly 16,000 compiler errors crate-by-crate across 64 parallel Claude instances, followed by workflows to get the CLI to run, then to get the full test suite (over 60,000 tests across three platforms) passing locally and then in CI. The whole effort took 11 days and 6,778 commits, with zero tests skipped or deleted, at a cost of roughly $165,000 in API pricing (5.9 billion uncached input tokens, 690 million output tokens, 72 billion cached input token reads) — versus an estimated 3 engineers working a full year by hand.

## Adversarial review catching real bugs

Three examples of bugs the adversarial reviewers caught before merge: an async `uv_close` pattern where a `Box` was dropped before libuv finished using the pointer, causing use-after-free then double-free (fixed by leaking the box before the async close); a `trunc()`-based time conversion that produced an invalid negative nanosecond value for pre-1970 timestamps (fixed by switching to `floor()`); and an eagerly-evaluated `unwrap_or` in CSS `color-mix()` parsing that panicked even when its fallback branch wasn't needed (fixed by switching to the lazy `unwrap_or_else`).

## Results

Bun v1.4.0 fixes 128 bugs that reproduce in v1.3.14, the last Zig-based release. Rust's `Drop` trait fixed several memory leaks — for example, every `Bun.build()` call in v1.3.14 leaked about 3 MB forever, causing tools like dev servers to eventually run out of memory; in v1.4.0 memory levels off. Combined with ICU changes and identical code folding, binary size shrank about 20% on Linux and Windows. Recursive-descent parsers now use less stack space thanks to LLVM's `lifetime.start`/`lifetime.end` intrinsics. Cross-language link-time optimization between C/C++ and Rust enabled inlining across language boundaries, contributing to a measured 2-5% throughput and build-time improvement across HTTP benchmarks and common CLI workloads (next build, vite build, tsc).

The rewrite introduced 19 known regressions, all since fixed, most stemming from code that looked syntactically identical between Zig and Rust but behaved differently — for example Zig's `assert()` running its argument in every build versus Rust's `debug_assert!` macro being erased entirely in release builds, silently dropping a side-effecting call needed for hot module reloading.

Prisma launched its "Prisma Compute" public beta on Bun's Rust rewrite after testing it against memory leaks and connection-pool recovery failures that had affected the Zig version. Claude Code itself has shipped on the Rust port of Bun since mid-June, with 10% faster startup on Linux.

Bun v1.3.14 was the last version of Bun written in Zig; Bun v1.4.0, available now via `bun upgrade --canary`, is the first written in Rust. About 4% of Bun's Rust code sits inside `unsafe` blocks, mostly single-line calls into C/C++ libraries like JavaScriptCore, which the team expects to continue using going forward.

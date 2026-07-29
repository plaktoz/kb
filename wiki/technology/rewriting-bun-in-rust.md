---
type: literature-note
source_url: https://bun.com/blog/bun-in-rust
author: Jarred Sumner
tags: [bun, rust, ai-assisted-engineering, software-rewrites, claude-code]
date_consumed: 2026-07-29
---

## Summary

The [[Bun]] team rewrote its entire 535,000-line JavaScript runtime from Zig to Rust in 11 days using roughly 64 parallel Claude Code instances organized into implementer/adversarial-reviewer loops, at an API cost of about $165,000 versus an estimated year of work for three human engineers. The rewrite targeted [[Rust]]'s compile-time memory safety (via `Drop` and the borrow checker) to systematically eliminate the use-after-free and memory-leak bugs that had plagued Zig's manual memory management, shipping as Bun v1.4.0 with zero tests skipped and 128 known bugs fixed.

## Core Concepts

- **[[Adversarial Code Review]]** — pairing an implementer Claude (with full context: original code, port plan, reasoning) against separate reviewer Claude instances that see only the diff and are told to assume it's wrong, mirroring how human code review works best when the reviewer isn't the same person trying to ship the change
- **[[Dynamic Workflows]]** — Claude Code loops (`task → result → review → apply`) run continuously and edited mid-flight when they misbehave, rather than one-shot prompting
- **[[Mechanical Porting]]** — translating code file-by-file to preserve architecture and behavior first, deferring idiomatic refactoring to a later phase, rather than attempting a "clean rewrite" all at once
- **[[Compiler Errors as a Work Queue]]** — treating ~16,000 Rust compiler errors as a literal task list divisible across dozens of parallel agents, grouped by crate

## Key Takeaways

- **Scale of automation**: ~64 Claude instances running in parallel across 4 worktrees, peaking at 1,300 lines of code written per minute
- **Adversarial review caught real bugs**: including a use-after-free from an async `uv_close` pattern, an invalid negative-nanosecond timespec from using `trunc()` instead of `floor()`, and a panic from eager evaluation in `unwrap_or`
- **Results**: ~20% smaller binaries, memory leaks eliminated (an unbounded ~3MB-per-build leak in `Bun.build()` became flat), and 2-5% faster throughput via cross-language LTO between Rust and C/C++
- **Not risk-free**: the rewrite introduced 19 regressions, mostly from Zig and Rust constructs that look identical but behave differently (e.g., Zig's `assert()` always runs its argument; Rust's `debug_assert!` is erased entirely in release builds)
- **Production validation**: Prisma's Compute beta and Claude Code itself both moved onto the Rust-based Bun after testing it against prior failure modes

## 🧠 First Principles & Mental Models

- **[[Compiler as Feedback Loop]]**: choosing Rust wasn't about developer taste — it was about converting a class of runtime bugs (use-after-free, double-free, leaks) into compile-time errors, moving the feedback loop as early as possible in the development cycle, which is a specific instance of the general principle that catching errors closer to their origin is exponentially cheaper than catching them in production.

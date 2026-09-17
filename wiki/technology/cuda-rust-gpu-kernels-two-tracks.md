---
type: literature-note
source_url: https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/
author: Sri Koundinyan, Melih Elibol, and Jonathan Bentz
tags: [cuda, rust, gpu-programming, nvidia]
date_consumed: 2026-09-17
---

## Summary

NVIDIA announced native GPU kernel programming in Rust via two open-source projects — [[cuda-oxide]] (SIMT track) and [[cutile-rs]] (Tile track) — closing the gap where Rust host code had to call out to other languages for kernels. Both projects leverage Rust's ownership and borrow-checker guarantees to enforce GPU memory-safety properties at compile time. They are early-stage and not production-ready, but cutile-rs already has external adoption in HuggingFace's Grout and mistral.rs.

## Core Concepts

- **[[CUDA Rust]]**: NVIDIA's initiative to bring native GPU kernel authoring to [[Rust]], mirroring the two existing [[CUDA]] programming models (SIMT and Tile).
- **[[SIMT (Single Instruction, Multiple Threads)]]**: The traditional GPU programming model where you describe what one thread does; thousands run in parallel. cuda-oxide implements this track.
- **[[Tile Programming Model]]**: A higher-level GPU model where you describe what one tile of data does; the compiler handles thread mapping and memory layout. cutile-rs implements this track.
- **[[cuda-oxide]]**: A custom `rustc` codegen backend routing `#[kernel]` functions through Rust MIR → Pliron IR → LLVM IR → PTX. Requires pinned nightly toolchain and LLVM; introduces `DisjointSlice<T>` and `#[launch_contract]` for compile-time safety.
- **[[cutile-rs]]**: A macro-based tile-level kernel library that embeds the kernel AST in the host binary and JIT-compiles via CUDA Tile IR. Targets stable Rust 1.89+; no custom LLVM required. Published on crates.io.
- **[[DisjointSlice]]**: A custom Rust type in cuda-oxide granting each GPU thread exclusive access to its own slice element, solving the problem that `&mut [f32]` cannot safely be shared across thousands of threads.
- **[[Rust Borrow Checker]]** applied to GPU: aliasing between input and output buffers is caught at the call site as a standard compile error in both tracks, preventing a whole class of GPU race conditions.

## Key Takeaways

- **Guidance**: NVIDIA recommends reaching for the Tile model first; drop to SIMT only when explicit thread/memory control is needed.
- **cuda-oxide safety**: `DisjointSlice<T>` enforces per-thread exclusivity; `#[launch_contract]` validates launch dimensions at call time.
- **cutile-rs safety**: Tensor partitioning + ownership transfer across the launch boundary prevents aliasing; execution is lazy until `.sync_on(&stream)`.
- **Toolchain gap**: cuda-oxide requires pinned nightly + LLVM (compute cap 8.0+, CUDA 12.x+); cutile-rs needs only stable Rust 1.89+ (CUDA 13.3).
- **External adoption**: cutile-rs is already used in HuggingFace's Grout inference engine and mistral.rs — a meaningful signal for an early-stage project.
- **Interoperability roadmap**: NVIDIA plans cross-language interop between CUDA Rust, CUDA C++, and CUDA Python so frontend choice is not a lock-in.
- **Research backing**: Related paper *Fearless Concurrency on the GPU* at arxiv.org/abs/2606.15991.

## 🧠 First Principles & Mental Models

- **[[Shifting Left]]**: By encoding GPU aliasing and out-of-bounds access as type-system constraints, both tracks move safety checks from runtime crashes to compile-time errors — the same "fail early, fail cheap" principle that motivates static typing in general.
- **[[Abstraction Ladder]]**: Tile sits at a higher rung (data-centric) while SIMT sits lower (thread-centric); NVIDIA's "reach for Tile first" guidance is an explicit recommendation to default to the highest abstraction that meets your needs and descend only when necessary.

## 🃏 Review Questions

**Q1**: What is the core problem CUDA Rust solves, and what are the two programming tracks it introduces?
**A**: CUDA Rust allows GPU kernels to be written directly in Rust rather than requiring a separate language for kernel code. It offers a SIMT track (cuda-oxide) for explicit thread-level control and a Tile track (cutile-rs) for a higher-level data-centric programming model.

**Q2**: How does cuda-oxide prevent a GPU thread from aliasing its input and output buffers?
**A**: It introduces the `DisjointSlice<T>` type, which grants each thread exclusive access to its own element; passing the same buffer as both input and output triggers a standard Rust borrow-checker error — "cannot borrow c_dev as mutable because it is also borrowed as immutable" — at the call site.

**Q3**: Which track is further along in adoption and what are the practical toolchain trade-offs between the two?
**A**: cutile-rs (Tile) is further along, already integrated into HuggingFace's Grout and mistral.rs; it requires only stable Rust 1.89+ and no custom LLVM, while cuda-oxide (SIMT) demands a pinned nightly toolchain and LLVM/clang, making cutile-rs significantly easier to adopt today.

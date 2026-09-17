---
source_url: https://developer.nvidia.com/blog/introducing-cuda-rust-two-tracks-for-writing-gpu-kernels/
author: Sri Koundinyan, Melih Elibol, and Jonathan Bentz
date: 2026-09-08
---

# Introducing CUDA Rust: Two Tracks for Writing GPU Kernels

NVIDIA announced native GPU kernel programming in Rust via two open-source projects, bridging a longstanding gap where kernels had to be written in other languages even when host code was Rust.

## The Two Tracks

CUDA Rust mirrors the two existing CUDA programming models:

**SIMT** (Single Instruction, Multiple Threads) — the traditional model where you describe what one thread does, then launch thousands. This maps to how CUDA C++ and numba-cuda work today.

**Tile** — a higher-level model where you describe what one *tile* of data does, and the compiler handles thread mapping and memory layout. Also available in C++ and Python frontends.

NVIDIA's guidance: "reach for Tile first," dropping to SIMT when explicit control over threads and memory is needed.

## Track 1: cuda-oxide (SIMT)

[cuda-oxide](https://github.com/NVlabs/cuda-oxide) is a custom `rustc` codegen backend that routes `#[kernel]` functions through Rust MIR, the Pliron IR framework, and LLVM IR down to PTX.

**Requirements:** Linux, compute capability 8.0+, CUDA 12.x+, clang/libclang, pinned nightly toolchain.

### Key Safety Mechanisms

The kernel signature for a vector addition takes `a: &[f32]`, `b: &[f32]` (shared readable slices) and `c: DisjointSlice<f32>` — a type that grants each thread exclusive access to its own element. This solves the fundamental problem that `&mut [f32]` can't be safely shared across thousands of threads.

- `thread::index_1d()` returns a typed index (not a bare integer)
- `c.get_mut(idx)` returns an `Option`, making out-of-bounds a handled branch rather than a memory error
- `#[launch_contract]` declares indexing dimensions and block size; `prepare_vecadd` validates the live `LaunchConfig1D` against it before launch

Passing the output buffer as its own input produces a compile error: `"cannot borrow c_dev as mutable because it is also borrowed as immutable"` — aliasing is caught at the call site.

## Track 2: cutile-rs (Tile)

[cutile-rs](https://github.com/NVlabs/cutile-rs) operates at the tile level. Each tile block runs the kernel body once as a single logical thread over a sub-tensor. The `#[cutile::module]` macro embeds the kernel's AST in the host binary and JIT-compiles through CUDA Tile IR on first launch.

**Requirements:** Compute capability 8.0+, CUDA 13.3, stable Rust 1.89+, Linux. No nightly toolchain, no custom LLVM.

Published on crates.io; already used in HuggingFace's Grout inference engine and mistral.rs.

### Key Design Points

- Kernel shapes use `-1` as a sentinel for dynamic dimensions resolved at launch
- `.partition([128])` on a mutable tensor grants each tile exclusive ownership of its 128-element chunk, fixes the grid, and supplies the const generic `B`
- The macro-generated launcher takes ownership of all tensors and returns them as a tuple when complete
- Nothing executes until `.sync_on(&stream)` — the entire pipeline is lazy and recorded

Aliasing is caught differently: attempting to pass the same tensor as both input and output produces `"use of moved value: z"` — ownership follows tensors across the launch boundary.

## Safety Comparison

| Aspect | cuda-oxide (SIMT) | cutile-rs (Tile) |
|--------|-------------------|------------------|
| Output exclusivity | `DisjointSlice<T>` type | Tensor partitioning + ownership |
| Aliasing check | Per launch call | Ownership across launch boundary |
| Shared memory | Available (currently `unsafe`) | Compiler-managed (not exposed) |
| Thread races possible | Yes (threads explicit) | No (tile block = single logical thread) |
| Toolchain | Pinned nightly + LLVM | Stable Rust 1.89+ |

## Project Status

Both are early-stage and not production-ready. cuda-oxide is early alpha. cutile-rs is further along with external adoption. APIs will change.

NVIDIA plans inter-language interoperability between CUDA Rust, CUDA C++, and CUDA Python so that choosing one frontend doesn't lock developers out of others.

A related paper, *Fearless Concurrency on the GPU*, is available at [arxiv.org/abs/2606.15991](https://arxiv.org/abs/2606.15991).

---
source_url: https://eiln.github.io/posts/ane-dma.html
author: Eileen Yoon
date: 2026-08-10
---

# Getting 50 GB/s Back Out of the ANE

An RTL performance erratum in the Apple M3 Neural Engine throttles DRAM weight streaming throughput down to 17–19 GB/s from the nominal 45–60 GB/s whenever total weight size is an integer multiple of 1 MiB. This affects 7 of ANEMLL's 15 models. Applying a software fix increased Llama 3.2 1B throughput from 10.0 to 24.3 tokens/s and Qwen3-8B from 1.36 to 2.97 tokens/s.

**Discovery**

While profiling neural engine DRAM weight streaming throughput for single token decode (X[1,D] × W[D,N] = Y[1,N]), the author noticed D=1536 ran nearly 3× faster than D=2048 at N=4096. At D=2048, throughput was 16.93 GB/s vs. 44.5 GB/s at D=2016 — a 27.57 GB/s drop. Data was collected on an M3 Air across 40 runs, with only the ANE register file's DMA size and address changing between measurements.

Sweeping D across a wider range revealed throughput dropping sharply at every multiple of D=2048, recovering to nominal levels just ~256 lines away. An FFT of throughput vs. tensor dimension showed a dominant harmonic with wavelength 2048. The bandwidth floor at multiples sits at 17–19 GB/s, down from nominal 45–60 GB/s.

**Hypothesis 1: DRAM Spatial Correlation**

M3's LPDDR5-6400 provides 128-bit × 6.4 GT/s = 102.4 GB/s theoretical bandwidth, matching the advertised 100 GB/s. The first hypothesis was that ANE's 16 cores might alias onto the same DRAM banks at power-of-two strides.

Testing showed latency remained constant from 1 to 16 active cores for both D=2016 and D=2048, ruling out core-level contention. The throttle existed at the per-core level.

Address scrambling across a ~60 MiB IOVA arena with interleaved baseline/scrambled samples showed median throughput of 31.37 GB/s (baseline) vs. 32.29 GB/s (scrambled) — a marginal 1 GB/s difference, insufficient to explain the ~200% collapse.

**Hypothesis 2: RTL Integer Wraparound**

The collapse repeating at exact power-of-two integer boundaries points to fixed-width digital logic overflow. Bytes per core equal (N/16) kernels × D weights × 2 bytes/weight. Sweeping D and N inversely while keeping total kernel data at exactly 1 MiB per core confirmed that any D×N combination totaling 1 MiB per core triggers the collapse to ~17 GB/s.

Since ANE's resident KMem is 64 KiB per core, some speculative prefetch/credit mechanism operates at the 1 MiB granularity. The key insight: at N=4096, each D += 2048 adds 1 MiB total. With 64-byte line granularity, a 1 MiB transfer is 0x4000 lines, exactly 2^14 lines.

**Speculative Prefetch Analysis**

The notch recovers at exactly ±256 lines around each 0x4000 boundary, and 64 bytes/line × 256 lines = 16 KiB = one VM page on Apple Silicon.

Overlaying bandwidth curves for k=1 (D=2048) and k=2 (D=4096) re-centered at their notches produced nearly identical shapes. More striking: per-lap time slopes are k-linear (R²=0.96–0.99), with a ramp of approximately 3.18 × k µs/line. This means each 0x4000-line period experiences the same throttled bandwidth profile, and k periods repeat that profile k times.

The credit function appears to be credit(x) = min(x, 256), where x is lines away from the boundary. Moving x lines off the boundary returns x prefetch credits up to the 256-line clamp, explaining the linear recovery.

**Likely RTL Bug**

The root cause is a speculative prefetch ring in the kernel DMA engine whose 14-bit head/tail address arithmetic omits a wrap/epoch bit. When a transfer is an exact multiple of 0x4000 lines, the ring aliasing treats "one full lap remaining" as "empty," starving the prefetch pipeline. The suspected buggy logic:

```
assign rd_ptr  = start_line[13:0];
assign end_ptr = (start_line + transfer_lines)[13:0];
assign distance = end_ptr - rd_ptr;  // modulo 0x4000
assign prefetch_credit = (distance > 256) ? 256 : distance;
```

Apple Silicon's 16 KiB pages make 14-bit address arithmetic attractive (addr[13:0] is the page offset, unchanged by virtual-to-physical translation). But 14-bit arithmetic aliases any separation of k × 0x4000, so a full-lap transfer appears identical to an empty transfer.

The fix is straightforward: compute distance in 32-bit space as `transfer_lines - issued_lines` rather than via the truncated 14-bit ring pointers.

**Software Fix**

The software workaround avoids requesting 1 MiB kernel transfers by splitting them into non-1-MiB-multiple chunks. Benchmark results:

- One 0x4000-line task: 17.25 GB/s
- Two 0x2000-line tasks: 45.52 GB/s (2.66×)
- Four 0x1000-line tasks: 44.83 GB/s (2.60×)

A control test confirmed no speedup when splitting transfers that weren't already at 1 MiB multiples, verifying the gain comes specifically from avoiding the prefetch bug.

**DRAM Throughput Results**

| D | Transfer | Original | Fixed | Speedup |
|---|---|---|---|---|
| 2048 | 1 MiB | 17.3 GB/s | 43.5 GB/s | 2.51× |
| 4096 | 2 MiB | 18.4 GB/s | 52.1 GB/s | 2.84× |
| 8192 | 4 MiB | 18.8 GB/s | 57.8 GB/s | 3.07× |
| 16384 | 8 MiB | 19.1 GB/s | 60.5 GB/s | 3.16× |

**Affected ANEMLL Models**

Seven models are affected, including Llama 3.2 1B (gate/up/down projections at 2048×8192), Llama 3.1 8B / DeepSeek / DeepHermes 8B (q and o projections at 4096², gate/up/down at 4096×14336), DeepHermes 3B, Qwen3-8B, and Gemma 3 4B. Splitting the MLP convolutions in affected models yields the reported throughput improvements: Llama 3.2 1B goes from 10 to 24 tokens/s, Qwen3-8B from 1.36 to 2.97 tokens/s.

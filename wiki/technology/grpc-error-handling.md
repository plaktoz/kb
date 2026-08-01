---
type: literature-note
source_url: https://grpc.io/docs/guides/error/
author: Unknown
tags: [grpc, error-handling, protocol-buffers, distributed-systems]
date_consumed: 2026-08-01
---

## Summary

gRPC uses a structured error model where successful calls return an `OK` status and failures return one of several standardized error status codes with an optional message. A richer error model exists for protobuf users, allowing servers to attach additional detail as trailing response metadata, though it comes with cross-language inconsistency and protocol overhead. Error codes are organized around general failures, network failures, and protocol-level errors.

## Core Concepts

- **[[gRPC]] Standard Error Model**: On failure, gRPC returns a status code and an optional human-readable string message.
- **[[gRPC]] Richer Error Model**: Defined by [[Google API Design Guide]], it allows [[Protocol Buffers]] messages to be appended as trailing metadata — supported in C++, Go, Java, Python, and Ruby.
- **Status Codes**: A finite set of canonical codes covering general errors (`CANCELLED`, `DEADLINE_EXCEEDED`, `UNIMPLEMENTED`, `UNAVAILABLE`, `UNKNOWN`), [[Network Failures]] (`DEADLINE_EXCEEDED`, `UNAVAILABLE`), and [[Protocol Errors]] (`INTERNAL`, `UNIMPLEMENTED`, `RESOURCE_EXHAUSTED`, `UNAUTHENTICATED`).
- **[[HTTP/2]] Trailers**: The richer model delivers error detail payloads as trailing response headers, which reduces header compression efficiency and can hit protocol size limits.

## Key Takeaways

- **Success path**: Server returns `OK`; any other status signals failure.
- **Standard model limit**: Cannot communicate structured error details beyond a string message.
- **Richer model**: Attach protobuf detail messages via trailing metadata; five languages supported.
- **Richer model caveats**: Cross-language inconsistency; proxies/loggers blind to detail payloads; compression and size overhead.
- **DEADLINE_EXCEEDED**: Covers both expired deadlines and no-data-before-deadline network failures.
- **UNAVAILABLE**: Used for both server shutdown and mid-transmission connection breaks.
- **INTERNAL**: Used for decompression failures and protobuf parse errors.
- **Language examples**: Available for C++, Go, Java, Node, Python; community `grpc-errors` repo has extras.

## 🃏 Review Questions

**Q1**: What does gRPC return when a call fails under the standard error model?
**A**: It returns one of its error status codes plus an optional string message providing further details.

**Q2**: How does the richer error model deliver additional error details, and what are its main caveats?
**A**: It appends structured protobuf messages as trailing HTTP/2 response metadata; caveats include cross-language inconsistency, proxy/logger blindness to payloads, reduced header compression, and potential protocol size limits.

**Q3**: Which status code should you expect when a client-set deadline expires before data arrives?
**A**: `GRPC_STATUS_DEADLINE_EXCEEDED` is returned for both explicit deadline expiry and network situations where no data arrives before the deadline.

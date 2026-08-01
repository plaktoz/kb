---
type: literature-note
source_url: https://grpc.io/docs/what-is-grpc/core-concepts/
author: Unknown
tags: [grpc, rpc, protocol-buffers, distributed-systems]
date_consumed: 2026-08-01
---

## Summary

gRPC is a high-performance RPC framework that uses [[Protocol Buffers]] as its default Interface Definition Language to describe service interfaces and message structures. It supports four service method types — unary, server streaming, client streaming, and bidirectional streaming — enabling flexible communication patterns between client and server. The framework handles serialization transparently via stub objects and provides lifecycle primitives like deadlines, cancellation, metadata, and channels for robust distributed communication.

## Core Concepts

- **[[gRPC]]**: Remote Procedure Call framework where services declare methods with typed parameters and return values
- **[[Protocol Buffers]]**: Default IDL used to define service contracts and message schemas
- **Service Method Types**:
  - *Unary RPC*: single request, single response — the simplest pattern
  - *[[Server Streaming RPC]]*: one request from client, stream of responses from server
  - *[[Client Streaming RPC]]*: client sends stream of messages, server replies once
  - *[[Bidirectional Streaming RPC]]*: both sides exchange independent streams; per-stream order is preserved
- **Stub**: client-side local object that mirrors server methods and handles serialization/deserialization transparently
- **[[Deadlines and Timeouts]]**: clients set max wait time; exceeding it raises `DEADLINE_EXCEEDED`; APIs vary between duration and fixed-point timestamp
- **Cancellation**: either party may cancel at any time; changes made before cancellation are not rolled back
- **Metadata**: key-value pairs (string keys, string or binary values) attached to calls; keys are case-insensitive and must not start with `grpc-`
- **[[gRPC Channel]]**: abstraction representing a server connection (host + port) with lifecycle states such as `connected` and `idle`

## Key Takeaways

- **Four streaming patterns**: unary, server-streaming, client-streaming, bidirectional cover all communication shapes.
- **Transparent serialization**: stubs abstract all encoding/decoding from application code.
- **Independent termination**: client and server each determine their own success — outcomes can differ.
- **Deadlines not timeouts by default**: some gRPC APIs express time as fixed-point timestamps, not durations.
- **Cancellation is non-transactional**: no rollback guarantee when an RPC is cancelled mid-flight.
- **Metadata restrictions**: keys must be lowercase, case-insensitive, and never prefixed with `grpc-`.
- **Channel state machine**: channels carry explicit connection state (`connected`, `idle`, etc.).

## 🧠 First Principles & Mental Models

- **[[Leaky Abstraction]]**: gRPC stubs hide serialization but surface distributed-systems concerns (deadlines, cancellation, partial failure) that local function calls never expose — the abstraction is necessarily incomplete.
- **[[Fail-Fast Principle]]**: Deadline enforcement causes early termination rather than indefinite blocking, preserving system stability under load.

## 🃏 Review Questions

**Q1**: What is the central design choice that distinguishes gRPC from REST-style HTTP APIs?
**A**: gRPC defines typed service contracts using Protocol Buffers as an IDL, enabling stub-based clients that handle serialization transparently — unlike REST, which relies on ad-hoc HTTP conventions and manual JSON parsing.

**Q2**: How does gRPC handle deadline enforcement, and what happens when a deadline is exceeded?
**A**: Clients set a deadline specifying how long they will wait; if the server does not respond within that window, the call terminates with a `DEADLINE_EXCEEDED` status. APIs differ between duration-based and fixed-point-timestamp representations.

**Q3**: What practical implication does gRPC's independent termination model have for distributed system design?
**A**: Because client and server independently determine success, callers cannot assume the server's view matches their own — error handling must account for ambiguous outcomes rather than treating the server's status as ground truth.

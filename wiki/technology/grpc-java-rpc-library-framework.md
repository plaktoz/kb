---
type: literature-note
source_url: https://github.com/grpc/grpc-java
author: Unknown
tags: [grpc, java, rpc, protocol-buffers]
date_consumed: 2026-08-01
---

## Summary

gRPC-Java is the official Java implementation of gRPC, an [[HTTP/2]]-based RPC framework supporting Java 8+ and Android (minSdkVersion 24+). Its current release is 1.83.1, distributed under the Apache-2.0 license. The library structures its internals into three distinct layers — Stub, Channel, and Transport — each with clearly separated responsibilities.

## Core Concepts

- **[[gRPC-Java]]**: the Java implementation of the [[gRPC]] framework; HTTP/2-based, supports Java 8+, Android, and multiple transport backends
- **[[Protocol Buffers]]**: `.proto` files are the source of truth for service contracts; the protobuf compiler generates type-safe Java stubs
- **Three-Layer Architecture**:
  - **Stub layer**: developer-facing, type-safe bindings generated from `.proto` files
  - **Channel layer**: transport abstraction; the right place to add logging, auth, and monitoring via [[gRPC Interceptors]]
  - **Transport layer**: handles raw bytes on the wire
- **Transport backends**: [[Netty]] (primary, non-Android), [[OkHttp]] (Android), in-process (testing and production), and Binder (Android IPC)
- **Maven dependencies**: `grpc-netty-shaded`, `grpc-protobuf`, `grpc-stub` under `io.grpc` for non-Android; `grpc-okhttp` and `grpc-protobuf-lite` for Android
- **API stability annotations**: `@Internal` marks APIs for gRPC-library use only; `@ExperimentalApi` signals instability across releases

## Key Takeaways

- **Three-layer design**: Stub → Channel → Transport separates concerns cleanly.
- **Transport choice matters**: Netty for servers/desktop; OkHttp for Android; in-process for testing.
- **Android dependency swap**: replace `grpc-netty-shaded`/`grpc-protobuf` with `grpc-okhttp`/`grpc-protobuf-lite`.
- **Avoid `@Internal` APIs**: reserved for gRPC internals; not stable for external use.
- **`@ExperimentalApi`**: signals the API may change across minor releases.
- **Community size**: ~12.1k stars, ~4k forks; Apache-2.0 license.

## 🧠 First Principles & Mental Models

- **[[Separation of Concerns]]**: The three-layer architecture (Stub/Channel/Transport) is a direct application of this principle — each layer handles exactly one responsibility, making it possible to swap transports (Netty ↔ OkHttp) without touching the generated stub code.

## 🃏 Review Questions

**Q1**: What is the core architectural design of gRPC-Java and what are its three layers?
**A**: gRPC-Java uses a three-layer architecture: the Stub layer provides developer-facing, type-safe bindings generated from `.proto` files; the Channel layer abstracts over transport and handles cross-cutting concerns like auth and logging; and the Transport layer handles raw bytes on the wire.

**Q2**: Which transport backend should be used for Android applications, and which dependencies does it require?
**A**: Android applications should use the OkHttp transport backend, substituting `grpc-okhttp` and `grpc-protobuf-lite` in place of the `grpc-netty-shaded` and `grpc-protobuf` artifacts used on non-Android platforms.

**Q3**: What do the `@Internal` and `@ExperimentalApi` annotations signal to gRPC-Java users?
**A**: `@Internal` marks APIs intended for use only by the gRPC library itself and should not be called by external users; `@ExperimentalApi` indicates that the API may change or be removed across releases without a stability guarantee.

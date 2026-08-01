---
type: literature-note
source_url: https://grpc.io/docs/languages/java/basics/
author: Unknown
tags: [grpc, java, protocol-buffers, rpc]
date_consumed: 2026-08-01
---

## Summary

This tutorial introduces Java developers to gRPC fundamentals by walking through the `RouteGuide` example service. It covers defining services in `.proto` files, generating client/server stubs via the protocol buffer compiler, and implementing both server and client using the Java gRPC API. Four RPC method types are demonstrated: simple, server-side streaming, client-side streaming, and bidirectional streaming.

## Core Concepts

- **[[gRPC]]**: a high-performance RPC framework using [[Protocol Buffers]] for service and message definition
- **[[Protocol Buffers]]**: the IDL used to define service contracts in `.proto` files; the compiler generates Java stubs
- **[[StreamObserver]]**: the Java interface used by both clients and servers to send and receive streaming messages
- **[[ManagedChannel]]**: the gRPC channel abstraction from which client stubs are created
- **Blocking vs Async Stubs**: a blocking stub handles synchronous calls; an async stub is required for any streaming RPC
- **Four RPC types**: simple RPC, server-side streaming, client-side streaming, and bidirectional streaming, each defined with `stream` keywords in `.proto`

## Key Takeaways

- **Service definition**: all four RPC types are declared in a single `.proto` file using `stream` keywords.
- **Server impl**: extends `RouteGuideGrpc.RouteGuideImplBase`, overrides methods with `StreamObserver` response param.
- **Simple RPC pattern**: call `onNext(result)` then `onCompleted()` on the `StreamObserver`.
- **Client-side streaming**: server method returns a `StreamObserver<Point>` instead of accepting one.
- **Server-side streaming (blocking)**: returns `Iterator<Feature>` rather than a single object.
- **Two stubs required**: blocking stub for unary calls; async stub for any streaming interaction.
- **Setup**: clone `grpc-java` at a tagged version and build from the `examples/` directory.

## 🃏 Review Questions

**Q1**: What are the four RPC method types supported by gRPC, as demonstrated in the `RouteGuide` example?
**A**: Simple RPC, server-side streaming RPC, client-side streaming RPC, and bidirectional streaming RPC — each declared in the `.proto` file using the `stream` keyword on request or response types.

**Q2**: How does a Java gRPC server handle a client-side streaming RPC differently from a simple RPC?
**A**: For client-side streaming, the server method returns a `StreamObserver<Point>` (the request observer) rather than accepting a `StreamObserver` as a final parameter, allowing it to process each incoming message incrementally.

**Q3**: When should a developer use the async stub instead of the blocking stub in a Java gRPC client?
**A**: The async stub is required for any streaming RPC call; the blocking stub is only suitable for simple unary calls where a direct response is returned synchronously.

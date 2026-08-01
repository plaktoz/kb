# gRPC-Java: An RPC Library and Framework

source_url: https://github.com/grpc/grpc-java

---

gRPC-Java is the Java implementation of gRPC, an HTTP/2-based RPC framework. It supports Java 8+ and Android (minSdkVersion 24+). Current version: 1.83.1.

Key dependency snippets:
- Maven (non-Android): Uses `grpc-netty-shaded`, `grpc-protobuf`, and `grpc-stub` artifacts under `io.grpc`.
- Android: Substitutes `grpc-okhttp` and `grpc-protobuf-lite` in place of the Netty/protobuf variants.

Architecture — the library has three layers:
- Stub: developer-facing, type-safe bindings generated from `.proto` files
- Channel: abstraction over transport; suited for logging, auth, and monitoring concerns
- Transport: handles bytes on the wire; includes Netty (primary), OkHttp (Android), in-process (testing/production), and Binder (Android IPC)

API notes: APIs annotated with `@Internal` are for internal use by the gRPC library and should not be used by gRPC users. `@ExperimentalApi` annotations signal instability across releases.

Stats: ~12.1k stars, ~4k forks, Apache-2.0 licensed.

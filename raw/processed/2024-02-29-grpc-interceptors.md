# Interceptors — gRPC Documentation

source_url: https://grpc.io/docs/guides/interceptors/

---

Interceptors provide a way to implement generic behavior across many RPC methods in gRPC. They are analogous to what other frameworks call "filters" or "middleware."

**When to Use Interceptors**
Interceptors excel at handling logic not specific to a single RPC method, easily shared across clients or servers. Common use cases: metadata handling, logging, fault injection, caching, metrics, policy enforcement, server-side authentication and authorization. Note: for client-side authentication, gRPC offers a dedicated "call credentials" API rather than interceptors.

**How to Use Interceptors**
Interceptors are added when building a gRPC channel or server, after which they apply to every RPC on that channel/server. They come in two varieties: client interceptors and server interceptors. Important limitations: interceptors are per-call and cannot manage TCP connections, configure ports, or configure TLS.

**Interceptor Order**
When chaining multiple interceptors, order matters. Think of interceptors as a line between the application and the network — some sit closer to the network, others closer to the application. For example, with a caching interceptor and a logging interceptor:
- Logging closer to the network: monitors actual communication, ignores cache hits
- Logging closer to the application: reveals what data the app is requesting

**Language Support**
- C++: grpc/examples/cpp/interceptors
- Go: grpc-go/examples/features/interceptor
- Java: grpc-java/examples/.../header
- Python: grpc/examples/python/interceptors

# Core Concepts, Architecture and Lifecycle — gRPC Documentation

source_url: https://grpc.io/docs/what-is-grpc/core-concepts/

---

gRPC defines services by specifying remotely callable methods with parameters and return types. It uses protocol buffers as its default IDL for describing service interfaces and message structures.

**Four Service Method Types**
1. Unary RPC — single request, single response: `rpc SayHello(HelloRequest) returns (HelloResponse);`
2. Server streaming — client sends one request, receives a stream of responses
3. Client streaming — client sends a stream of messages, server returns one response
4. Bidirectional streaming — both sides send independent message streams; order within each stream is preserved

**API Usage**
- Server side: implements declared methods, runs a gRPC server that decodes requests and encodes responses
- Client side: uses a local stub object mirroring the service methods, handling serialization/deserialization transparently

**RPC Lifecycle Highlights**
- Unary: client calls stub → server notified with metadata, method name, deadline → server responds with status and optional trailing metadata
- Deadlines: clients set how long they'll wait; exceeding it yields `DEADLINE_EXCEEDED`. Some APIs use durations, others use fixed-point timestamps.
- Termination: client and server make independent success determinations — outcomes can differ
- Cancellation: either side may cancel at any time; "changes made before a cancellation are not rolled back"
- Metadata: key-value pairs (string keys, string or binary values); keys are case-insensitive, must not start with `grpc-`
- Channels: provide a server connection (host + port); carry state such as `connected` and `idle`

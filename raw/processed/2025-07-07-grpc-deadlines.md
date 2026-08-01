# Deadlines | gRPC Documentation

source_url: https://grpc.io/docs/guides/deadlines/

---

A deadline specifies a point in time past which a client won't wait for a server response — a critical concept for building robust distributed systems.

**Deadline vs. Timeout distinction:**
- Deadline: a fixed point in time the call must not exceed
- Timeout: maximum duration for the call (can be converted to a deadline by adding it to the current time)

**Deadlines on the Client:** gRPC sets no deadline by default, meaning clients could wait indefinitely. Always set realistic deadlines explicitly. If the server exceeds the deadline, the client fails the RPC with `DEADLINE_EXCEEDED` status.

**Deadlines on the Server:** Servers receiving RPCs with unrealistically short deadlines waste resources and risk crashes. gRPC automatically cancels such calls (`CANCELLED` status) once the client's deadline passes. Server applications must also stop any spawned activity and periodically check if an initiating RPC has been cancelled.

**Deadline Propagation:** When a server also acts as a client, it should honor the original client's deadline. Some gRPC implementations propagate deadlines automatically (Java, Go by default; C++ requires explicit enablement). To handle clock skew between servers, gRPC converts deadlines to timeouts with already-elapsed time deducted.

**Language Support:** Java (grpc-java examples/deadline), Go (grpc-go examples/features/deadline), C++ (grpc examples/cpp/deadline), Python (grpc examples/python/timeout)

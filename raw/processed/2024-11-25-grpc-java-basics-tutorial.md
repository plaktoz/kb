# Basics Tutorial | Java | gRPC

source_url: https://grpc.io/docs/languages/java/basics/

---

This tutorial introduces Java developers to gRPC fundamentals, covering: defining services in `.proto` files, generating client/server code via the protocol buffer compiler, and writing clients and servers using the Java gRPC API.

Service definition — four RPC method types are demonstrated in `RouteGuide`:

| Type | Proto Syntax |
|------|-------------|
| Simple RPC | `rpc GetFeature(Point) returns (Feature) {}` |
| Server-side streaming | `rpc ListFeatures(Rectangle) returns (stream Feature) {}` |
| Client-side streaming | `rpc RecordRoute(stream Point) returns (RouteSummary) {}` |
| Bidirectional streaming | `rpc RouteChat(stream RouteNote) returns (stream RouteNote) {}` |

Server implementation: The server extends `RouteGuideGrpc.RouteGuideImplBase` and overrides methods using `StreamObserver` for responses. For simple RPCs, the pattern is calling `responseObserver.onNext(result)` then `responseObserver.onCompleted()`. For client-side streaming, the method returns a `StreamObserver<Point>` rather than accepting one as a final parameter.

Client implementation: Two stubs are created from a `ManagedChannel`:
- Blocking stub: synchronous calls, returns responses directly
- Async stub: required for streaming calls, uses `StreamObserver` callbacks

Server-side streaming via the blocking stub returns an `Iterator<Feature>` instead of a single object.

Setup:
```
git clone -b v1.81.0 --depth 1 https://github.com/grpc/grpc-java
cd grpc-java/examples
```

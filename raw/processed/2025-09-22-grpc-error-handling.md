# Error Handling | gRPC

source_url: https://grpc.io/docs/guides/error/

---

Standard error model: When a gRPC call succeeds, the server returns an `OK` status. On failure, gRPC returns one of its error status codes along with an optional string message providing further details.

Richer error model: The standard model is limited — it cannot communicate error details. For protobuf users, Google has developed a richer error model (described at cloud.google.com/apis/design/errors) that lets servers return additional details as protobuf messages, delivered as trailing response metadata. This richer model is supported in C++, Go, Java, Python, and Ruby. Caveats: cross-language inconsistency in handling error detail payloads; proxies and loggers lack visibility into those details; extra trailer data reduces HTTP/2 header compression efficiency; large payloads may hit protocol limits.

Error status codes:

General errors:
| Case | Status Code |
|------|-------------|
| Client cancelled request | `GRPC_STATUS_CANCELLED` |
| Deadline expired | `GRPC_STATUS_DEADLINE_EXCEEDED` |
| Method not found | `GRPC_STATUS_UNIMPLEMENTED` |
| Server shutting down | `GRPC_STATUS_UNAVAILABLE` |
| Server threw exception | `GRPC_STATUS_UNKNOWN` |

Network failures:
| Case | Status Code |
|------|-------------|
| No data before deadline | `GRPC_STATUS_DEADLINE_EXCEEDED` |
| Connection breaks mid-transmission | `GRPC_STATUS_UNAVAILABLE` |

Protocol errors:
| Case | Status Code |
|------|-------------|
| Decompression failure | `GRPC_STATUS_INTERNAL` |
| Unsupported compression | `GRPC_STATUS_UNIMPLEMENTED` |
| Flow-control limits reached | `GRPC_STATUS_RESOURCE_EXHAUSTED` |
| Unauthenticated / invalid authority | `GRPC_STATUS_UNAUTHENTICATED` |
| Response/request protobuf parse error | `GRPC_STATUS_INTERNAL` |

Language support: Examples are available for C++, Go, Java, Node, and Python via their respective GitHub repositories. The community repo `grpc-errors` also offers additional examples.

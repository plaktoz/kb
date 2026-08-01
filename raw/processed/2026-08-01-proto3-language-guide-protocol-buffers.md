# Language Guide (proto 3) — Protocol Buffers Documentation

source_url: https://protobuf.dev/programming-guides/proto3/

---

This is the official reference guide for proto3, the third revision of Protocol Buffers' schema language.

**Defining Messages**
A `.proto` file begins with `syntax = "proto3";` as the first non-empty, non-comment line. Fields require a name, type, and a unique number between 1–536,870,911. Numbers 19,000–19,999 are reserved for internal use. Field numbers 1–15 cost one byte to encode; 16–2047 cost two bytes.

**Field Cardinality**
- `optional` (recommended): tracks whether a value was explicitly set
- implicit (not recommended): scalar fields cannot distinguish between "unset" and "set to default"
- `repeated`: ordered, zero-or-more values; scalar numeric types are packed by default
- `map`: key/value pairs; keys must be integral or string types

**Scalar Types**
`double`, `float`, `int32`, `int64`, `uint32`, `uint64`, `sint32`, `sint64`, `fixed32`, `fixed64`, `sfixed32`, `sfixed64`, `bool`, `string`, and `bytes`.

**Enumerations**
The first enum value must be zero. Recommended naming: `ENUM_TYPE_NAME_UNSPECIFIED = 0;`. Aliases are allowed with `option allow_alias = true;`.

**Updating Messages**
- Wire-unsafe: changing field numbers, moving fields into an existing `oneof`
- Wire-safe: adding/removing fields, adding enum values
- Wire-compatible (conditional): `int32`↔`int64`↔`bool`↔`uint32`↔`uint64` are mutually compatible; `string`/`bytes`/embedded messages have limited cross-compatibility

**Oneof**
Groups mutually exclusive fields sharing memory. Setting one field clears all others. If the parser encounters multiple members of the same oneof on the wire, only the last member seen is used.

**Maps**
Syntax: `map<key_type, value_type> field_name = N;`. Internally equivalent to a repeated message with key/value fields. Ordering is undefined.

**Reserved Fields**
Deleted field numbers and names should be reserved to prevent reuse:
```
message Foo {
  reserved 2, 15, 9 to 11;
  reserved "foo", "bar";
}
```

**Options**
Common options: `java_package`, `java_multiple_files`, `optimize_for` (SPEED/CODE_SIZE/LITE_RUNTIME), `deprecated`, `packed`.

**Generating Code**
Run `protoc` with appropriate output flags (`--cpp_out`, `--java_out`, `--go_out`, etc.) and set `--proto_path` to the highest-level directory containing your protos.

# Protocol Buffer Basics: Java

source_url: https://protobuf.dev/getting-started/javatutorial/

---

This tutorial introduces Java developers to working with protocol buffers, covering three main areas: defining message formats in `.proto` files, using the protocol buffer compiler, and reading and writing messages via the Java API.

**The Problem Domain**
An "address book" application demonstrates how protobuf solves structured data serialization more efficiently than Java Serialization, ad-hoc string encoding, or XML.

**Proto File Definition**
The example uses `addressbook.proto` with `syntax = "proto2"`, defining `Person` (with nested `PhoneNumber` and `PhoneType` enum) and `AddressBook` messages. Java-specific options: `java_multiple_files`, `java_package`, `java_outer_classname`. Field modifiers: `optional`, `repeated`, and `required` (required fields are "strongly disfavored" internally at Google).

**Generated API**
The compiler produces immutable message classes with builder counterparts. Builders support method chaining. Key serialization methods: `toByteArray()`, `parseFrom()`, `writeTo()`, and `parseFrom(InputStream)`.

**Extending Protos (Compatibility Rules)**
- Must not change existing tag numbers
- Must not add/delete required fields
- May delete optional or repeated fields
- May add new optional/repeated fields using fresh tag numbers

**Advanced Usage**
Protobuf supports reflection via `Message` and `Message.Builder` interfaces, enabling field iteration and conversion to formats like XML or JSON without message-type-specific code.

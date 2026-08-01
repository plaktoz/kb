# Quick Start: gRPC Java

source_url: https://grpc.io/docs/languages/java/quickstart/

---

This guide walks through setting up gRPC in Java using a simple client-server example.

Prerequisites: JDK version 7 or higher.

Clone the repository and navigate to examples:
```
git clone -b v1.81.0 --depth 1 https://github.com/grpc/grpc-java
cd grpc-java/examples
```

Running the basic example:
1. Compile: `./gradlew installDist`
2. Start server: `./build/install/examples/bin/hello-world-server`
3. Run client: `./build/install/examples/bin/hello-world-client`

Expected client output includes `"Greeting: Hello world"`.

The guide demonstrates extending the service by adding a second RPC method (`SayHelloAgain`) to the existing `Greeter` service defined in a `.proto` file. The service originally defines `SayHello`, which takes a `HelloRequest` and returns a `HelloReply`. After modifying the proto file, both server and client implementations require updates to handle the new method. The build process auto-regenerates gRPC stub classes, but hand-written logic must be added manually. After updates, the client outputs both `"Greeting: Hello world"` and `"Greeting: Hello again world"`.

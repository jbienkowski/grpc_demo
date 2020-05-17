# Introduction

Demo gRPC project.

# Install Python virtual environment and dependencies

1. Install virtual environment:
    ```
    $ python3 -m venv env
    ```
1. Install numpy (otherwise obspy installation will fail):
    ```
    $ pip install numpy
    ```
1. Install rest of the dependencies:
    ```
    $ pip install -r requirements.txt
    ```

# Docker

1. Build the gRPC server image using:
    ```
    $ docker build -t grpc .
    ```
1. Run the gRPC server container using:
    ```
    $ docker run -d -p 127.0.0.1:50051:50051/tcp grpc:latest
    ```

# Dev and sidenotes

## Rebuild gRPC classes

1. Generate gRPC code for the server:
    ```
    $ python3 -m grpc_tools.protoc -I./protos --python_out=./server/grpc_classes --grpc_python_out=./server/grpc_classes ./protos/grpc_demo.proto
    ```
1. Generate gRPC code for the client:
    ```
    $ python3 -m grpc_tools.protoc -I./protos --python_out=./client/grpc_classes --grpc_python_out=./client/grpc_classes ./protos/grpc_demo.proto
    ```
1. After generating the gRPC code, one of the imports in the `grpc_demo_pb2_grpc.py` needs to be changed from:
    ```
    import grpc_demo_pb2 as grpc__demo__pb2
    ```
    to:
    ```
    from . import grpc_demo_pb2 as grpc__demo__pb2
    ```
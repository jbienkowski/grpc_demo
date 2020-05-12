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

# Rebuild gRPC classes

1. Build classes for the server:
    ```
    $ python3 -m grpc_tools.protoc -I./protos --python_out=./server/grpc_classes --grpc_python_out=./server/grpc_classes ./protos/grpc_demo.proto
    ```
1. Build the classes for the client:
    ```
    $ python3 -m grpc_tools.protoc -I./protos --python_out=./client/grpc_classes --grpc_python_out=./client/grpc_classes ./protos/grpc_demo.proto
    ```
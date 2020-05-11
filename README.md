# Introduction

Demo gRPC project.

# Rebuild gRPC

Build classes for the server:

`$ python3 -m grpc_tools.protoc -I./protos --python_out=./server/grpc_classes --grpc_python_out=./server/grpc_classes ./protos/grpc_demo.proto`

Build the classes for the client:

`$ python3 -m grpc_tools.protoc -I./protos --python_out=./client/grpc_classes --grpc_python_out=./client/grpc_classes ./protos/grpc_demo.proto`
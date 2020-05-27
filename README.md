# Introduction

Demo gRPC project.

# Install Python virtual environment and dependencies

1. Install and activate the virtual environment:
    ```
    $ python3 -m venv env
    $ source env/bin/activate
    ```
1. Install numpy (otherwise obspy installation will fail):
    ```
    $ pip install numpy
    ```
1. Install rest of the dependencies:
    ```
    $ pip install -r requirements.txt
    ```

# Running the software (basic)

1. Python server
    ```
    $ python3 server/server.py
    ```
1. Python client
    1. Ping server
        ```
        $ python3 client_python/client.py --ping
        ```
    1. Get biggest event in last 7 days
        ```
        $ python3 client_python/client.py --past 7
        ```
    1. Get biggest event that happened on 2020-01-21 [YYYY MM DD]
        ```
        $ python3 client_python/client.py --day 2020 01 21
        ```
1. C# client
    1. Build the client
        ```
        $ dotnet build client_csharp/
        ```
    1. Ping server
        ```
        $ dotnet client_csharp/bin/Debug/netcoreapp3.1/gRPC.dll --ping
        ```
    1. Get biggest event in last 7 days
        ```
        $ dotnet client_csharp/bin/Debug/netcoreapp3.1/gRPC.dll --past 7
        ```
    1. Get biggest event that happened on 2020-01-21 [YYYY MM DD]
        ```
        $ dotnet client_csharp/bin/Debug/netcoreapp3.1/gRPC.dll --day 2020 01 21

```

# Build the gRPC server and haproxy images

1. Build the gRPC server image using:
    ```
    $ ./generate_keys
    $ docker build -t grpc .
    ```
2. Run the gRPC server container using:
    ```
    $ cd haproxy
    $ docker build -t my-haproxy .
    ```



# Containers network setup

1. Create dedicated network
    1. Create grpc_demo network with 172.18.0.0/16 ipv4 address space:
        ```
        $ docker network create --subnet=172.18.0.0/16 grpc_demo
        ```
    2. Run the haproxy load balancer container using:
        ```
        $ docker run --net grpc_demo --ip 172.18.0.254 -d -p 127.0.0.1:50051:50051/tcp my-haproxy
        ```
    3. Run the gRPC secure server container using:
        ```
        $ docker run -d -p 127.0.0.1:50443:50443/tcp grpc:latest
        ```
    4. Run 3 backend servers containers using:
        ```
        $ docker run -d --net grpc_demo --ip 172.18.0.2 grpc:latest
        $ docker run -d --net grpc_demo --ip 172.18.0.3 grpc:latest
        $ docker run -d --net grpc_demo --ip 172.18.0.4 grpc:latest
        ```
        
        

# Dev and sidenotes

## Rebuild gRPC classes

1. After changing the proto file (`protos/grpc_demo.proto`), do not forget to copy it over to the C# client (`client_csharp/Protos/grpc_demo.proto`).
1. Generate gRPC code for the server:
    ```
    $ python3 -m grpc_tools.protoc -I./protos --python_out=./server/grpc_classes --grpc_python_out=./server/grpc_classes ./protos/grpc_demo.proto
    ```
1. Generate gRPC code for the client:
    ```
    $ python3 -m grpc_tools.protoc -I./protos --python_out=./client_python/grpc_classes --grpc_python_out=./client_python/grpc_classes ./protos/grpc_demo.proto
    ```
1. After generating the gRPC code, one of the imports in the `grpc_demo_pb2_grpc.py` needs to be changed from:
    ```
    import grpc_demo_pb2 as grpc__demo__pb2
    ```
    to:
    ```
    from . import grpc_demo_pb2 as grpc__demo__pb2
    ```

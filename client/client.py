
from __future__ import print_function
import logging

import grpc

from grpc_classes import grpc_demo_pb2
from grpc_classes import grpc_demo_pb2_grpc


def ping_server():
    with grpc.insecure_channel('127.0.0.1:50051') as channel:
        stub = grpc_demo_pb2_grpc.SeismoServiceStub(channel)
        response = stub.SeismoPing(
            grpc_demo_pb2.SeismoPingRequest(name='client')
        )
    print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    ping_server()

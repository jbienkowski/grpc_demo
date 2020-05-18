from concurrent import futures
import logging

import grpc

from grpc_classes import grpc_demo_pb2
from grpc_classes import grpc_demo_pb2_grpc

import obspy


class SeismoServer(grpc_demo_pb2_grpc.SeismoServiceServicer):
    def SeismoPing(self, request, context):
        return grpc_demo_pb2.SeismoPingReply(message=f"Hello, {request.name}!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    grpc_demo_pb2_grpc.add_SeismoServiceServicer_to_server(SeismoServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

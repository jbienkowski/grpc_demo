from concurrent import futures
import logging

import grpc

from grpc_classes import grpc_demo_pb2
from grpc_classes import grpc_demo_pb2_grpc


from obspy.core.event import read_events
from obspy import UTCDateTime
from obspy.clients.fdsn import Client


class SeismoServer(grpc_demo_pb2_grpc.SeismoServiceServicer):
    def SeismoPing(self, request, context):
        return grpc_demo_pb2.SeismoPingReply(message=f"Hello, {request.name}!")

    def BiggestEventInDays(self, request, context):
        starttime = UTCDateTime() - request.days * 24 * 60 * 60

        client = Client("EMSC")
        response = client.get_events(starttime=starttime, orderby="magnitude", limit=1)

        event = response.events[0]
        mag = event.magnitudes[0].mag
        lat = event.origins[0].latitude
        lon = event.origins[0].longitude

        reply = grpc_demo_pb2.BiggestEventReply()
        reply.magnitude = mag
        reply.latitude = lat
        reply.longitude = lon
        return reply

    def BiggestEventOn(self, request, context):
        starttime = UTCDateTime(request.year, request.month, request.day)
        endtime = starttime + 24 * 60 * 60

        client = Client("EMSC")
        response = client.get_events(
            starttime=starttime, endtime=endtime, orderby="magnitude", limit=1
        )

        event = response.events[0]
        mag = event.magnitudes[0].mag
        lat = event.origins[0].latitude
        lon = event.origins[0].longitude

        reply = grpc_demo_pb2.BiggestEventReply()
        reply.magnitude = mag
        reply.latitude = lat
        reply.longitude = lon
        return reply


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    grpc_demo_pb2_grpc.add_SeismoServiceServicer_to_server(SeismoServer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()

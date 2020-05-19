from __future__ import print_function
import argparse
import logging

import grpc

from grpc_classes import grpc_demo_pb2
from grpc_classes import grpc_demo_pb2_grpc


def ping():
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = grpc_demo_pb2_grpc.SeismoServiceStub(channel)
        reply = stub.SeismoPing(grpc_demo_pb2.SeismoPingRequest(name="Python Client"))
    print(reply.message)


def past(daysBack):
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = grpc_demo_pb2_grpc.SeismoServiceStub(channel)
        reply = stub.BiggestEventInDays(
            grpc_demo_pb2.BiggestEventInDaysRequest(days=daysBack)
        )
    print(
        f"Biggest event in last {daysBack} days had magnitude of {round(reply.magnitude, 2)}, latitude {round(reply.latitude, 2)} and longitude {round(reply.longitude, 2)}"
    )


def day(year, month, day):
    with grpc.insecure_channel("127.0.0.1:50051") as channel:
        stub = grpc_demo_pb2_grpc.SeismoServiceStub(channel)
        reply = stub.BiggestEventOn(
            grpc_demo_pb2.BiggestEventOnRequest(year=year, month=month, day=day)
        )
    print(
        f"Biggest event on {year}-{month}-{day} had magnitude of {round(reply.magnitude, 2)}, latitude {round(reply.latitude, 2)} and longitude {round(reply.longitude, 2)}"
    )


if __name__ == "__main__":
    logging.basicConfig()
    parser = argparse.ArgumentParser(description="Access to the SeismoServer.")
    parser.add_argument("--ping", help="pings the server", action="store_true")
    parser.add_argument(
        "--past", dest="past", type=int, help="show biggest event from past X days"
    )
    parser.add_argument(
        "--day",
        dest="day",
        type=int,
        nargs="+",
        help="show biggest event from past X days",
    )

    args = parser.parse_args()

    if args.ping:
        ping()

    if args.past:
        past(args.past)

    if args.day:
        day(args.day[0], args.day[1], args.day[2])

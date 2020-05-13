FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y \
    python3-dev \
    python3-setuptools \
    python3-pip

RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

RUN mkdir -p /data/grpc
WORKDIR /data/grpc

COPY requirements.txt /data/grpc

# Dependencies
RUN pip3 install numpy
RUN pip3 install -r requirements.txt

# Copy sources
COPY server/ /data/grpc/

CMD python3 /data/grpc/server.py
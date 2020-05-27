FROM ubuntu:18.04

# Update package list
RUN apt-get update -y
RUN apt-get install net-tools

# Install Python and pip
RUN apt-get install -y \
    python3-dev \
    python3-setuptools \
    python3-pip

# Upgrade pip and Python setuptools
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

# Prepare dir for the server
RUN mkdir -p /data/grpc
WORKDIR /data/grpc

# Copy list of required Python modules
COPY requirements.txt /data/grpc


# Install required Python modules
RUN pip3 install numpy
RUN pip3 install -r requirements.txt

# Copy sources
COPY server/ /data/grpc/

# Define entrypoint command
CMD python3 /data/grpc/server.py

#!/bin/bash

# Copy in the latest protobuf messages 
cp ../common/messages_pb2.py .

# Build the docker image and tag it
docker build -t hal .
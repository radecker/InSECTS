#!/bin/bash
set -e
set -o pipefail

# Generate an updated config proto file based on yaml
python yaml_to_proto.py

# Compile protobuf messages and generate new classes
protoc -I=. --python_out=. config.proto message.proto
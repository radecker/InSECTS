#!/bin/bash

# Compile protobuf messages and generate new classes
protoc -I=. --python_out=. messages.proto
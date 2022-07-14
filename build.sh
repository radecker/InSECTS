#!/bin/bash

# Run the common library build first
cd common/
./build.sh

# Build each individual app
cd ../hal/
./build.sh
cd ../autonomy_app/
./build.sh
cd ../demo_app/
./build.sh
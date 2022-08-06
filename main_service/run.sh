#!/bin/bash
docker run -v /home/insects/InSECTS-Vehicle-Testbed/main_service/config.yaml:/usr/src/app/config.yaml:ro --network=host vehicle.main_service

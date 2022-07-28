#!/usr/bin/env python3

from TCPClient import TCPClient
from UDPClient import UDPClient
from BaseApp import BaseApp
import message_pb2 as proto
import time

# Autonomy Rules
#
# initial: fan speed @ 25%
# initial: baffle = closed
#
# if heater temp >95C @ 25% speed, increase fan speed to 50%
# if heater temp >95C @ 50% speed, increase fan speed to 75%
# if heater temp >95C @ 75% speed, increase fan speed to 100%
#
# if heater temp <80C @100% speed, decrease fan speed to 75%
# if heater temp <80C @75% speed, decrease fan speed to 50%
# if heater temp <80C @50% speed, decrease fan speed to 25%
#
# if fan OR servomotor temp >50C @ baffle = closed, set baffle = half-open
# if fan OR servomotor temp >50C @ baffle = half-open, set baffle = full-open
#
# if fan OR servomotor temp <0C @ baffle = full-open, set baffle = half-open
# if fan OR servomotor temp <0C @ baffle = half-open, set baffle = closed


class AutonomyApp(BaseApp):
    def __init__(self) -> None:
        super().__init__("vehicle.autonomy_app")

    def setup(self):
        print("SETUP!")
        print(self.config_params)

    def run(self):
        print("Autonomy Run!")
        # Check for command messages
        # Check for telemetry messages
        time.sleep(1)


if __name__ == "__main__":
    AutonomyApp()   # Runs the app
    

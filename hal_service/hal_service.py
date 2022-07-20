#!/usr/bin/env python3

from TCPServer import TCPServer
from BaseApp import BaseApp
import message_pb2 as proto
import serial
import time

"""
Purpose: This app is supposed to expose/emulate much of the hardware functions to the applications running

Use Cases:
    1. Abstract serial connection to arduino/wowki
    2. ????
"""

class HalService(BaseApp):
    def __init__(self) -> None:
        self.arduino_addr = None
        super().__init__(id="vehicle.hal_service")

    def _send_to_arduino(self):
        if self.config_params.emulate_arduino:
            # Connect to Wowki server instead
            pass
        else:
            # Send data over serial
            pass

    def setup(self):
        self.arduino_addr = self.config_params.

    def run(self):
        pass

    def shutdown(self):
        pass


if __name__ == "__main__":
    HalService()
#!/usr/bin/env python3

from UDPClient import UDPClient

import message_pb2 as proto
import socket
import threading
import queue
import time

"""
General sequence:
    1. Connect to infrastructure multicast group
    2. Listen for config params and read them in
    3. perform ack that all apps see each other (skip for now)
    4. Call Setup with startup params as message input
    5. Call Run
"""

class BaseApp():
    def __init__(self, id: str) -> None:
        self.udp_client = UDPClient(id=id)
        self.config_params = None

        self.__startup_group = "224.1.1.99"
        self.__startup_port = 5099
        self.__command_group = None
        self.__command_port = None
        self.__telemetry_group = None
        self.__telemetry_port = None

        self.__initialize()
        self.setup()
        while True:
            self.run()

    def __initialize(self):
        """Sets up connection and listens for init params from main controller
        """
        self.udp_client.add_listener(group=self.__startup_group, port=self.__startup_port)
        self.udp_client.add_sender(group=self.__startup_group, port=self.__startup_port)
        self.__wait_for_config_params()
        self.__connect_command_group()
        self.__connect_telemetry_group()

    def __wait_for_config_params(self) -> None:
        """Waits until config params have been received
        """
        while self.config_params is None:
            messages = self.udp_client.get_messages()
            for message in messages:
                if message.HasField("config_params"):
                    self.config_params = message.config_params

    def __connect_command_group(self):
        """Setup connection and start listening for any commands
        """
        self.__command_group = self.config_params.command_multicast_ip
        self.__command_port = self.config_params.command_multicast_port
        self.udp_client.add_listener(group=self.__command_group, port=self.__command_port)
        self.udp_client.add_sender(group=self.__command_group, port=self.__command_port)

    def __connect_telemetry_group(self):
        """Setup connection and start listening for any telemetry
        """
        self.__telemetry_group = self.config_params.telemetry_multicast_ip
        self.__telemetry_port = self.config_params.telemetry_multicast_port
        self.udp_client.add_listener(group=self.__telemetry_group, port=self.__telemetry_port)
        self.udp_client.add_sender(group=self.__telemetry_group, port=self.__telemetry_port)

    def setup():
        """Runs once prior to Run() loop
        """
        raise NotImplementedError()

    def run():
        """runs in a loop continously
        """
        raise NotImplementedError()

    def shutdown():
        """Called when the system shuts down
        """
        raise NotImplementedError()


if __name__=="__main__":
    base_app = BaseApp("base_app")
    print(f"params {base_app.config_params}")
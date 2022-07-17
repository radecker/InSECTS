#!/usr/bin/env python3

import message_pb2
import socket
import threading
import queue
import time


class BaseApp():
    def __init__(self) -> None:
        pass

    def __initialize():
        """Sets up connection and listens for init params from main controller
        """
        pass

    def start_command_listener():
        """Setup connection and start listening for any commands
        """
        pass

    def start_telemetry_listener():
        """Setup connection and start listening for any telemetry
        """
        pass

    def start_tcp_server():
        """Start a TCP server
        """
        pass

    def connect_to_tcp_server():
        """Connect to a TCP Server
        """
        pass

    def setup():
        """Runs once prior to Run() loop
        """
        pass

    def run():
        """runs in a loop continously
        """
        pass

    def shutdown():
        """Called when the system shuts down
        """
        pass
#!/usr/bin/env python3

from TCPClient import TCPClient
from UDPClient import UDPClient
import message_pb2 as proto
import time


if __name__ == "__main__":
    udp_client = UDPClient(id="vehicle.autonomy_app")
    udp_client.add_listener("224.1.1.1", 5050)
    udp_client.add_sender("224.1.1.1", 5050)
    msg = proto.Message()
    while True:
        messages = udp_client.get_messages()
        for msg in messages:
            print(f"Received: {msg}")
            time.sleep(3)
            udp_client.send(msg=msg, group="224.1.1.1", port=5050)
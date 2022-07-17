#!/usr/bin/env python3

from tcp_client import TCPClient
from udp_client import UDPClient
import message_pb2 as proto
import time


if __name__ == "__main__":
    tcp_client = TCPClient(ip="127.0.0.1", port=5052, sender="autonomy")
    tcp_client.start()
    udp_client = UDPClient(id="vehicle.sdr_app")
    udp_client.add_listener("224.1.1.1", 5050)
    udp_client.add_sender("224.1.1.1", 5050)
    msg = proto.Message()
    tcp_client.send(msg=msg, dst="sdr")
    done = False
    while True:
        tcp_messages = tcp_client.get_messages()
        udp_messages = udp_client.get_messages()
        for msg in tcp_messages:
            print(f"Received TCP: {msg}")
            if not done:
                time.sleep(2)
                tcp_client.send(msg=msg, dst="gui")
                udp_client.send(msg=msg, group="224.1.1.1", port=5050)
                done = True
        for msg in udp_messages:
            print(f"Received UDP: {msg}")
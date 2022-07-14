#!/usr/bin/env python3

# External Dependencies
import RPi.GPIO as GPIO
import serial

import messages_pb2

import socket 
import threading


HEADER = 64
PORT = 5051
SERVER = "127.0.0.1"    # socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER_FORMAT = 'utf-8'
dmsg = messages_pb2.Message()
dmsg.disconnect = True
DISCONNECT_MESSAGE = dmsg

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(HEADER_FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            data = conn.recv(msg_length)
            msg = messages_pb2.Message()
            msg.ParseFromString(data)
            # msg = conn.recv(msg_length).decode(HEADER_FORMAT)
            if msg.disconnect:
                connected = False

            print(f"[{addr}]:\n{msg}")
            conn.send("Msg received".encode(HEADER_FORMAT))

    conn.close()
        

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()

import messages_pb2
import socket

HEADER = 64
PORT = 5051
HEADER_FORMAT = 'utf-8'
dmsg = messages_pb2.Message()
dmsg.disconnect = True
DISCONNECT_MESSAGE = dmsg
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    data = msg.SerializeToString()
    msg_length = len(data)
    send_length = str(msg_length).encode(HEADER_FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(data)
    print(client.recv(2048).decode(HEADER_FORMAT))


msg = messages_pb2.Message()
msg.sender = "Ryan Decker"
msg.destination = "The World"
send(msg)

send(DISCONNECT_MESSAGE)
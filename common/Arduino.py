import time
import serial
import threading
import message_pb2 as proto

class Arduino():
    def __init__(self, port: str, baudrate: int) -> None:
        self.port = port
        self.baudrate = baudrate
        self.conn = None
        self.messages = []
        self.__connect()

    def translate_proto_to_serial(self, msg: proto.Message) -> str:
        # All serial commands are csv format (cmd type, val1, val2..., val n)
        # This function needs to be carefully maintained until a better method is implemented
        if msg.HasField("command"):
            if msg.command.HasField("set_servo_position"):
                return f"1, {msg.command.set_servo_position.servo_pos}"
            if msg.command.HasField("set_fan_speed"):
                return f"2, {msg.command.set_fan_speed.fan_speed}"
            if msg.command.HasField("set_fan_state"):
                return f"3, {int(msg.command.set_fan_state.fan_state)}"
            if msg.command.HasField("set_autonomy_state"):
                return f"4, {int(msg.command.set_autonomy_state.autonomy_state)}"
        if msg.HasField("telemetry"):
            pass
        return None


    def __connect(self) -> None:
        self.conn = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=1)
        time.sleep(2)
        receiver = threading.Thread(target=self.__receive)
        receiver.start()

    def send_msg(self, msg: proto.Message) -> None:
        buf = self.translate_proto_to_serial(msg)
        if buf is not None:
            self.conn.write(bytes(buf, 'utf-8'))

    def __receive(self):
        while True:
            while self.conn.in_waiting:
                data = self.conn.readline()
                self.messages.append(data)
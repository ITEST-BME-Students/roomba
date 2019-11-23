from pycreate2 import Create2
from library import Ports
import serial
import time

class MyRoomba:
    def __init__(self, port=None):
        if port is None: port = Ports.get_port('FT231X')
        self.port = serial.Serial(port, baudrate=115200)
        print(port)
        self.port.write(128)
        time.sleep(5)
        self.port.write(142)
        self.port.write(100)
        time.sleep(0.1)
        a = self.port.read_all()
        print(a)




if __name__ == "__main__":
    import time
    roomba = MyRoomba()


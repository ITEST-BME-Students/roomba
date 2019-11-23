from pycreate2 import Create2
from library import Ports

class MyRoomba:
    def __init__(self, port=None):
        if port is None: port = Ports.get_port('FT231X')
        self.robot = Create2(port)
        self.robot.full()

    def set_motors(self, left_speed, right_speed):
        # in mm/s. The order in the api is different
        self.robot.drive_direct(right_speed, left_speed)

    def get_sensors(self):
        sensors = self.robot.get_sensors()
        return sensors





if __name__ == "__main__":
    import time
    roomba = MyRoomba()
    roomba.set_motors(0,0)

    opcode = 142
    cmd = (100,)

    sensor_pkt_len = 80

    roomba.robot.SCI.write(opcode, cmd)
    time.sleep(15)  # wait 15 msec
    packet_byte_data = roomba.robot.SCI.read(sensor_pkt_len)
    #sensors = SensorPacketDecoder(packet_byte_data)

    #return sensors






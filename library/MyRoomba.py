from pycreate2 import Create2
from library import Ports


class MyRoomba:
    def __init__(self, port=None):
        if port is None: port = Ports.get_port('FT231X')
        self.robot = Create2(port)
        self.robot.start()
        self.robot.full()

    def set_motors(self, left_speed, right_speed):
        if left_speed > 1: left_speed

        # in mm/s. The order in the api is different
        self.robot.drive_direct(right_speed, left_speed)

    def set_display(self, text):
        text = str(text)
        text = text[0:4]
        text = text.ljust(4,' ')
        self.robot.digit_led_ascii(text)

    def get_sensors(self):
        sensors = self.robot.get_sensors()
        sensors = sensors._asdict()
        sensors = dict(sensors)
        return sensors


if __name__ == "__main__":
    import time
    roomba = MyRoomba()
    roomba.set_motors(0,0)
    roomba.set_display(123)
    s = roomba.get_sensors()



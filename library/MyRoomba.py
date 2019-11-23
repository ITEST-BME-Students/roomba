from pycreate2 import Create2
from library import Ports
from library import Misc
import json


class MyRoomba:
    def __init__(self, port=None):
        if port is None: port = Ports.get_port('FT231X')
        self.robot = Create2(port)
        self.robot.start()
        self.robot.safe()

    def set_motors(self, left_speed, right_speed):
        left_speed = Misc.constrain(left_speed, -1, 1) * 500
        right_speed = Misc.constrain(right_speed, -1, 1) * 500
        left_speed = round(left_speed)
        right_speed = round(right_speed)
        # in mm/s. The order in the api is different
        self.robot.drive_direct(right_speed, left_speed)

    def set_display(self, text):
        text = str(text)
        text = text[0:4]
        text = text.ljust(4, ' ')
        self.robot.digit_led_ascii(text)

    def get_sensors(self):
        sensors = self.robot.get_sensors()
        sensors = sensors._asdict()
        sensors = dict(sensors)
        return sensors

    def set_leds(self, leds, color=0, intensity=0):
        # check, dock, spot, debris
        string_value = str(leds[0]) + str(leds[1]) + str(leds[2]) + str(leds[3])
        decimal = int(string_value, 2)
        self.robot.led(led_bits=decimal, power_color=color, power_intensity=intensity)

    def handle_roomba_text_command(self, txt):
        txt = txt.replace(' ', '')
        parts = txt.split(',')
        command = parts[0]
        command = command.upper()
        # MOTOR COMMAND
        if command == 'M':
            left = float(parts[1])
            right = float(parts[2])
            self.set_motors(left, right)
            return 'motors set'
        # SENSOR DATA
        if command == 'S':
            data = self.get_sensors()
            data = json.dumps(data)  # reading at the other side: json.loads(a)
            return data
        # SET DISPLAY
        if command == 'D':
            self.set_display(parts[1])
            return 'display set'

if __name__ == "__main__":
    roomba = MyRoomba()
    roomba.handle_roomba_text_command('M,0,0')

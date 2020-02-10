from pycreate2 import Create2
from . import Ports
from . import Misc
import json


class MyRoomba:
    def __init__(self, port=None):
        if port is None: port = Ports.get_port('FT231X')
        self.robot = Create2(port)
        self.robot.start()
        self.robot.safe()
        self.max_speed = 250

    def set_motors(self, left_speed, right_speed):
        left_speed = Misc.constrain(left_speed, -self.max_speed, self.max_speed)
        right_speed = Misc.constrain(right_speed, -self.max_speed, self.max_speed)
        left_speed = round(left_speed)
        right_speed = round(right_speed)
        # in mm/s. The order in the api is different
        self.robot.drive_direct(right_speed, left_speed)

    def move(self, distance):  # in mm
        # the robot command accepts distances in meters, so we need to convert
        meter = distance / 1000
        self.robot.drive_distance(meter, 100, True)

    def turn(self, degrees):
        self.turn_angle_alternative(degrees, 100)

    def set_display(self, text):
        text = str(text)
        text = text[0:4]
        text = text.ljust(4, ' ')
        self.robot.digit_led_ascii(text)

    def get_roomba_sensors(self):
        sensors = self.robot.get_sensors()
        sensors = sensors._asdict()
        sensors = dict(sensors)
        return sensors

    def set_leds(self, leds, color=0, intensity=0):
        # leds is a string of 0's and 1's indicating withch LEDS to switch on.
        # Order of leds: check, dock, spot, debris

        string_value = str(leds[0]) + str(leds[1]) + str(leds[2]) + str(leds[3])
        decimal = int(string_value, 2)
        self.robot.led(led_bits=decimal, power_color=color, power_intensity=intensity)

    def turn_angle_alternative(self, angle, speed):
        # This function is a reimplementation of the turn angle function in the icreate2 package
        # The problem with the original function was that it did not stop the robot when done turning
        # I did not want to edit the original function to avoid having to edit things every time I install the package from the web

        turn_angle = 0.0
        if angle > 0:
            cmd = (speed, -speed)  # R, L
        else:
            cmd = (-speed, speed)
            angle = -angle

        while abs(turn_angle) < angle:
            self.robot.drive_direct(*cmd)
            sensors = self.robot.get_sensors()
            turn_angle += sensors.angle  # roomba only tracks the delta angle
        self.robot.drive_direct(0, 0)

    def handle_roomba_text_command(self, txt):
        txt = txt.replace(' ', '')
        parts = txt.split(',')
        command = parts[0]
        command = command.upper()
        # MOTOR COMMAND
        if command == 'MT':
            left = float(parts[1])
            right = float(parts[2])
            self.set_motors(left, right)
            return 'motors set'
        # SENSOR DATA
        if command == 'SD':
            data = self.get_roomba_sensors()
            data = json.dumps(data)  # reading at the other side: json.loads(a)
            return data
        # SET DISPLAY
        if command == 'DP':
            self.set_display(parts[1])
            return 'display set'
        # MOVE DISTANCE
        if command == 'MD':
            distance = int(parts[1])
            self.move(distance)
            return 'moved'
        # TURN DEGREES
        if command == 'TD':
            degrees = int(parts[1])
            self.turn(degrees)
            return 'turned'



if __name__ == "__main__":
    roomba = MyRoomba()
    result = roomba.robot.reset()
    print(result)

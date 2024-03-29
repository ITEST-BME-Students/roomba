from Roomba.pycreate2 import Create2
from Roomba import Ports
from Roomba import Misc
from Roomba import Kinematics
from itertools import tee


def get_bumper_data(sensor_data):
    a = sensor_data['light_bumper_left']
    b = sensor_data['light_bumper_front_left']
    c = sensor_data['light_bumper_center_left']
    d = sensor_data['light_bumper_center_right']
    e = sensor_data['light_bumper_front_right']
    f = sensor_data['light_bumper_right']
    analog_data = [a, b, c, d, e, f]
    return analog_data


def preprocess_song(song):
    new_song = []
    n = len(song)
    if n % 2 == 1: raise Exception('Songs must consist of pairs of notes and durations. You passed %i values.' % n)
    notes = song[0::2]
    durations = song[1::2]
    for note, duration in zip(notes, durations):
        duration64 = round(duration * 64)
        new_song.append(note)
        new_song.append(duration64)
    return new_song


class Roomba:
    def __init__(self, port=None):
        if port is None: port = Ports.get_port('FT231X')
        self.robot = Create2(port)
        self.robot.start()
        self.robot.safe()
        self.max_speed = 250

    def reset(self):
        self.robot.reset()

    def set_motors(self, left_speed, right_speed):
        left_speed = Misc.constrain(left_speed, -self.max_speed, self.max_speed)
        right_speed = Misc.constrain(right_speed, -self.max_speed, self.max_speed)
        left_speed = round(left_speed)
        right_speed = round(right_speed)
        # in mm/s. The order in the api is different
        self.robot.drive_direct(right_speed, left_speed)

    def stop(self):
        self.set_motors(0, 0)

    def kinematic(self, lin_speed=0, rot_speed=0):
        rot_speed = rot_speed * -1
        left, right, _, _ = Kinematics.kinematics(lin_speed, rot_speed)
        self.set_motors(left, right)

    def move(self, distance, speed=100):  # in mm
        # the robot command accepts distances in meters, so we need to convert
        meter = distance / 1000
        self.robot.drive_distance(meter, speed, True)

    def turn(self, degrees, speed=100):
        degrees = degrees * -1
        self.robot.turn_angle(degrees, speed)

    def set_display(self, text):
        text = str(text)
        if len(text) == 0: text = ' '
        text = text[0:4]
        text = text.ljust(4, ' ')
        self.robot.digit_led_ascii(text)

    def get_sensors(self):
        sensors = self.robot.get_sensors()
        sensors = sensors._asdict()
        sensors = dict(sensors)
        return sensors

    def get_bumpers(self):
        data = self.get_sensors()
        bumpers = get_bumper_data(data)
        return bumpers

    def set_leds(self, leds, color=0, intensity=0):
        # leds is a string of 0's and 1's indicating withch LEDS to switch on.
        # Order of leds: check, dock, spot, debris

        string_value = str(leds[0]) + str(leds[1]) + str(leds[2]) + str(leds[3])
        decimal = int(string_value, 2)
        self.robot.led(led_bits=decimal, power_color=color, power_intensity=intensity)

    def play_song(self, song):
        song = preprocess_song(song)
        self.robot.createSong(0, song)
        self.robot.playSong(0)


if __name__ == "__main__":
    import time
    import Whiskers

    roomba = Roomba()
    roomba.set_display('sd')
    w = Whiskers.Whiskers()
    w.feel(plot=True)

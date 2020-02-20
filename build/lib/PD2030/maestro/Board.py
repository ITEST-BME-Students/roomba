from .Device import BoardDevice
from . import Util
import time
import numpy


class Board(BoardDevice):
    """
    This class is used to communicate with the maestro-based board

    For student use: Yes

    :param ser_port: The port used for serial communication. If omitted, the code will try to find the port.
    :param verbose: Boolean.
    """
    def __init__(self, ser_port=None, verbose=True):
        self.servo1 = 0
        self.servo2 = 1
        self.led1 = 2
        self.led2 = 3
        self.pot = 4
        self.photo = 5

        self.photo_min = 30
        self.photo_max = 210

        self.pot_min = 0.25
        self.pot_max = 234

        self.min_servo = 544
        self.zero_servo = 1500
        self.max_servo = 2400
        self.offset_servo = -150
        BoardDevice.__init__(self, ser_port, verbose)
        self.set_speeds([0, 0]) #0 is max speed

    def test_connection(self):
        try:
            self.get_photo()
            self.get_dial()
            self.set_led1(True)
            self.set_led2(True)
            time.sleep(0.25)
            self.set_led1(False)
            self.set_led2(False)
            return True
        except:
            return False

    def get_photo(self):
        """ Gets the normalized level of the photocell.

        :return: float
            Level of the photocell in the range [0, 1].
        """
        photo = self.device.get_position(self.photo)
        photo = Util.normalize(photo, self.photo_min, self.photo_max)
        return photo

    def set_speeds(self, speeds):
        channels = [0, 1, 2, 3, 4, 5]
        speeds = [speeds[0], speeds[1], 0, 0, 0, 0]
        self.device.set_speeds(channels, speeds)

    def get_dial(self):
        """Get the normalized level of the potentiometer.

        :return: float
            Level of the potentiometer in the range [0, 1].
        """
        pot = self.device.get_position(self.pot)
        pot = 1 - Util.normalize(pot, self.pot_min, self.pot_max)
        return pot

    def set_servo(self, nr, target, raw):
        new = raw
        if not raw:
            new = numpy.interp(target, [0, 0.5, 1], [self.min_servo, self.zero_servo + self.offset_servo, self.max_servo])
        self.device.set_target(nr, int(new))

    def set_led(self, nr, value):
        if value: new = self.max_servo
        if not value: new = self.min_servo
        result = self.device.set_target(nr, new)
        return result

    def set_leds(self, l1, l2):
        """Shortcut to set both LEDs at the same time.

        :param l1: State of LED 1
        :type l1: Bool
        :param l2: State of LED 2
        :type l2: Bool
        :return: None
        """
        result1 = self.set_led1(l1)
        result2 = self.set_led2(l2)
        return result1, result2

    def set_servo1(self, position, raw=False):
        """ Set the position of servo 1.

        :param position: Normalized target position [0, 1] for the servo.
        :type position: Float
        :param raw: If true, position is given in steps.
        :type raw: Bool
        :return: None
        """
        self.set_servo(self.servo1, position, raw)

    def set_servo2(self, target, raw=False):
        """ Set the position of servo 2.
        """
        self.set_servo(self.servo2, target, raw)

    def set_led1(self, value):
        """Set state of LED 1.

        :param value: State of LED 1.
        :type value: Bool
        :return: None
        """
        result = self.set_led(self.led1, value)
        return result

    def set_led2(self, value):
        """Set state of LED 2."""
        result = self.set_led(self.led2, value)
        return result

    def stop_all(self):
        """Set all motors to a neutral position and switch of both LEDs.

        :return: None
        """
        self.set_servo1(0.5)
        self.set_servo2(0.5)
        self.set_led1(False)
        self.set_led2(False)

    def calibrate_channel(self, channel, n=10):
        mx = 0
        mn = 1000
        for x in range(0, n):
            time.sleep(1)
            print('.', end='')
            value = self.device.get_position(channel)
            if value > mx: mx = value
            if value < mn: mn = value
        print()
        return mn, mx

    def calibrate_photo(self):
        """ Function to calibrate the photocell. A number of measurements will be taken. The recorded minimum and 
        maximum values are used to normalize subsequent measurements.

        :return: Minimum and maximum value.
        """
        print('Calibrating photocell', end='')
        mn, mx = self.calibrate_channel(self.photo, 5)
        self.photo_min = mn
        self.photo_max = mx
        return mn, mx

    def calibrate_pot(self):
        """ Function to calibrate the potentiometer. A number of measurements will be taken. The recorded minimum and 
        maximum values are used to normalize subsequent measurements.

        :return: Minimum and maximum value.
        """
        print('Calibrating pot', end='')
        mn, mx = self.calibrate_channel(self.pot, 10)
        self.pot_min = mn
        self.pot_max = mx
        return mn, mx

# -*- coding: utf-8 -*-
# @Author: liu
# @Date:   2019-11-18 18:15:31
# @Last Modified by:   liu2z2
# @Last Modified time: 2019-12-04 14:25:16

import adafruit_amg88xx
import board
import busio
import gpiozero

from library import SensorDefinitions


class ThermalCamera:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.amg = adafruit_amg88xx.AMG88XX(i2c)

    def get_data(self):
        pixels = self.amg.pixels
        return pixels


class SonarSensors:
    def __init__(self):
        self.max_distance = 3
        self.echo_pin1 = SensorDefinitions.echo_pin1
        self.trigger_pin1 = SensorDefinitions.trigger_pin1
        self.echo_pin2 = SensorDefinitions.echo_pin2
        self.trigger_pin2 = SensorDefinitions.trigger_pin2
        # The distancesensor class has some coode that avoids interference between multiple sensors
        self.sonar1 = gpiozero.DistanceSensor(echo=self.echo_pin1, trigger=self.trigger_pin1, max_distance=self.max_distance)
        self.sonar2 = gpiozero.DistanceSensor(echo=self.echo_pin2, trigger=self.trigger_pin2, max_distance=self.max_distance)

    def get_data(self):
        d1 = self.sonar1.distance
        d2 = self.sonar2.distance
        return [d1, d2]

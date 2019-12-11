# -*- coding: utf-8 -*-
# @Author: liu
# @Date:   2019-11-18 18:15:31
# @Last Modified by:   liu2z2
# @Last Modified time: 2019-12-04 14:25:16

import adafruit_amg88xx
import board
import busio



class ThermalCamera:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.amg = adafruit_amg88xx.AMG88XX(i2c)

    def get_data(self):
        pixels = self.amg.pixels
        return pixels


class SonarSensors:
    def __init__(self):
        pin1 = 0
        pin2 = 0

    def get_data(self):
        return [0, 0]





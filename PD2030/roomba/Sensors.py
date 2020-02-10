# -*- coding: utf-8 -*-
# @Author: liu
# @Date:   2019-11-18 18:15:31
# @Last Modified by:   liu2z2
# @Last Modified time: 2019-12-04 14:25:16

from . import Settings
import adafruit_mlx90640
#import adafruit_amg88xx
import board
import busio
import gpiozero
import time
import copy
import threading

# class ThermalCamera:
#     def __init__(self):
#         i2c = busio.I2C(board.SCL, board.SDA)
#         self.amg = adafruit_amg88xx.AMG88XX(i2c)
#
#     def get_data(self):
#         pixels = self.amg.pixels
#         return pixels


class SonarSensors:
    def __init__(self):
        self.max_distance = 3
        self.echo_pin1 = Settings.echo_pin1
        self.trigger_pin1 = Settings.trigger_pin1
        self.echo_pin2 = Settings.echo_pin2
        self.trigger_pin2 = Settings.trigger_pin2
        # The distancesensor class has some coode that avoids interference between multiple sensors
        self.sonar1 = gpiozero.DistanceSensor(echo=self.echo_pin1, trigger=self.trigger_pin1, max_distance=self.max_distance)
        self.sonar2 = gpiozero.DistanceSensor(echo=self.echo_pin2, trigger=self.trigger_pin2, max_distance=self.max_distance)

    def get_data(self):
        d1 = self.sonar1.distance
        d2 = self.sonar2.distance
        return [d1, d2]


class ThermalCamera:
    def __init__(self):
        self.ic2 = busio.I2C(board.SCL, board.SDA, frequency=400000)
        self.mlx = adafruit_mlx90640.MLX90640(self.ic2)
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ
        self.msg = ("MLX addr detected on I2C", [hex(i) for i in self.mlx.serial_number])
        self.frame = [0] * 768
        self.reading_camera_data = False
        self.returning_data = False

        thread = threading.Thread(target=self.data_acquisition_loop)
        thread.start()

    def data_acquisition_loop(self):
        while True:
            while self.returning_data: time.sleep(0.1)
            self.reading_camera_data = True
            self.mlx.getFrame(self.frame)
            self.frame = list(map(int, self.frame))
            self.reading_camera_data = False
            time.sleep(0.5)

    def get_data(self):
        while self.reading_camera_data: time.sleep(0.1)
        self.returning_data = True
        data = copy.copy(self.frame)
        self.returning_data = False
        return data





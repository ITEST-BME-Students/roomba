import time
import RPi.GPIO as GPIO
import gpiozero

from Roomba import Settings
GPIO.cleanup()

class Sonar:
    def __init__(self, sensors=[1,2]):
        print('Creating sonar')
        self.max_distance = 3
        self.echo_pin1 = Settings.echo_pin1
        self.trigger_pin1 = Settings.trigger_pin1
        self.echo_pin2 = Settings.echo_pin2
        self.trigger_pin2 = Settings.trigger_pin2
        self.echo_pin3 = Settings.echo_pin3
        self.trigger_pin3 = Settings.trigger_pin3
        self.echo_pin4 = Settings.echo_pin4
        self.trigger_pin4 = Settings.trigger_pin4
        time.sleep(1)
        # The distance sensor class has some code that avoids interference between multiple sensors
        self.sensors = sensors

        if 1 in sensors:
            print('Setting up sonar 1', end=' ')
            self.sonar1 = gpiozero.DistanceSensor(echo=self.echo_pin1, trigger=self.trigger_pin1, max_distance=self.max_distance)
            print('Done 1')
            time.sleep(0.5)

        if 2 in sensors:
            print('Setting up sonar 2', end=' ')
            self.sonar2 = gpiozero.DistanceSensor(echo=self.echo_pin2, trigger=self.trigger_pin2, max_distance=self.max_distance)
            print('Done 2')
            time.sleep(0.5)

        if 3 in sensors:
            print('Setting up sonar 3', end=' ')
            self.sonar3 = gpiozero.DistanceSensor(echo=self.echo_pin3, trigger=self.trigger_pin3, max_distance=self.max_distance)
            print('Done 3')
            time.sleep(0.5)

        if 4 in sensors:
            print('Setting up sonar 4', end=' ')
            self.sonar4 = gpiozero.DistanceSensor(echo=self.echo_pin4, trigger=self.trigger_pin4, max_distance=self.max_distance)
            print('Done 4')
            time.sleep(0.5)

    def sensor_distance(self, nr):
        if nr == 1: distance = self.sonar1.distance
        if nr == 2: distance = self.sonar2.distance
        if nr == 3: distance = self.sonar3.distance
        if nr == 4: distance = self.sonar4.distance
        return distance

    def distance(self):
        output = []
        for nr in self.sensors:
            distance = self.sensor_distance(nr)
            output.append(distance)
        return output
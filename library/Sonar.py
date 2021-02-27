import gpiozero

from library import Settings


class Sonar:
    def __init__(self, sensors=[1,2]):
        print('Creating sonar')
        self.max_distance = 3
        self.echo_pin1 = Settings.echo_pin1
        self.trigger_pin1 = Settings.trigger_pin1
        self.echo_pin2 = Settings.echo_pin2
        self.trigger_pin2 = Settings.trigger_pin2
        # The distance sensor class has some code that avoids interference between multiple sensors
        self.sensors = sensors

        if 1 in sensors:
            print('Setting up sonar 1', end=' ')
            self.sonar1 = gpiozero.DistanceSensor(echo=self.echo_pin1, trigger=self.trigger_pin1, max_distance=self.max_distance)
            print('Done 1')

        if 2 in sensors:
            print('Setting up sonar 2', end=' ')
            self.sonar2 = gpiozero.DistanceSensor(echo=self.echo_pin2, trigger=self.trigger_pin2, max_distance=self.max_distance)
            print('Done 2')

    def distance(self, ):
        d1 = self.max_distance
        d2 = self.max_distance
        if 1 in self.sensors: d1 = self.sonar1.distance
        if 2 in self.sensors: d2 = self.sonar2.distance
        return [d1, d2]
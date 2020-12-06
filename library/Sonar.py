import gpiozero

from library import Settings


class Sonar:
    def __init__(self):
        self.max_distance = 3
        self.echo_pin1 = Settings.echo_pin1
        self.trigger_pin1 = Settings.trigger_pin1
        self.echo_pin2 = Settings.echo_pin2
        self.trigger_pin2 = Settings.trigger_pin2
        # The distance sensor class has some code that avoids interference between multiple sensors
        self.sonar1 = gpiozero.DistanceSensor(echo=self.echo_pin1, trigger=self.trigger_pin1, max_distance=self.max_distance)
        self.sonar2 = gpiozero.DistanceSensor(echo=self.echo_pin2, trigger=self.trigger_pin2, max_distance=self.max_distance)

    def get_data(self):
        d1 = self.sonar1.distance
        d2 = self.sonar2.distance
        return [d1, d2]
from Roomba import Settings
from matplotlib import pyplot
from Roomba import Analog


class Whiskers:
    def __init__(self, sensors=[1, 2]):
        self.sensors = sensors
        self.adc = Analog.myAnalog()

    def feel(self, plot=False):
        channels = Settings.whisker_channels
        values = []
        for whisker_nr in self.sensors:
            channel = channels[whisker_nr - 1]
            value = self.adc.get_value(channel=channel)
            values.append(value)

        if plot:
            n = len(channels)
            pyplot.bar(range(n), values)
            pyplot.title('whisker values')
            pyplot.show()

        return values

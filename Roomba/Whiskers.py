from Roomba import Settings
from matplotlib import pyplot
from Roomba import Analog

class Whiskers:
    def __init__(self):
        #todo: update the analog channels and allow for 4 whiskers, as provided on the board
        self.adc = Analog.myAnalog()

    def feel(self, plot=False):
        channels = Settings.whisker_channels
        values = []
        for channel in channels:
            value = self.adc.get_value(channel=channel)
            values.append(value)

        if plot:
            n = len(channels)
            pyplot.bar(range(n), values)
            pyplot.title('whisker values')
            pyplot.show()

        return values

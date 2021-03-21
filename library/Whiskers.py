from grove import adc_8chan_12bit
from library import Settings
from matplotlib import pyplot


class Whiskers:
    def __init__(self):
        self.adc = adc_8chan_12bit.Pi_hat_adc()

    def feel(self, plot=False):
        channels = Settings.whisker_channels
        n = len(channels)
        data = self.adc.get_all_ratio_0_1_data()
        values = []
        for channel in channels:
            value = data[channel] / 1000
            values.append(value)

        if plot:
            pyplot.bar(range(n), values)
            pyplot.title('whisker values')
            pyplot.xlim([-0.5, n - 0.5])
            pyplot.show()

        return values

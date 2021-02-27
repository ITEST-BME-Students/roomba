from grove import adc_8chan_12bit
from library import Settings
from matplotlib import pyplot

class Whiskers:
    def __init__(self):
        self.adc = adc_8chan_12bit.Pi_hat_adc()

    def feel(self, plot=False):
        channels = Settings.whisker_channels
        data = self.adc.get_all_ratio_0_1_data()
        w1 = data[channels[0]] / 1000
        w2 = data[channels[1]] / 1000

        if plot:
            pyplot.bar([0, 1], [w1, w2])
            pyplot.title('whisker values')
            pyplot.ylim([0, 1])
            pyplot.show()

        return w1, w2

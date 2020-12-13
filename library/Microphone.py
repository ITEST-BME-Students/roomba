# import pyaudio
import numpy
import sounddevice
from matplotlib import pyplot
from library import Settings
from scipy.signal import correlate, butter, lfilter
from scipy.signal.windows import hamming

sounddevice.default.channels = 2
sounddevice.default.dtype = 'int16'


def make_frequency_bands():
    bands = []
    width = Settings.microphone_band_width
    a = Settings.microphone_band_centers[0]
    b = Settings.microphone_band_centers[1]
    c = Settings.microphone_band_centers[2]
    centers = numpy.linspace(a, b, c)
    for center in centers:
        low = int(center - width / 2)
        high = int(center + width / 2)
        if low < 200: low = 200
        bands.append([low, high])
    return bands


def my_fft(signal):
    spectrum = numpy.fft.fft(signal)
    spectrum = numpy.abs(spectrum)
    frequencies = numpy.fft.fftfreq(signal.size, 1 / 44100)
    selected = frequencies > 0
    spectrum = spectrum[selected]
    frequencies = frequencies[selected]
    return spectrum, frequencies


def my_fft_binaural(data):
    channel0, f0 = my_fft(data[0, :])
    channel1, _ = my_fft(data[1, :])
    return channel0, channel1, f0


def loudness(channel0, channel1, freq, band):
    low = band[0]
    high = band[1]
    selected = (freq > low) * (freq < high)
    value0 = numpy.mean(numpy.abs(channel0[selected])) / 100
    value1 = numpy.mean(numpy.abs(channel1[selected])) / 100
    return value0, value1


def signal_ramp(n, percent):
    if percent > 49: percent = 49
    length = int(numpy.floor((n * percent) / 100))
    window = hamming(length * 2 + 1)
    window = window - numpy.min(window)
    window = window / numpy.max(window)
    left = window[0:length + 1]
    right = window[length:]
    buffer = numpy.ones(n - 2 * left.size)
    total = numpy.hstack((left, buffer, right))
    return total


class LagDetector:
    def __init__(self, lowcut, highcut, fs=44100, order=3):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        self.b, self.a = butter(order, [low, high], btype='band')

    def run_channel(self, signal):
        y = lfilter(self.b, self.a, signal)
        return y

    def find_lag(self, data):
        n = data.shape[1]
        ramp = signal_ramp(n, 10)
        y1 = data[0, :] * ramp
        y2 = data[1, :] * ramp
        y1 = self.run_channel(y1)
        y2 = self.run_channel(y2)
        y1 = y1 / numpy.max(y1)
        y2 = y2 / numpy.max(y2)
        corr = correlate(y1, y2, mode='same')  # left leading = negative value
        delay_arr = numpy.linspace(-0.5 * n, 0.5 * n, n)
        delay = delay_arr[numpy.argmax(corr)]
        return delay, y1, y2

# Distance between mic is 8 cm, or 0.235 ms.
# 8 cm wavelength == 4287.5 Hz
# At 0.235 ms diff and 44100 fs, max lag in samples is 10.36

class Microphone:
    def __init__(self, duration=0.5, fs=44100):
        self.duration = duration
        self.sample_rate = fs
        self.bands = make_frequency_bands()
        self.lag_detector = LagDetector(200, 4000, fs=fs)

    def get_data(self, plot=False):
        samples = int(self.sample_rate * self.duration)
        fs = self.sample_rate
        data = sounddevice.rec(samples, samplerate=fs, blocking=True)
        data = data.transpose()
        data = numpy.flipud(data)  # To make left channel, channel 0
        if plot:
            pyplot.plot(data[0, :])
            pyplot.plot(data[1, :])
            pyplot.legend(['Left', 'Right'])
            pyplot.show()
        return data

    def listen(self, plot=False):
        data = self.get_data()
        values0 = []
        values1 = []
        channel0, channel1, freq = my_fft_binaural(data)
        for band in self.bands:
            v0, v1 = loudness(channel0, channel1, freq, band)
            values0.append(v0)
            values1.append(v1)
        lag, y1, y2 = self.lag_detector.find_lag(data)

        if plot:
            pyplot.subplot(2, 1, 1)
            pyplot.plot(values0)
            pyplot.plot(values1)
            pyplot.legend(['Left', 'Right'])
            pyplot.subplot(2, 1, 2)
            pyplot.plot(y1, alpha=0.25)
            pyplot.plot(y2, alpha=0.25)
            pyplot.legend(['Left', 'Right'])
            pyplot.show()

        values0 = numpy.array(values0)
        values1 = numpy.array(values1)
        values0 = numpy.round(values0)
        values1 = numpy.round(values1)
        return values0, values1, lag

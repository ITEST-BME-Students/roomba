# import pyaudio
import numpy
import sounddevice
from matplotlib import pyplot
from library import Settings
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


class Microphone:
    def __init__(self, duration=0.5, fs=44100):
        self.duration = duration
        self.sample_rate = fs
        self.bands = make_frequency_bands()

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
        if plot:
            pyplot.plot(values0)
            pyplot.plot(values1)
            pyplot.legend(['Left', 'Right'])
            pyplot.show()
        values0 = numpy.array(values0)
        values1 = numpy.array(values1)
        values0 = numpy.round(values0)
        values1 = numpy.round(values1)
        return values0, values1

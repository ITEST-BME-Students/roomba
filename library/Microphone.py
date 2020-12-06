import pyaudio
import wave
import numpy
from matplotlib import pyplot

freq_bands = [[100, 200], [200, 600], [600, 1400], [1400, 3200], [3200, 6800]]


def my_fft(signal):
    spectrum = numpy.fft.fft(signal, norm='ortho')
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
    value0 = numpy.mean(numpy.abs(channel0[selected]))
    value1 = numpy.mean(numpy.abs(channel1[selected]))
    return value0, value1


def get_devices():
    devices = []
    p = pyaudio.PyAudio()
    n = p.get_device_count()
    for i in range(n):
        device = p.get_device_info_by_index(i)
        devices.append(device)
    p.terminate()
    return devices


class SoundSensor:
    def __init__(self, device_index=0, chunk=22050):
        self.chunk = chunk
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=2,
            rate=44100,
            input=True,
            frames_per_buffer=chunk,
            input_device_index=device_index)
        self.stream.stop_stream()

    def get_data(self, plot=False):
        self.stream.start_stream()
        data = self.stream.read(self.chunk)
        self.stream.stop_stream()
        data = numpy.frombuffer(data, dtype=numpy.int16)
        data = data.reshape((self.chunk, 2))
        data = data.transpose()
        data = numpy.flipud(data)  # to make channel 0 the left one
        if plot:
            pyplot.plot(data.transpose())
            pyplot.show()
        return data

    def listen(self, plot=False):
        data = self.get_data()
        values0 = []
        values1 = []
        channel0, channel1, freq = my_fft_binaural(data)
        for band in freq_bands:
            v0, v1 = loudness(channel0, channel1, freq, band)
            values0.append(v0)
            values1.append(v1)
        if plot:
            pyplot.plot(values0)
            pyplot.plot(values1)
            pyplot.legend(['Left', 'Right'])
            pyplot.show()
        return values0, values1

    def __del__(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

from library import Microphone
#
# devices = Microphone.get_devices()
# print(devices)
# from matplotlib import pyplot
# import sounddevice
# sounddevice.default.samplerate = 44100
# sounddevice.default.channels = 2
# sounddevice.default.device = 0
#
# myrecording = sounddevice.rec(int(2 * 44100), blocking=True)
# pyplot.plot(myrecording)
# pyplot.show()

s = Microphone.SoundSensor()
s.get_data(plot=True)
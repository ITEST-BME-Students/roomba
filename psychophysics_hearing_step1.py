from library import Microphone
import time
import numpy
microphone = Microphone.Microphone()

while True:
    data = microphone.get_data(plot=True)
    mx = numpy.max(numpy.abs(data))
    print('max. value:', mx)
    time.sleep(0.25)
from matplotlib import pyplot

from library import Roomba
from library import Microphone
from library import Camera
from library import Device
from library import Thermal
from library import Sonar
#from grove import adc_8chan_12bit

mic = Microphone.Microphone()
snr = Sonar.Sonar(sensors=[1, 2])
thr = Thermal.Thermal()
cam = Camera.Camera()

thermal_data = thr.get_data(plot=True)
#visual_data = cam.get_data(plot=True)
#dist = snr.distance()
#print(dist)
#hat = adc_8chan_12bit.Pi_hat_adc()



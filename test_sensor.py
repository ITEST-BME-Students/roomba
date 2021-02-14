from matplotlib import pyplot

from library import Roomba
from library import Microphone
from library import Camera
from library import Device
from library import Thermal
from library import Sonar

mic = Microphone.Microphone()
snr = Sonar.Sonar(sensors=[1])
thr = Thermal.Thermal()
cam = Camera.Camera()

thermal_data = thr.get_data()
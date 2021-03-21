from matplotlib import pyplot

from library import Roomba
from library import Microphone
from library import Camera
from library import Device
from library import Thermal
from library import Sonar
from library import Whiskers


micrphone = Microphone.Microphone()
#snr = Sonar.Sonar(sensors=[1, 2])
thermal = Thermal.Thermal()
camera = Camera.Camera()
whiskers = Whiskers.Whiskers()


#thermal_data = thermal.get_data(plot=True)
visual_data = camera.get_data(plot=True)
whiskers.feel(plot=True)
thermal.get_data(plot=True)


from matplotlib import pyplot

from Roomba import Roomba
from Roomba import Microphone
from Roomba import Camera
from Roomba import Device
from Roomba import Thermal
from Roomba import Sonar
from Roomba import Whiskers


micrphone = Microphone.Microphone()
#snr = Sonar.Sonar(sensors=[1, 2])
thermal = Thermal.Thermal()
camera = Camera.Camera()
whiskers = Whiskers.Whiskers()


#thermal_data = thermal.get_data(plot=True)
visual_data = camera.get_data(plot=True)
whiskers.feel(plot=True)
thermal.get_data(plot=True)


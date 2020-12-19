import numpy
import math
from library import Roomba
from library import Microphone
from library import Camera
from library import Thermal
r = Roomba.Roomba()

#sensor = Camera.Camera()
sensor = Thermal.Thermal()

sensor.get_data(plot=True)

#%%
while True:
    sensor_data = sensor.look()
    n = len(sensor_data)
    n = math.floor(n/2)
    max_index = numpy.argmax(sensor_data)
    print(sensor_data, max_index, n)
    if max_index < n: r.turn(-6)
    if max_index > n: r.turn(+6)
sensor.get_data(plot=True)

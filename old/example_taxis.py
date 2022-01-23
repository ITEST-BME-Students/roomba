import numpy
import math
from Roomba import Roomba
from Roomba import Camera
my_robot = Roomba.Roomba()

sensor = Camera.Camera()
sensor.get_data(plot=True)

#%%
while True:
    sensor_data = sensor.look()
    red = sensor_data[:, 0]
    n = len(red)
    middle = math.floor(n/2)
    max_index = numpy.argmax(red)
    print(red, max_index, n)
    if max_index < n: my_robot.turn(-10)
    if max_index > n: my_robot.turn(+10)


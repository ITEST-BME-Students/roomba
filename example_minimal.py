from PD2030.roomba import Client
import time
from matplotlib import pyplot
import numpy

name = 'ELMER'

robot = Client.Client(name=name, do_upload=True)
robot.start_remote_server()
robot.test_communication(message=['hello'])
data = robot.get_adc()

data = robot.get_thermal_image(plot=True)

mn = numpy.mean(data, axis=0)
left = numpy.mean(mn[0:12])
right = numpy.mean(mn[12:])

pyplot.plot(mn)
pyplot.show()

pyplot.plot([left, right])
pyplot.show()

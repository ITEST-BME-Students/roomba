from library import Roomba
import numpy
from library import Thermal

thermal = Thermal.Thermal()
robot = Roomba.Roomba()

angle_range = numpy.linspace(-50, 50, 11)
steps = numpy.diff(angle_range)

robot.turn(angle_range[0])

counter = 1
for step in steps:
    data = thermal.look(plot=True)
    print('Thermal data %i:' % counter, data)
    robot.turn(step)
    counter = counter + 1



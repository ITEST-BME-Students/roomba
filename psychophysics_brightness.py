from library import Camera
import numpy

camera = Camera.Camera()
data = camera.get_data(plot=True)
data = camera.look(plot=True)
n = data.shape[0]
i = int(numpy.floor(n/2))

red = data[i, 0]
green = data[i, 1]
blue = data[i, 2]
brightness = numpy.mean(data[i, :])

print('Red value', red)
print('Green value', green)
print('Blue value', blue)
print('Brightness value', brightness)

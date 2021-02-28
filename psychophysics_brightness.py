from library import Camera
import numpy

camera = Camera.Camera()
data = camera.look(plot=True)
n = data.shape[0]
i = numpy.floor(n/2)

measurement = data[i, :]
print('Red, Green, Blue:')
print(measurement)

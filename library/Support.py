import math
import numpy
from scipy.interpolate import griddata


def interpolate_thermal_image(data):
    flat = data.flatten()
    points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
    grid_x, grid_y = numpy.mgrid[0:7:32j, 0:7:32j]
    interpolated = griddata(points, flat, (grid_x, grid_y), method='cubic')
    return interpolated

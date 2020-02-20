import numpy
from scipy.interpolate import griddata
from matplotlib import pyplot

# def interpolate_thermal_image(data, plot=False):
#     maximum = 32
#     minimum = 20
#     flat = data.flatten()
#     points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
#     grid_x, grid_y = numpy.mgrid[0:7:32j, 0:7:32j]
#     interpolated = griddata(points, flat, (grid_x, grid_y), method='cubic')
#     interpolated[interpolated < minimum] = minimum
#     interpolated[interpolated > maximum] = maximum
#     if plot:
#         pyplot.matshow(interpolated, cmap='jet', vmin=minimum, vmax=maximum)
#         pyplot.colorbar()
#         pyplot.show()
#     return interpolated


def process_thermal_data(data, plot=False):
    maximum = 32
    minimum = 20

    data = numpy.array(data)
    flat = data.flatten()

    points = []
    indices = numpy.unravel_index(range(data.size), data.shape)
    for (r, c) in zip(indices[0], indices[1]): points.append((r, c))

    grid_x, grid_y = numpy.mgrid[0:32:64j, 0:24:48j]
    interpolated = griddata(points, flat, (grid_x, grid_y), method='cubic')
    interpolated[interpolated < minimum] = minimum
    interpolated[interpolated > maximum] = maximum
    if plot:
        pyplot.matshow(interpolated, cmap='jet', vmin=minimum, vmax=maximum)
        pyplot.colorbar()
        pyplot.show()
    return interpolated



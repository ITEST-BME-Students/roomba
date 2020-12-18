import numpy
import math
import pandas
from PIL import Image
from matplotlib import pyplot

def make3d(array):
    shape = array.shape
    if len(shape) == 2: array = numpy.expand_dims(array, axis=2)
    return array


class Regions:
    def __init__(self, width, height, centers=[]):
        self.width = width
        self.height = height
        self.centers = centers
        self.masks = []

        horizontal_axis = numpy.linspace(-1, 1, width)
        vertical_axis = numpy.linspace(+1, -1, height)
        horizontal, vertical = numpy.meshgrid(horizontal_axis, vertical_axis)
        self.horizontal_grid = horizontal
        self.vertical_grid = vertical
        self.set_centers(centers)

    def plot_grids(self):
        pyplot.matshow(self.horizontal_grid)
        pyplot.colorbar()
        pyplot.title('Horizontal')
        pyplot.show()

        pyplot.matshow(self.vertical_grid)
        pyplot.colorbar()
        pyplot.title('Vertical')
        pyplot.show()

    def create_mask(self, center):
        term1 = (self.horizontal_grid - center[0]) ** 2
        term2 = (self.vertical_grid - center[1]) ** 2
        distance = (term1 + term2) ** 0.5
        mask = 1.0 * (distance < center[2])
        mask[mask == 0] = numpy.nan
        return mask

    def set_centers(self, centers):
        self.centers = centers
        self.masks = []
        for center in self.centers:
            mask = self.create_mask(center)
            self.masks.append(mask)
        return self.masks

    def plot_current_masks(self):
        i = 1
        n = len(self.masks)
        fig_cols = 2
        fig_rows = math.ceil(n / fig_cols)
        for x in self.masks:
            pyplot.subplot(fig_rows, fig_cols, i)
            pyplot.imshow(x)
            pyplot.title(i - 1)
            i = i + 1
        pyplot.tight_layout()
        pyplot.show()

    def get_stats(self, image, as_frame=True):
        results = []
        image = make3d(image)
        layers = image.shape[2]
        for m in self.masks:
            if layers == 1: m = make3d(m)
            if layers == 3: m = numpy.dstack((m, m, m))
            masked = image * m
            result = numpy.nanmean(masked, axis=(0, 1))
            result = numpy.round(result).astype(int)
            result = list(result)
            results.append(result)
        if as_frame: results = pandas.DataFrame(results)
        return results

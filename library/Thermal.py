import adafruit_mlx90640
import board
import busio
import numpy
from library import Settings
from matplotlib import pyplot



class Thermal:
    def __init__(self):
        self.ic2 = busio.I2C(board.SCL, board.SDA, frequency=400000)
        self.mlx = adafruit_mlx90640.MLX90640(self.ic2)
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ
        self.msg = ("MLX addr detected on I2C", [hex(i) for i in self.mlx.serial_number])
        self.frame = [0] * 768

    def get_snapshot(self):
        self.mlx.getFrame(self.frame)
        self.frame = list(map(int, self.frame))
        data = numpy.array(self.frame)
        data = data.reshape((24, 32))
        data = numpy.fliplr(data)
        return data

    def look(self):
        n = Settings.thermal_sections
        snapshot = self.get_snapshot()
        sections = numpy.linspace(0,32, n)
        sections = sections.astype(int)
        result = numpy.zeros((n - 1, 3))
        for i in range(n - 1):
            slice = snapshot[:, sections[i]:sections[i + 1]]
            slice = numpy.max(slice, axis=(0, 1))
            result[i, :] = slice
        if Settings.camera_greyscale: result = numpy.mean(result, axis=1)
        result = numpy.round(result)
        return result



# t = Thermal()
# s = t.get_snapshot()
# pyplot.imshow(s)
# pyplot.show()
#
# x = t.look()
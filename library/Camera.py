import picamera
import time
import numpy
from library import Settings
from matplotlib import pyplot


class Camera:
    def __init__(self):
        self.w = Settings.camera_width
        self.h = Settings.camera_height
        self.camera = picamera.PiCamera(resolution=(self.w, self.h), framerate=30)
        self.camera.iso = Settings.camera_iso
        time.sleep(2)

        # Now fix the values
        self.camera.shutter_speed = Settings.camera_shutter_speed
        self.camera.exposure_mode = 'off'
        g = self.camera.awb_gains
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = g

    def get_data(self, plot=False):
        output = numpy.empty((self.h, self.w, 3), dtype=numpy.uint8)
        self.camera.capture(output, 'rgb')
        if plot:
            pyplot.imshow(output)
            pyplot.show()
        return output

    def look(self, plot=False):
        operation = Settings.camera_operation
        n = Settings.camera_sections
        snapshot = self.get_data()
        sections = numpy.linspace(0, self.w, n)
        sections = sections.astype(int)
        result = numpy.zeros((n - 1, 3))
        for i in range(n - 1):
            slice = snapshot[:, sections[i]:sections[i + 1], :]
            if operation == 'max': slice = numpy.max(slice, axis=(0, 1))
            if operation == 'mean': slice = numpy.mean(slice, axis=(0, 1))
            result[i, :] = slice
        if Settings.camera_greyscale: result = numpy.mean(result, axis=1)
        result = numpy.round(result)
        if plot:
            pyplot.plot(result)
            pyplot.show()
        return result

# c = Camera()
# c.get_section_profiles()

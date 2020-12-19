import picamera
import time
import numpy
from library import Settings
from library import RegionInterest
from matplotlib import pyplot


def YUV2RGB(yuv):
    m = numpy.array([[1.0, 1.0, 1.0],
                  [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                  [1.4019975662231445, -0.7141380310058594, 0.00001542569043522235]])

    rgb = numpy.dot(yuv, m)
    rgb[:, :, 0] -= 179.45477266423404
    rgb[:, :, 1] += 135.45870971679688
    rgb[:, :, 2] -= 226.8183044444304
    return rgb


class Camera:
    def __init__(self):
        self.w = Settings.camera_width
        self.h = Settings.camera_height
        self.centers = Settings.camera_roi
        self.regions = RegionInterest.Regions(width=self.w, height=self.h, centers=self.centers)
        self.camera = None
        self.init_camera()


    def init_camera(self, warm_up=2):
        self.camera = picamera.PiCamera(resolution=(self.w, self.h), framerate=5)
        self.camera.iso = Settings.camera_iso
        # Give the camera some warm-up time
        time.sleep(warm_up)
        # Now fix the values
        self.camera.shutter_speed = Settings.camera_shutter_speed
        self.camera.exposure_mode = 'off'
        g = self.camera.awb_gains
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = g

    def close_camera(self):
        self.camera.close()

    def get_data(self, plot=False):
        output = numpy.empty((self.h, self.w, 3), dtype=numpy.uint8)
        self.camera.capture(output, 'rgb', use_video_port=True)
        if Settings.camera_greyscale: output = numpy.mean(output, axis=2)
        if plot:
            pyplot.imshow(output)
            pyplot.show()
        return output

    def look(self, plot=False):
        snapshot = self.get_data()
        result = self.regions.get_stats(snapshot)
        if plot:
            pyplot.plot(result)
            pyplot.show()
        return result

# c = Camera()
# c.get_section_profiles()

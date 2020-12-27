import picamera
import time
import numpy
from library import Settings
from library import RegionInterest
from matplotlib import pyplot


class Camera:
    def __init__(self):
        self.w = Settings.camera_width
        self.h = Settings.camera_height
        self.centers = Settings.camera_roi
        self.fov = Settings.camera_fov
        self.regions = RegionInterest.Regions(width=self.w, height=self.h, fov=self.fov, centers=self.centers)
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
        if plot:
            pyplot.imshow(output)
            pyplot.show()
        return output

    def look(self, plot=False):
        snapshot = self.get_data()
        result = self.regions.get_stats(snapshot)
        result = numpy.matmul(result, Settings.camera_channel_matrix)
        if plot:
            pyplot.plot(result)
            pyplot.show()
        return result

# c = Camera()
# c.get_section_profiles()

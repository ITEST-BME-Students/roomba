import picamera
import time
import numpy
import copy
from library import Settings
from library import RegionInterest
from matplotlib import pyplot
from fractions import Fraction


class Camera:
    def __init__(self):
        print('Creating video camera')
        self.w = Settings.camera_width
        self.h = Settings.camera_height
        self.centers = Settings.camera_roi
        self.fov = Settings.camera_fov
        self.regions = RegionInterest.Regions(width=self.w, height=self.h, fov=self.fov, centers=self.centers)
        self.camera = None
        self.init_camera()

    def init_camera(self, warm_up=2):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (self.w, self.h)
        self.camera.framerate = Settings.camera_frame_rate
        self.camera.iso = Settings.camera_iso
        self.camera.shutter_speed = 6000000 # slowest possible, the camera adjust aut. to match framerate
        # Give the camera some warm-up time
        time.sleep(warm_up)

    def close_camera(self):
        self.camera.close()

    def get_data(self, plot=False, raw=False):
        output = numpy.empty((self.h, self.w, 3), dtype=numpy.uint8)
        self.camera.capture(output, 'rgb', use_video_port=True)
        if raw: return copy.copy(output * 1)
        output = output.astype('float32')
        output = output * Settings.camera_gain
        output[output > 255] = 255
        if plot:
            pyplot.imshow(output/255)
            pyplot.show()
        return output

    def look(self, plot=False):
        snapshot = self.get_data()
        result = self.regions.get_stats(snapshot)
        result = numpy.matmul(result, Settings.camera_channel_matrix)
        if plot:
            n = result.shape[1]
            for i in range(n): pyplot.plot(result[:, i], Settings.camera_channel_line_specs[i])
            pyplot.legend(Settings.camera_channel_labels)
            pyplot.xlabel('Region number')
            pyplot.ylabel('Intensity')
            pyplot.show()
        return result

# c = Camera()
# c.get_section_profiles()

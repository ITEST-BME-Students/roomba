from library import RegionInterest
import numpy
from fractions import Fraction

variation = 2

# Whiskers
whisker_channels = [0, 1]

# Sonar
trigger_pin1 = 26  # GPOI nr
echo_pin1 = 20  # GPOI nr

trigger_pin2 = 19  # GPOI nr
echo_pin2 = 16  # GPOI nr

# Thermal
thermal_fov = 110  # width of FOV in angles
# Rois is in center center angle h, center angle_v, size in angles
thermal_roi = [[-50, 0, 10],
               [-20, 0, 10],
               [-10, 0, 10],
               [0, 0, 10],
               [10, 0, 10],
               [20, 0, 10],
               [50, 0, 10]]

# Microphone
microphone_band_centers = [500, 20000, 10]  # start, end, n
microphone_bandwidth = 1000
microphone_itd_band = [200, 4000]
if variation == 1: microphone_itd_band = [7000, 10000]

# Camera settings
camera_fov = 160  # width of FOV in angles
camera_width = 160
camera_height = 80
camera_iso = 200  # 400 higher iso increases brightness
camera_frame_rate = Fraction(50, 1)  # frames per second, min = 1/6. Lower frame rate = brighter

if variation == 2:
    camera_iso = 800  # 400 higher iso increases brightness
    camera_frame_rate = Fraction(10, 1)  # frames per second, min = 1/6. Lower frame rate = brighter

camera_gain = 1  # software gain applied after capturing the image
camera_channel_matrix = numpy.eye(3)
camera_channel_labels = ['red', 'green', 'blue']
camera_channel_line_specs = ['o-r', 'o-g', 'o-b']
camera_roi = [[-50, 0, 20],
              [-40, 0, 20],
              [-30, 0, 20],
              [-20, 0, 20],
              [-10, 0, 20],
              [+0, 0, 20],
              [+10, 0, 20],
              [+20, 0, 20],
              [+30, 0, 20],
              [+40, 0, 20],
              [+50, 0, 20]]


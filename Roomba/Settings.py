import numpy
from fractions import Fraction
import board


# Whiskers
whisker_channels = [4, 5, 6, 7]
cs_pin = board.D8

#todo: update the pins + expand to the 4 sensors provided by the board

# Sonar
trigger_pin1 = 26  # GPOI nr
echo_pin1 = 6  # GPOI nr

trigger_pin2 = 16  # GPOI nr
echo_pin2 = 24  # GPOI nr

trigger_pin3 = 27  # GPOI nr
echo_pin3 = 17  # GPOI nr

trigger_pin4 = 22  # GPOI nr
echo_pin4 = 5  # GPOI nr

# Thermal
thermal_fov = 110  # width of FOV in angles
# Rois is in center center angle h, center angle_v, size in angles
thermal_roi = [[-50, 0, 10],
               [-40, 0, 10],
               [-30, 0, 10],
               [-20, 0, 10],
               [-10, 0, 10],
               [0, 0, 10],
               [10, 0, 10],
               [20, 0, 10],
               [30, 0, 10],
               [40, 0, 10],
               [50, 0, 10]]

# Microphone
microphone_iid_bands = [4000, 8000, 20, 1000]  # start, end, n, width
microphone_itd_band = [200, 4000]
#microphone_itd_band = [7000, 10000]

# Camera settings
camera_fov = 160  # width of FOV in angles
camera_width = 160
camera_height = 80
camera_iso = 400  # 400 higher iso increases brightness
camera_frame_rate = Fraction(50, 1)  # frames per second, min = 1/6. Lower frame rate = brighter

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


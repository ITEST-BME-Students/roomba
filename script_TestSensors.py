from Roomba import Camera
from Roomba import Sonar
from Roomba import Thermal
from Roomba import Whiskers
from Roomba import Microphone
import time

#
# Test camera
#

visual_camera = Camera.Camera()
raw = visual_camera.get_data(plot=True)
data = visual_camera.look(plot=True)
visual_camera.regions.plot_current_masks_single_figure()
#
# patch0_red = data[0, 0]
# patch0_green = data[0, 1]
# patch0_blue = data[0, 2]
# #
# # Test sonar
# #
#
# n = 15
# sonar_sensors = Sonar.Sonar(sensors=[1, 2])
# for i in range(n):
#     sonar_ranges = sonar_sensors.distance()
#     print(i, sonar_ranges)
#     time.sleep(1)
#
# #
# # Test Thermal
# #
#
# thermal_camera = Thermal.Thermal()
# thermal_camera.get_data(plot=True)
# thermal_camera.look(plot=True)
# thermal_camera.regions.plot_current_masks_single_figure()
#
# #
# # Test whiskers
# #
#
# n = 100
# whiskers = Whiskers.Whiskers(sensors=[1,2])
# for i in range(n):
#     touch = whiskers.feel()
#     print(touch)
#     time.sleep(0.5)
# #
# # # Test sound
# # #
# #
# # microphone_sensor = Microphone.Microphone()
# # microphone_sensor.listen(plot=True)
#
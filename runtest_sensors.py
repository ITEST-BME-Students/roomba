from Roomba import Camera
from Roomba import Sonar
from Roomba import Thermal
from Roomba import Whiskers
from Roomba import Microphone
import time

test_camera = True
test_sonar = True
test_thermal = True
test_whiskers = True
test_mic = True

#
# Test camera
#
if test_camera:
    visual_camera = Camera.Camera()
    raw = visual_camera.get_data(plot=True)
    data = visual_camera.look(plot=True)
    visual_camera.regions.plot_current_masks_single_figure()


if test_sonar:
    n = 5
    sonar_sensors = Sonar.Sonar(sensors=[1, 2])
    for i in range(n):
        sonar_ranges = sonar_sensors.distance()
        print(i, sonar_ranges)
        time.sleep(1)

if test_thermal:
    thermal_camera = Thermal.Thermal()
    thermal_camera.get_data(plot=True)
    thermal_camera.look(plot=True)
    thermal_camera.regions.plot_current_masks_single_figure()

if test_whiskers:
    n = 10
    whiskers = Whiskers.Whiskers(sensors=[1,2])
    for i in range(n):
        touch = whiskers.feel()
        print(touch)
        time.sleep(0.5)


if test_mic:
    microphone = Microphone.Microphone()
    loudness_difference, time_difference = microphone.listen(plot=True)
    print(loudness_difference)
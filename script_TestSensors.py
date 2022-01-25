from Roomba import Camera
from Roomba import Sonar
from Roomba import Thermal
from Roomba import Whiskers
from Roomba import Analog
from Roomba import Microphone
import time

# Test camera
#c = Camera.Camera()
#c.look(plot=True)


#
# Test sonar
#

n = 1
sonar_data = []
sonar_sensors = Sonar.Sonar()
for i in range(n):
    sonar_ranges = sonar_sensors.distance()
    print(i, sonar_ranges)
    sonar_data.append(sonar_ranges)
    time.sleep(1)

#
# Test Thermal
#

thermal_camera = Thermal.Thermal()
thermal_camera.get_data(plot=True)
thermal_camera.look(plot=True)

#
# Test whiskers
#

analog = Analog.myAnalog()
analog.get_value(channel=0)

whisker_sensor = Whiskers.Whiskers()
whisker_sensor.feel(plot=True)

#
# Test sound
#

microphone_sensor = Microphone.Microphone()
microphone_sensor.listen(plot=True)


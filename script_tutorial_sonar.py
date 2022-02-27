from Roomba import Sonar
from Roomba import Roomba
import time

robot = Roomba.Roomba()
sonar_sensors = Sonar.Sonar()

while True:
    distances = sonar_sensors.distance()
    print(distances)
    time.sleep(0.5)

    left = distances[0]
    right = distances[1]

    if left < right:
        robot.kinematic(rot_speed=20)
    else:
        robot.kinematic(rot_speed=-20)



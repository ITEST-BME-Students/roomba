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
    print(left, right)

    if min(left, right) < 0.25:
        robot.stop()
    else:
        robot.kinematic(lin_speed=20)




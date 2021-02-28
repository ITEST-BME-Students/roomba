from library import Sonar
import time

sonar = Sonar.Sonar()

while True:
    sensor1, sensor2 = sonar.distance()
    txt = "Left: %0.2f, Right: %0.2f" % (sensor1, sensor2)
    print(txt)
    time.sleep(0.5)



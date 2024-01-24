from Roomba import Sonar
import time
n = 50
sensors = [1]
sonar_sensors = Sonar.Sonar(sensors=sensors)
for i in range(n):
    print(i)
    try:
        sonar_ranges = sonar_sensors.distance()
    except:
        pass
    print(i, sonar_ranges)
    time.sleep(1)


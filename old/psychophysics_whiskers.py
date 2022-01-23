from Roomba import Whiskers
import time

whiskers = Whiskers.Whiskers()
repeats = 10

while True:
    sensor1_sum = 0
    sensor2_sum = 0
    for x in range(repeats):
        sensor1, sensor2 = whiskers.feel()
        sensor1_sum = sensor1_sum + sensor1
        sensor2_sum = sensor2_sum + sensor2
    sensor1 = sensor1_sum / repeats
    sensor2 = sensor2_sum / repeats
    txt = "Left: %0.2f, Right: %0.2f" % (sensor1, sensor2)
    print(txt)
    time.sleep(0.5)



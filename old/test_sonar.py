#!/usr/bin/env python3

from time import sleep
from gpiozero import DistanceSensor

#dist_sensor1 = DistanceSensor(echo=20, trigger=26)
dist_sensor2 = DistanceSensor(echo=18, trigger=17)

print('deter')
while True:
    #print("Distance sensor 1 read %.1f cm." % (dist_sensor1.distance * 100))
    print("Distance sensor 2 read %.1f cm." % (dist_sensor2.distance * 100))
    sleep(1)


# import time
# import board
# import adafruit_hcsr04
# sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D19, echo_pin=board.r)
# print(sonar.distance())
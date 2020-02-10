from PD2030.roomba import Client
import time
import random
import numpy
c = Client.Client(False)
c.start_remote_server()
c.toggle_logging(False)

rotational_velocity = 10
linear_velocity = 0.1
threshold = 30

while True:
    bumpers = c.get_bumper_data(binary=False)
    binary = c.get_bumper_data(binary=True)

    left = max(bumpers[0:3])
    right = max(bumpers[3:])
    both = max(bumpers)

    print(left, right,binary)

    if both > threshold:
        if left > right: c.set_velocity(0, -rotational_velocity)
        if left < right: c.set_velocity(0, rotational_velocity)
    else:
        c.set_velocity(linear_velocity, 0)

    time.sleep(1)

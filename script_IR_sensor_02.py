from Roomba import Roomba
import time

my_robot = Roomba.Roomba()
threshold = 10

while True:

    # Get data from IR sensors
    ir_values = my_robot.get_bumpers()
    max_value = max(ir_values)
    print(max_value, ir_values)

    # Move if max value < threshold, else stop
    if max_value < threshold:
        my_robot.set_motors(100, 100)
    if max_value > threshold:
        my_robot.stop()

    time.sleep(0.25)

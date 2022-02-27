from Roomba import Roomba
import time

my_robot = Roomba.Roomba()
threshold1 = 50
threshold2 = 100
threshold3 = 200
threshold4 = 500

while True:
    # Get data from IR sensors
    ir_values = my_robot.get_bumpers()
    max_value = max(ir_values)
    print(max_value, ir_values)

    # Move if max value < threshold, else move back
    if max_value < threshold1:
        my_robot.set_motors(100, 100)
    if max_value > threshold1:
        my_robot.set_motors(75, 75)
    if max_value > threshold2:
        my_robot.set_motors(50, 50)
    if max_value > threshold3:
        my_robot.set_motors(25, 25)
    if max_value > threshold4:
        my_robot.stop()

    time.sleep(0.25)

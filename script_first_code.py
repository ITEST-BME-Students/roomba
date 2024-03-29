from Roomba import Roomba
import time

robot = Roomba.Roomba()
threshold = 10

while True:

    # Get data from IR sensors
    ir_values = robot.get_bumpers()
    left_ir_values = ir_values[0:3]
    right_ir_values = ir_values[3:6]

    max_all = max(ir_values)
    max_left = max(left_ir_values)
    max_right = max(right_ir_values)

    if max_all > threshold:
        if max_left > max_right:
            robot.kinematic(0, 20)
        if max_left < max_right:
            robot.kinematic(0, -20)

    if max_all < threshold:
        robot.kinematic(100)

    print(left_ir_values, right_ir_values)
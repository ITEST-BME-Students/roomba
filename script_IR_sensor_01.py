from Roomba import Roomba
import time

my_robot = Roomba.Roomba()

while True:
    ir_values = my_robot.get_bumpers()
    print(ir_values)
    time.sleep(1)

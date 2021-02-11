from library import Roomba
import time

# Approach 1
# my_robot = Roomba.Roomba()
#
# for x in range(100):
#     values = my_robot.get_bumpers()
#     mx = max(values)
#     if mx < 30: my_robot.move(100)
#     print(values)
#

# Approach 2

my_robot = Roomba.Roomba()
my_robot.set_display('strt')
my_robot.kinematic(lin_speed=100)
while True:
    values = my_robot.get_bumpers()
    if max(values) > 30: break
    print(values)
my_robot.stop()

my_robot.set_display('end')
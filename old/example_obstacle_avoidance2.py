from Roomba import Roomba
import time

#Approach 1
# my_robot = Roomba.Roomba()
#
# for x in range(2000):
#     values = my_robot.get_bumpers()
#     left = values[0:3]
#     right = values[3:6]
#     max_left = max(left)
#     max_right = max(right)
#
#     if max_left > 30:
#         my_robot.turn(10)
#     elif max_right > 30:
#         my_robot.turn(-10)
#     else:
#         my_robot.move(100)



# Approach 2
speed = 100
my_robot = Roomba.Roomba()
my_robot.set_display('strt')


while True:
    values = my_robot.get_bumpers()
    left = values[0:3]
    right = values[3:6]
    max_left = max(left)
    max_right = max(right)

    if max_left > 30:
        my_robot.kinematic(lin_speed=0, rot_speed=10)
    elif max_right > 30:
        my_robot.kinematic(lin_speed=0, rot_speed=-10)
    else:
        my_robot.kinematic(lin_speed=speed)


my_robot.set_display('end')

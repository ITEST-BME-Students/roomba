from Roomba import Roomba
import time

robot = Roomba.Roomba()

robot.move(100)
while True:

    all_sensors = robot.get_sensors()
    bumpers = robot.get_bumpers()
    a = all_sensors['bumps_wheeldrops'].bump_left
    b = all_sensors['bumps_wheeldrops'].bump_right
    print('wall', all_sensors['wall'])
    print('wall_signal', all_sensors['wall_signal'])
    print(a,b)
    time.sleep(1)
    #break

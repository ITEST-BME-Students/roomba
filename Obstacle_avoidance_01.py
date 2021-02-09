from library import Roomba
import time

my_robot = Roomba.Roomba()
my_robot.set_display('strt')

for x in range(100):
    time.sleep(0.5)
    values = my_robot.get_bumpers()
    print(values)
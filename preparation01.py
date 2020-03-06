from PD2030.roomba import Client
import time
# Connect to the robot
robot = Client.Client(name='WALL-E', do_upload=True)
robot.start_remote_server()
robot.toggle_logging(False)

while True:
    data = robot.get_bumper_data(binary=False)
    print(data)
    mn = min(data)

    if mn > 0.75: robot.set_velocity(100, 0)
    if mn < 0.75: robot.set_velocity(0, 0)
    time.sleep(0.5)

from PD2030.roomba import Client
import time
# Connect to the robot
robot = Client.Client(name='WALL-E', do_upload=True)
robot.start_remote_server()


while True:
    data = robot.get_bumper_data()
    #print(data)

    right_sensors = data[0:3]
    left_sensors = data[4:6]

    mn = min(data)
    mn_left = min(left_sensors)
    mn_right = min(right_sensors)

    if mn > 0.9:
        scaledVelocity = (mn-.45)/.55
        robot.set_velocity(100*scaledVelocity, 0)
        print(scaledVelocity)
    if mn < 0.9:
        if mn_left < mn_right: robot.set_velocity(0, 50)
        if mn_left > mn_right: robot.set_velocity(0, -50)

    time.sleep(0.75)
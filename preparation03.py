from PD2030.roomba import Client
import time
# Connect to the robot
robot = Client.Client(name='WALL-E', do_upload=True)
robot.start_remote_server()

while True:
    data = robot.get_bumper_data()
    print(data)

    right_sensors = data[0:3]
    left_sensors = data[4:6]

    mn = min(data)
    mn_left = min(left_sensors)
    mn_right = min(right_sensors)

    threshold = 0.85

    if mn > threshold:
        factor = (mn - threshold) / (1 - threshold)
        speed = 500 * factor
        robot.set_velocity(speed, 0)
    else:
        if mn_left < mn_right: robot.set_velocity(0, 25)
        if mn_left > mn_right: robot.set_velocity(0, -25)

    time.sleep(0.5)

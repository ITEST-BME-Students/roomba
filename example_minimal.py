from PD2030.roomba import Client
import time

name = 'WALL-E'

robot = Client.Client(name=name, do_upload=True)
robot.start_remote_server()
robot.test_communication(message=['hello'])
data = robot.get_adc()


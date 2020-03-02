from PD2030.roomba import Client
ip = 'WALL-E'
robot = Client.Client(name='WALL-E', do_upload=True)
robot.start_remote_server()

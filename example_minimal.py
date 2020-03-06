from PD2030.roomba import Client
robot = Client.Client(name='KITT', do_upload=False)
robot.start_remote_server()
robot.test_communication(message=['hello'])
data = robot.get_adc()
print(data)
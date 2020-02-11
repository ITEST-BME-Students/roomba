from PD2030.roomba import Client
from PD2030.roomba import Support

c = Client.Client(ip='192.168.0.249', do_upload=True)
c.start_remote_server()

t = c.get_external_sensor('thermal')
Support.process_thermal_data(t, True)


from library import Client
from library import Support
c = Client.Client(ip='192.168.0.249', do_upload=True)


c.start_remote_server()

#%%
t = c.get_external_sensor('thermal')
Support.process_thermal_data(t, True)


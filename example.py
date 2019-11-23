from library import Client
import time

c = Client.Client(run_locally=True)
c.start_remote_server()
c.set_motors(0.1,0.1)
time.sleep(0.1)
c.get_sensors()
c.set_motors(0.5,0.5)
from library import Client
import time
c = Client.Client(run_locally=False)


c.start_remote_server()

for x in range(100):
    d = c.get_external_sensor('sonar1')
    print(d)
    time.sleep(0.25)

#c.get_roomba_sensors()
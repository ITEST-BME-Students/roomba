from library import Client
from library import Support
import time

c = Client.Client(False)


c.start_remote_server()

for x in range(100):
    a = c.get_thermal_image()
    b = Support.interpolate_thermal_image(a, True)
    time.sleep(0.25)
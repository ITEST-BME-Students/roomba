from library import Client
from library import Misc
import time

c = Client.Client(run_locally=True)
c.start_remote_server()
c.toggle_logging(False)

while True:
    text = c.formatted_sensor_data()
    Misc.clear_console()
    print(text)
    time.sleep(1)
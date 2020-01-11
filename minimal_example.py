from library import Client
import time
#ip = '192.168.0.249'
ip = '192.168.200.238'
c = Client.Client(ip=ip, do_upload=True)


c.start_remote_server()

#for x in range(100):
#    d = c.get_external_sensor('sonar1')
#    print(d)
#    time.sleep(0.25)

#c.get_roomba_sensors()
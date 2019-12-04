from library import Client

c = Client.Client(run_locally=False)


c.start_remote_server()
c.get_roomba_sensors()
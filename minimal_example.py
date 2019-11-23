from library import Client

c = Client.Client(run_locally=True)
c.start_remote_server()
c.get_sensors()
from Roomba import Camera


c = Camera.Camera()
d = c.get_data(plot=True)
c.close_camera()
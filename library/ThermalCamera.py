import adafruit_mlx90640
import board
import busio
import time
import copy
import threading


class ThermalCamera:
    def __init__(self):
        self.ic2 = busio.I2C(board.SCL, board.SDA, frequency=400000)
        self.mlx = adafruit_mlx90640.MLX90640(self.ic2)
        self.mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ
        self.msg = ("MLX addr detected on I2C", [hex(i) for i in self.mlx.serial_number])
        self.frame = [0] * 768
        self.reading_camera_data = False
        self.returning_data = False

        thread = threading.Thread(target=self.data_acquisition_loop)
        thread.start()

    def data_acquisition_loop(self):
        while True:
            while self.returning_data: time.sleep(0.1)
            self.reading_camera_data = True
            self.mlx.getFrame(self.frame)
            self.frame = list(map(int, self.frame))
            self.reading_camera_data = False
            time.sleep(0.5)

    def get_data(self):
        while self.reading_camera_data: time.sleep(0.1)
        self.returning_data = True
        data = copy.copy(self.frame)
        self.returning_data = False
        return data

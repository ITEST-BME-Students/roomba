# # from library import Microphone
# # s = Microphone.SoundSensor()
# # s.get_data(plot=True)
#
# from library import Camera
# c = Camera.Camera()
# p = c.get_section_values()

from library import Roomba
from library import Microphone
from library import Camera
from library import Thermal

t = Thermal.Thermal()
x = t.look()
print(x)
# m = Microphone.Microphone()
# c = Camera.Camera()
# r = m.listen()
# v = c.look()

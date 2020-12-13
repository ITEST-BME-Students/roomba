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

r = Roomba.Roomba()
m = Microphone.Microphone()
c = Camera.Camera()

#snd = m.listen(plot=True)
vis = c.look(plot=True)
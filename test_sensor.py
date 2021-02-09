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
from library import Device
from library import Thermal

#from library import Thermal
#r = Roomba.Roomba()
#m = Microphone.Microphone()
c = Camera.Camera()
c.get_data(plot=True)

#snd = m.listen(plot=True)
#vis = c.look(plot=True)

#t = Thermal.Thermal()
#r = t.look()

#c.look()

#d = Device.AnalogInput()
#d.sense(plot=True)
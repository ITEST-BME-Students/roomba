from PD2030.maestro import Board
import time

b = Board.Board()

b.set_led1(True)
b.set_led2(True)

time.sleep(3)

b.set_led1(False)
b.set_led2(False)

light_level = b.get_photo()
dial_position = b.get_dial()
print(light_level)
print(dial_position)




# GOAL: We want to the green and the red LED to flash every second, for 15 times.

# From the package PD2030 import the subpackage maestro
# and from that import the the definition of the board class
from PD2030.maestro import Board
# import the time package (or module). This is a standard package included in python
import time

# Make a variable of the board class type. This will connect to the physical board
board = Board.Board()

n = 15
# read as: repeat the next block n times (with the value of n set in the previous line).
for x in range(n):
    # switch one LED on and the other off
    board.set_led1(False)
    board.set_led2(True)
    # wait 1 second
    time.sleep(1)
    # swap which LEDs are on
    board.set_led1(True)
    board.set_led2(False)
    # wait 1 second
    time.sleep(1)



# Goal: the value of the light sensor is constantly read out. If the light value is below a preset value
# the LEDs are turned on. If the light sensor value is higher than the threshold, the LEDs are switched off.

# From the package PD2030 import the subpackage maestro
# and from that import the the definition of the board class
from PD2030.maestro import Board
# import the time package (or module). This is a standard package included in python
import time

# Make a variable of the board class type. This will connect to the physical board
board = Board.Board()

# Specify the threshold value
threshold = 0.75

# Start a never ending loop
# TO STOP YOUR PROGRAM YOU WILL NEED TO CLICK THE RED SQUARE IN THE TOP RIGHT CORNER OF THE CONSOLE WINDOW
# OR YOU CLICK IN THE CONSOLE WINDOW AND TYPE Crtl+C

while True:
    # Get the current value of the light sensor (which is between 0 and 1)
    light_value = board.get_photo()
    # Print the light value to the screen to get some feedback while the program is running
    print(light_value)
    # if the light value is below the threshold, switch the LEDs on
    if light_value < threshold:
        board.set_led1(True)
        board.set_led2(True)

    # if the light value is above the threshold, switch the LEDs off
    if light_value > threshold:
        board.set_led1(False)
        board.set_led2(False)




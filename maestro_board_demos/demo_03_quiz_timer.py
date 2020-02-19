# Goal: Let's build a quiz timer counting down n seconds you have to give an answer
# The arrow of one motor will be used as an analog clock ticking down the seconds.
# The quiz contestant can respond by pressing a button (putting their finger over the light sensor)
# If the contestant responds within n seconds, the clock stops and the green led comes on
# If time is up, the red led comes on.

# Goal: the value of the light sensor is constantly read out. If the light value is below a preset value
# the LEDs are turned on. If the light sensor value is higher than the threshold, the LEDs are switched off.

# From the package PD2030 import the subpackage maestro
# and from that import the the definition of the board class
from PD2030.maestro import Board
# import the time package (or module). This is a standard package included in python
import time

# Make a variable of the board class type. This will connect to the physical board
board = Board.Board()

# set the number of seconds the contestant has
seconds = 5
# set the number of steps in which we will count down
steps = 50
# Set the start position of the motor
motor_position = 0

# start a loop that repeats 'steps' times
for x in range(steps):
    #set the motor to position 'motor_position'. The first time around, this will be zero
    board.set_servo1(motor_position)
    #wait some time (seconds/steps)
    time.sleep(seconds/steps)
    # increase the position of the motor. The motor position runs from 0 to 1. So, we add 1/steps to the position of the motor
    motor_position = motor_position + (1/steps)
    # get the value of the light sensor to check for a response
    light_value = board.get_photo()
    # if the light value is smaller than 0.75, we will assume that someone has blocked the sensor (pressed the response button)
    # the break statement breaks out whatever loop is currently running
    if light_value < 0.75:
        break # This stops the for-loop

# If we reach this position in our program two things might have happened:
# 1) we detected a button press (light value < 0.75) and we broke out off the loop
# 2) or, we have completed the 'steps' iterations. In this case time has run out.

# if x = 49, time has run out (the for loop will run from x=0 to x=49)
# in general, x will run from 0 to steps - 1
# in this case, we switch on the red light
if x == (steps - 1):
    board.set_led1(False)
    board.set_led2(True)
    print('Time out - you loose')

# if x < 49, we had some time left, and we switch on the green light
if x < (steps - 1):
    board.set_led1(True)
    board.set_led2(False)
    print('What is your answer?')


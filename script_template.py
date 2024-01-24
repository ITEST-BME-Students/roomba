# Import the Roomba module to be able to communicate with the robot
from Roomba import Roomba

# Import the modules needed for communicating with the sensors on the robot
from Roomba import Camera
from Roomba import Sonar
from Roomba import Thermal
from Roomba import Whiskers
from Roomba import Microphone

# The time module contains various timing functions
# It can be used to slow down the execution of the program
import time

# Create an object for communicating with the robot
my_robot = Roomba.Roomba()

# Create objects to communicate with the sensors (as needed)
# Remove the # in front of each line to starting using it

#my_camera = Camera.Camera()
my_sonar = Sonar.Sonar()
#my_thermal = Thermal.Thermal()
#my_whiskers = Whiskers.Whiskers()
#my_mics = Microphone.Microphone()

# Now you are ready to start the mainloop of your program.
while True:
    # Anything in this loop will be repeated over and over again
    # The bulk of your program should go here. These are the steps you most likely need:
    # 1. Get some data from selected sensors
    # 2. Process/Select data
    # 3. Make a decision about what to do next and Mmve the robot
    # Below I give a very example of these steps

    # STEP 1. Get data from sonar sensors
    sonar_data = my_sonar.distance()

    # STEP 2. Do some processing
    # Sonar_data will contain 2 numbers, here I assign these to different variables
    # I also get the minimum distance across the two sensor values
    left = sonar_data[0]
    right = sonar_data[1]
    min_distance = min(sonar_data)
    # It's a good idea to print some sensor values so you can see what's going on
    print(sonar_data)

    # Step 3. Deciding what to do
    if min_distance < 0.10:
        my_robot.stop()
    else:
        if left < right:
            my_robot.kinematic(lin_speed=50, rot_speed=20)
        if left > right:
            my_robot.kinematic(lin_speed=50, rot_speed=-20)

    # Let the robot execute whatever command you gave it for a while before re-running the loop
    time.sleep(1)





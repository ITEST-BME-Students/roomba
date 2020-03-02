from PD2030.roomba import Client

# Connect to the robot
robot = Client.Client(name='WALL-E', do_upload=True)
robot.start_remote_server()

# Turn in place
robot.turn(30) # Degrees

# Move forward
robot.move(100) # Millimeter

# Get bumper data
data = robot.get_bumper_data()

# Set velocities
linear = 100 # in mm/s
angular = 20 # in degrees/s
robot.set_velocity(linear, angular)
# Robot commands

## Creating a robot

```angular2html
from library import Roomba
my_robot = Roomba.Roomba()
```

The robot should respond with the following message, showing that connection was made.

```angular2html
----------------------------------------
 Create opened serial connection
   port: /dev/ttyUSB0
   datarate: 115200 bps
----------------------------------------
```

## Commands controlling the robot motion

### Motion commands

+ `my_robot.set_motors(left_speed, right_speed)`

Sets the speed of the two motors, in millimeter per second.

+ `my_robot.kinematic(rot_speed=x, lin_speed=y)`

Sets the robot's linear speed and rotational speed, in millimeter per second and degrees per second. If one the two arguments is not provided, it will be assumed to be zero.

+ `my_robot.move(distance)` 

Makes the robot drive a certain distance, in millimeter.

+ `my_robot.turn(degrees)`

Makes the robot turn a number of degrees. Positive angles are clockwise (right) and negative angles are counter clock wise (left).

+ `my_robot.stop()`

Stops the robot


### Additional commands

+ `my_robot.set_display(text)`

This command sets the onboard roomba display. The onboard display can show up to four characters.

+ `result = my_robot.get_bumpers()`

Gets the 6 values of the onboard obstacle detection sensors (bumpers). This function returns a list of 6 values, in the following order:

1. left
2. front left
3. center left
4. center right
5. front right
6. right

In theory, the sensors values range from 0 to 4095, with larger values indicating closer obstacles detected by the sensor. Typical values without obstacle range up to ~20.




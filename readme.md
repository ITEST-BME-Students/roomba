# Summary of flow control


### The `if` statement

Syntax: 

```python
if <condition>:
	<code inside the if statement>
```

Example:

```python
value = 100
if value < 100:
	print('smaller than 100')
```

More examples:

+ [https://www.w3schools.com/python/python_conditions.asp](https://www.w3schools.com/python/python_conditions.asp)

### The `for` loop

Syntax: 

```python
for <variable> in <collection>:
	<code inside the for loop>
```

Example  1 (executing something n times):

```python
for i in range(n):
	print(n)
```

Example 2:

```python
my_list = [10, 23, 45, 10, 7]
for i in my_list:
	result = i * 3
	print(result)
```

More examples:

+ [https://www.w3schools.com/python/python_for_loops.asp](https://www.w3schools.com/python/python_for_loops.asp)

### The `while` loop

Syntax: 

```python
while <collection>:
	<code inside the while loop>
```

Example  1 (executing something forever):

```python
import random
while True:
	random_number = random.random()
	print(random_number)
```

Example  2:

```python
import random
random_number = 0
while random_number < 0.5:
	random_number = random.random()
	print(random_number)
```

More examples:

+ [https://www.w3schools.com/python/python_while_loops.asp](https://www.w3schools.com/python/python_while_loops.asp)


# Robot commands



## Creating a robot

```python
from library import Roomba
my_robot = Roomba.Roomba()
```

The robot should respond with the following message, showing that connection was made.

```
----------------------------------------
 Create opened serial connection
   port: /dev/ttyUSB0
   datarate: 115200 bps
----------------------------------------
```

## Motion commands

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

## Sensor commands

### Camera

The camera on the robot has an 160 degree field of view. The following code gets data from the camera. It returns values from a number of areas within the 160 degree field of the camera. Depending on the settings, the data can be RGB data or grayscale data (or any combination of the camera's RGB values).

```python
from library import Camera
camera = Camera.Camera()
data = camera.look()
```

### Thermal camera

The thermal camera on the robot has an 110 degree field of view. The following code gets data from the thermal camera. It returns values from a number of areas within the field of the camera. The data is in degrees celcius.

```python
from library import Thermal
thermal = Thermal.Thermal()
data = thermal.look()
```

### Microphone

The robot features two micophones. The following code returns data from the microphones. The `listen()` function returns two sets of values:

1. The loudness of the right microphone, for different frequency bands minus the loudness of the right microphone, for different frequency bands

2. The estimated interaural time difference (left leading sounds produce negative values)

```python
from library import Microphone
microphone = Microphone.Microphone()
loudness_difference, time_difference = microphone.listen()
```

### Sonar

The robot's sonar sensors measure the distance to the nearest object that returns a detectable echo. The following code gets the distance as detected by the two sensors.

```python
from library import Sonar
sonar = Sonar.Sonar()
left, right = sonar.distance()
```

## Additional commands

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
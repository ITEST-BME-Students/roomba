# Programming cheat sheet

## Basic program structure

The diagram below shows the basic structure of a program for the robot. A program typically starts with some initialization code. This code defines variables used in the remainder of the code. The main loop continously iterates through a number of steps.

![](/home/dieter/Dropbox/PythonRepos/roomba/student_documentation/program_structure.png)

## Flow control

### Main loop
Setting up the mainloop is typically done using ```while True:```. This creates an infinite loop.  The following shows how to use the while loop.

```
while True:
	Do_something_here
	Do_something_else
```

### If statement

Your robot will need to make decisions based on the sensor data. This can be programmed using the ```if``` statement. The ```if``` statement allows executing part of the code if something is true. The struture of the ```if``` statement is shown below.

```
if [some_check]:
	Do_this
	And_this
```
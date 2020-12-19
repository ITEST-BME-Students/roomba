# Roomba

## Required libraries:

+ ```pip3 install adafruit-circuitpython-mlx90640```
+ ```pip3 install sounddevice```
+ ```pip3 install matplotlib```
+ ```sudo apt install python3-scipy```
+ ```sudo apt install python3-pandas```

## Reference frame robot

* positive angles: counter clockwise
+ negative angles: clock wise

## Reference frame IR camera

If the MLX label on the camera is the top of the camera, then in the returned image
+ left is left with respect to the camera
+ up is up with respect to the camera

## Reference frame PI camera

If the ribbon camera is bottom of the camera, then in the returned image
+ left is left with respect to the camera
+ up is up with respect to the camera
# Roomba

## iRobot Create  2 Open Interface

[https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf](https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf)

## Required libraries:

+ See ```install_packages.sh```

## Reference frame robot

* Positive angles: clockwise (right)
+ Negative angles: counter clock wise (left)

## Reference frame IR camera

If the MLX label on the camera is the top of the camera, then in the returned image
+ Left is left with respect to the camera.
+ Up is up with respect to the camera.

## Reference frame PI camera

If the ribbon camera is bottom of the camera, then in the returned image
+ left is left with respect to the camera
+ up is up with respect to the camera

## Known bugs
+ Very small turn angles (<6 degrees) do not seem to be reliably executed.
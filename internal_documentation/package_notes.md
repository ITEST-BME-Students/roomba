# Roomba

## iRobot Create  2 Open Interface
[https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf](https://cdn-shop.adafruit.com/datasheets/create_2_Open_Interface_Spec.pdf)

## Required libraries:

+ ```pip3 install adafruit-circuitpython-mlx90640```
+ ```pip3 install sounddevice```
+ ```pip3 install matplotlib```
+ ```sudo apt install python3-scipy``` (do not use ```pip3```)
+ ```sudo apt install python3-pandas```

Portaudio not found:

+ ```sudo apt-get install libasound-dev```
+ ```sudo apt-get install portaudio19-dev```
+ ```sudo apt-get install python3-pyaudio```


libf77blas.so.3 not found:

+ ```sudo apt-get install libatlas-base-dev```



## Reference frame robot

* positive angles: clockwise (right)
+ negative angles: counter clock wise (left)

## Reference frame IR camera

If the MLX label on the camera is the top of the camera, then in the returned image
+ left is left with respect to the camera
+ up is up with respect to the camera

## Reference frame PI camera

If the ribbon camera is bottom of the camera, then in the returned image
+ left is left with respect to the camera
+ up is up with respect to the camera

## Known bugs
+ Too small turn angles (<6 degrees) do not seem be reliably executed.
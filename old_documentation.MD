
# Deprecated

## Thermal sensor: adafruit amg88xx

Adafruit provides a library for this sensor. It can be installed for Python 3 by running the following code on the Raspberry Pi.

```sudo pip3 install adafruit-circuitpython-amg88xx```

The orientation of the data is as follows: with the sensor oriented with the wires at the bottom, the image behaves like a camera image: 

+ Pixels at the left of the image come from the left of the field of view.
+ Pixels at the top come from the top of the field of view.

```

######
##++##
##++##
######
#WIRES#
 | | | |


----->

```
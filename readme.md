# Documentation for users and students

The documentation for users and students can be found in the ```documentation``` folder. The functions provided by the class ```client``` are documented in ```documentation\markdown```. The documentation below specifies how the software can be installed on the raspberry pi and the host computer. **The documentation is not intended to be used by students**.

[Direct link to the student documentation](https://github.com/BME-ITEST-Students/roomba/blob/master/documentation/markdown/index.md) 

**Downloading the code** The latest version of the code can be downloaded as a zip file by clicking the green download button, alternatively you can navigate to the releases and download a specific version.

# Software installation

## Generating the docs

```make markdown```

## Install pycreate2

```https://github.com/MomsFriendlyRobotCompany/pycreate2```

## ADC shield

First, activate i2c on the raspberry pi in the settings. Next, install the python library. The instructions are found on this [wiki](http://wiki.seeedstudio.com/8-Channel_12-Bit_ADC_for_Raspberry_Pi-STM32F030/). In brief, this code should be run on the Raspberry Pi:

````
cd ~
git clone https://github.com/Seeed-Studio/grove.py
sudo pip3 install .
````

This installs the python code in home directory. Therefore, using the code requires the following lines to the Python scripts using it.

```
sys.path.insert(0,'/home/pi/grove.py/grove')
import adc_8chan_12bit
```

The wiki lists the `` Pi_hat_adc`` class and its functions, which can be used to read out the ADC shield.

## Thermal sensor

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

## RPi.GPIO library

The ```RPi.GPIO ``` libray is  installed per default for Python 3 on the raspberry. The Raspberry Pi provides a command ```pinout```  to get the pinout diagram:

```
   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21
```



## PyQt 4

The joystick control script requires PyQt 4 on the host computer (not the Raspberry Pi), this can be installed as follows,

```conda install pyqt=4```


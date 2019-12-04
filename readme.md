# install pycreate2


```https://github.com/MomsFriendlyRobotCompany/pycreate2```

# ADC manual

## Installation

Step 1: activate i2c on the raspberry pi in the settings.

Step 2: install the python library

The instructions are found on this wiki:

+ http://wiki.seeedstudio.com/8-Channel_12-Bit_ADC_for_Raspberry_Pi-STM32F030/

In brief, run this code on the raspberry:

````
cd ~
git clone https://github.com/Seeed-Studio/grove.py
sudo pip3 install .
````

This installs the python code in home directory. Therefore, using the code requires

```
sys.path.insert(0,'/home/pi/grove.py/grove')
import adc_8chan_12bit
```

The wiki also lists the `` Pi_hat_adc`` class and its functions, which can be used to read out the ADC.



# Roomba

## Reset

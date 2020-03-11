# Wiring the sensors

**THE ADC BOARD IS NOT 5V TOLERANT!**

## Whisker sensors
+ Analog sensor. Connects to the ADC board.

```Command: robot.get_adc()```

This sensor can be wired to any of the analog channels. The sensor can use 5V (from raspberry pi) or 3V (from the Raspberry Pi or the ADC board) as input.

## MLX90640 Thermal Camera

+ Connects to I2C. 

```Command: robot.get_thermal_image()```

If the power is wired correctly, a green LED comes on. To use this sensor, it needs to be switched on in the ```Settings.py``` file. Be sure to upload the new version of this settings file to the raspberry.

 Vin → connect to any 3v pin (raspberry or on the ADC board)
 Gnd → connect to any ground pin (raspberry or on the ADC board)
 SDA → GPIO 02
 SCL → GPOI 03

## Makeblock light sensor

+ Analog sensor. Connects to the ADC board.

```Command: robot.get_adc()```

This sensor should be powered **using 3V only**. If fed with 5V, the output voltage goes up to 5V. However, the sensor can be be used with 3V input and gives an adequate signal in this case.

## Makeblock sound sensor

* Analog sensor. Connects to the ADC board.

```Command: robot.get_adc()```

This is an analog sensor. You can feed the sound sensor with 5V, the output signal does not go beyond about 2.5V

## RCWL-1601 Sonar

* Digital sensor. Connects to the Raspberry Pi GPIO pins.
 
```Command: robot.get_sonar_distances()```

To use these sensors, they need to be switched on in the ```Settings.py``` file. Be sure to upload the new version of this settings file to the raspberry.

This sensor is a 3v compatible version of the popular sonar sensor that typically requires 5V.  The sensors can be powered using any 3v pin and ground pin. The other pins should be wired to the following GPIOs. The number refers to the GPIO number (not the physical pin number)

trigger_pin1 → 26
trigger_pin2 → 19 
echo_pin1 → 20
echo_pin2 → 16
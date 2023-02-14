import RPi.GPIO as GPIO
import time
from Roomba import Settings

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = Settings.trigger_pin2
GPIO_ECHO = Settings.echo_pin2

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        print('.')
        StartTime = time.time()

    # save time of arrival
    print('Waiting for Echo.', end='')
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    print('done')


    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    print(TimeElapsed)
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

print('go')
a = distance()
print(a)
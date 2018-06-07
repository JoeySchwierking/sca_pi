#!/usr/bin/evn python
# This script will turn the passive buzzer on then off

import RPi.GPIO as GPIO
import time

#breadboard seatup
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

# set Passive Buzzer pin's mode as ountut
GPIO.setup(buzz_pin,GPIO.OUT)

# create Buzz function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(1)

# stop Passive Buzzer using Buzz function
Buzz.stop

# reset GPIO resources used by script
GPIO.cleanup()

#change Buzz finction and set the sound frequency to 500
Buzz = GPIO.PWM(buzz_pin,500)
Buzz.ChangeFrequency(450)

# start Passive Buzzer using Buzz function with 50% duty for 1 second
Buzz.start(50)
time.sleep(1)

# stop Passive Buzzer using Buzz function
Buzz.stop

# reset GPIO resources used by script
GPIO.cleanup()

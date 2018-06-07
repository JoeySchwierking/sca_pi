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

Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)
Buzz.start(50)
time.sleep(1)
Buzz.stop

Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)
Buzz.start(50)
time.sleep(1)
Buzz.stop

Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)
Buzz.start(50)
time.sleep(1)
Buzz.stop

Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)
Buzz.start(50)
time.sleep(1)
Buzz.stop

Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)
Buzz.start(50)
time.sleep(1)
Buzz.stop

Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)
Buzz.start(50)
time.sleep(1)
Buzz.stop

Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)
Buzz.start(50)
time.sleep(1)
Buzz.stop




















































GPIO.cleanup()

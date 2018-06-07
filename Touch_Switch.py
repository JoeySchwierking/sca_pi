#!/usr/bin/evn python
import RPi.GPIO as GPIO
import time

# breadboard set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


# assign pin number for Touch Switch and Buzzer
# pin 31 = GPIO 6
# pin 32 = GPIO 12
touch_pin = 31
buzz_pin = 32

# set Touch Switch pin's mode as input
GPIO.setup(touch_pin,GPIO.IN)

# set Buzzer pin's mode as output
GPIO.setup(buzz_pin,GPIO.OUT)

Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(450)

# create infinite loop that reads Touch Switch input
while True:
	if GPIO.input (touch_pin) == 0:
		Buzz.stop()
	if GPIO.input(touch_pin) == 1:
		Buzz.start(440)

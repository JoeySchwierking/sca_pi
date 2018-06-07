#!/usr/bin/env python

import random
import RPi.GPIO as GPIO
import time

# breadboard set up
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#assign pin number for Passive Buzzer; pin 32 = GPIO 12
buzz_pin = 32

#assign the pin number for Auto Flash LED; pin 11 = GPIO 17
led_pin = 11

# set Passive Buzzer pin's mode as ountut
GPIO.setup(buzz_pin,GPIO.OUT)

# create Buzz function and set initial sound frequency to 1000 Hz
Buzz = GPIO.PWM(buzz_pin,1760)
Buzz.ChangeFrequency(3000)

i=0

print 'Guess the number between 1 and 10'	
a=random.randint(1,10)
counter=0
while counter<10:
	guess=int(raw_input('Guess a random number between 1 and 10: '))
	if guess>a:
		# turn on buzzer
		Buzz.start(50)
		time.sleep(1)
		#stop buzzer
		Buzz.stop
		GPIO.cleanup()
		#computer screen
		print 'Too High'
		counter = counter + 1
		print 'Attempt number',counter
	else:
		if guess<a:
			# turn on buzzer
			Buzz.start(50)
			time.sleep(1)
			#stop buzzer
			Buzz.stop
			GPIO.cleanup()
			# computer screen
			print 'Too Low'
			counter = counter + 1
			print 'Attempt number ',counter
		else:
			#turn on Auto Flash LED
			GPIO.output (led_pin,True)
			time.sleep (2)
			#turn off Auto Flash LED
			GPIO.output(led_pin,False)
			# reset GPIO resources used by script
			GPIO.cleanup()
			print 'You win'
			i=i+1
			counter = counter+1
			print 'Number of attempts required: ',counter
			counter=11
if i<1:
	print 'You took too long'
	Buzz.start(50)
	time.sleep(1)
	#stop buzzer
	Buzz.stop
	GPIO.cleanup()
	Buzz.start(50)
	time.sleep(1)
	#stop buzzer
	GPIO.cleanup()
	Buzz.stop
	Buzz.start(50)
	time.sleep(1)
	#stop buzzer
	Buzz.stop
	GPIO.cleanup()

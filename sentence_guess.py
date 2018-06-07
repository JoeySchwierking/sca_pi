#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# use the RGB values to define colours

counter = 1
white = (255, 255, 255)
blue = (0, 0, 255)
i = 0
speed = 0.01
message = 'As a farmer I know that when an animal is sick sometimes the right thing to do is put it out of its misery. With the electricity we are using to keep Meredith alive, we could power a small fan for two days. You tell me what’s unethical.'


print 'Guess what the Rasberry Pi Hat said'
while (i==0):
	sense.show_message(message, speed, text_colour=white, back_colour=blue)
	guess = raw_input('')
	if (guess==message):
		if (counter<=5):
			print 'You won! The speed of the sentence was ',speed,' and you took ',counter,' attempts.'
			speed = 0.05
			message = "You win!"
			sense.clear()
			sense.show_message(message,speed, text_colour=white,back_colour=blue)
			i = i + 1
			sense.clear()
		else:
			print 'Oh no! You found out! However, you were not able to redeem yourself. You are a waste of our time.'
			sense.clear()
			i = i + 1
	else:
		print 'You are a failure. You may be able to redeem yourself if you try again.'
		speed = speed + 0.005
		counter = counter + 1

#!/usr/bin/env python

import random
i=0


print 'Guess the number between 1 and 10'	
a=random.randint(1,10)
counter=0
while counter<10:
	guess=int(raw_input('Guess a random number between 1 and 10: '))
	if guess>a:
		print 'Too High'
		counter = counter + 1
		print 'Attempt number',counter
	else:
		if guess<a:
			print 'Too Low'
			counter = counter + 1
			print 'Attempt number ',counter
		else:
			print 'You win'
			i=i+1
			counter = counter+1
			print 'Number of attempts required: ',counter
			counter=11
if i<1:
	print 'You took too long'



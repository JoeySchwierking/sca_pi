import random
i=0
num_random_numbers = 10
while i<10:
	random_number = random.randint(1,4)
	print random_number
	i=i+1
	guessed_random_number = int(raw_input('Guess and intiger between 1 and 4')
	if guessed_random_number != random_number:
		print 'Your guess was not correct'

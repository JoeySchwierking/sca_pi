
from sense_hat import SenseHat
import time
import random
sense = SenseHat()

t = 1

while (t < 4):
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	if (t == 1):
		sense.show_letter("H", (r, g, b))
		time.sleep(1)
	if (t == 2):
		sense.show_letter("i", (r, g, b))
		time.sleep(1)
	if (t == 3):
		sense.show_letter("!", (r, g, b))
		time.sleep(1)
	t = t+1
sense.clear()

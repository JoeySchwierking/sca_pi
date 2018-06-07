#!/usr/bin/evn python
from sense_hat import SenseHat
sense = SenseHat()
import time
import random

for 
	x = random.randint(1,7)
	y = random.randint(1,7)

	sense.set_pixel(x, y, (190,60,30))
	time.sleep(random.randint(1,60))

	sense.clear()

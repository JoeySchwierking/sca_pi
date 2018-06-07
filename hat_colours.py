#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()

# use the RGB values to define colours
purple = (255,0,255)
yellow = (255, 255, 0)
blue = (0, 255, 255)

speed = 0.05
message = "Hello World!"

sense.show_message(message, speed, text_colour=blue, back_colour=purple)

sense.clear()

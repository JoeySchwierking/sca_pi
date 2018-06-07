#!/usr/bin/env python

x = int(raw_input('Enter and intiger (>1):'))
while x < 2:
	x = input("Enter and intiger (>1):")
i = 1

while i < x:
	print i," ", i * i
	i=i+1

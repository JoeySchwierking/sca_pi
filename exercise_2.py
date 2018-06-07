#!/user/bin/env python
a=raw_input('Enter first intiger ')
b=raw_input('Enter second intiger ')

if int(a)>int(b):
		print 'Your Minimum is ',b
		print 'The Maximum is ',a
		print 'Maximum-Minimum = ',int(a)-int(b)
else:
	if int(a)<int(b):
		print 'Your minimum is ',a
		print 'Your maximum is ',b
		print 'Maximum-Minimum = ',int(b)-int(a)
	else:
		print 'Your two numbers are equal to each other with a value of',a

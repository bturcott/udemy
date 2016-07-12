#While Loop
#Section 5 Lecture 36

#Basic While Loop
x = 0
while x < 10:
	print 'x is currently: {}'.format(x)
	x+=1
else:
	print 'all done'

#break,continue,pass
x = 0
while x < 10:
	print 'x is currently: {}'.format(x)
	x+=1
	if x==3:
		print 'x==3'
		print 'braking'
		break
	else:
		print 'continuing'
		continue
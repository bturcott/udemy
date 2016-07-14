#s9_l64_hw.py

def problem_one():
	lst = ['a','b','c']
	for elem in lst:
		try:
			print elem ** 2
		except:
			print "Element in list is not a number!"

def problem_two():
	x = 5
	y = 0
	try:
		z=x/y
	except:
		print "Unable to divide by zero!"
	finally:
		print "All done!"

def problem_three():

	while True:
		x = raw_input("Please enter an integer: ")
		try:
			y = int(x) ** 2
		except:
			print "An error occured! Try again!"
			continue
		else:
			print 'Thanks! The number squared is: {}'.format(y)
			break 

problem_one()
problem_two()
problem_three()


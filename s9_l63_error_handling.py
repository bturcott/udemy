#s9_l63_error_handling.py
#Try Except Finally

try:
	2 + 's'
except:
	print "There was a type error!"
finally:
	print 'Finally this was printed'

#Useful when accounting for input errors
try:
	f = open('testfile1232','r')
	f.write('Test write this')
except IOError:
	print 'Error in writing to file!' #Only when it fails
else:
	print 'File write was a success' #Only when it works
finally:
	print "Always execute finally code blocks" #Always occurs

def askint():
	try:
		val = int(raw_input('Please enter an integer: '))
	
	except:
		print 'Looks like you did not enter an integer!'
		val = int(raw_input("Try again - Please enter an integer: "))
	
	finally:
		print 'Finally block exectured!'
	
	print val

askint()

def askint_2():
	while True:
		try:
			val = int(raw_input('Please enter an integer: '))

		except:
			print "looks like you didn't enter an integer!"
			continue
		else:
			print 'Correct, that is an integer!'
			break
		finally:
			print 'Finally block exectued'
		print val

askint_2():
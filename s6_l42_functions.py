#Functions
#Section 6 Lecture 42
import math

def my_func(x,y):
	"""Returns the sum of the two inputs"""
	return x + y

def is_prime(num):
	'''Simple method of checking if prime'''
	for n in range(2,num):
		if num % n == 0:
			print 'not prime'
			break
	else:
		print 'prime'

def improve_prime(num):
	'''
	Better method of checking for primes.
	'''
	if num % 2 == 0 and num >2:
		return False
	for i in range(3, int(math.sqrt(num))+1,2):
		if num % i == 0:
			return False
	return True


#x = 5
#y = 3

#print my_func(x,y)
#print help(my_func)

is_prime(16)
print improve_prime(5)

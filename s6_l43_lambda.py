#Lambda
#Section 6 Lecture 43

def squared(num):
	result = num ** 2
	return result

def square_small(num):
	return num ** 2

#Lambda square function
square = lambda num: num ** 2
print square(2)

#Sum two numbers
suming = lambda num1,num2: num1 + num2
print suming(2,4)

#Check to see if a number is even
even = lambda num: num%2 == 0
print even(5)
print even(3)

def evens(num):
	return num%2 == 0

print even(2)

#Reverse a string
rev = lambda s: s[::-1]
print rev('hello')
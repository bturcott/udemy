#Functions and Methods Homework
import math
import string

#Question 1
def vol(rad):
	return (4.0/3.0)*math.pi*(rad**3)

print vol(3)

#Question 2
def ran_check(num,low,high):
	if num >= low and num <=high:
		return True
	False
print ran_check(3,1,10)

#Question 3
def up_low(s):
	lst = [0,0]
	for letter in s:
		if letter.isupper():
			lst[0] += 1
		elif letter.islower():
			lst[1] += 1
		else:
			pass 
	print 'No. of Upper case characters : {}'.format(lst[0])
	print 'No. of Lower case characters : {}'.format(lst[1])
	return lst
print up_low('Hello Mr. Rogers, how are you this fine Tuesday')

#Question 4
def unique_list(l):
	return set(l)

print unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

#Question 5
def multiply(numbers):
	prod = 1
	for num in numbers:
		prod *= num
	return prod

print multiply([1,2,3,-4])

#Question 6
def palindrome(s):
	rev_s = s[::-1]
	if rev_s == s:
		return True
	return False
print palindrome('helleh')

#Question 7
def ispangram(strl, alphatbet=string.ascii_lowercase):
	set_strl = set(strl)
	set_alph = set(alphatbet)
	if set_alph.issubset(set_strl):
		return True
	return False

print ispangram('The quick brown fox jumps over the lazy dog')

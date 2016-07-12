#List Comprehensions
#Section 5 Lecture 38

lst = [x for x in 'word']
print lst

lst = [x**2 for x in range(0,11)]
print lst

#List comp with conditional
lst = [x for x in range(11) if x % 2 == 0]
print lst

#arithmetic
#Start with output you want and then how you will get it at the end
celsius = [0, 10, 20.1, 34.5,100]
farenheit = [ ((float(9)/5)*temp + 32) for temp in celsius]
print farenheit

#More complex
lst = [ x**2 for x in [x**2 for x in range(11)] if x % 2 == 0]
print lst
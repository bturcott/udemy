#Strings Lesson
#Section 3 Lecture 17
#strings are immutable 
#from __future__ import print_function

#print('Hello World! {}'.format(1))

#built-in string methods
my_string = "Ferrari Porsche Maserati"
print len(my_string)
my_string.upper()
print my_string
my_string.lower()
print my_string
print tuple(my_string.split()) #does not modify string rather returns a list
print my_string
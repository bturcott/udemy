#Range Function
#Section 5 Lecture 37

print range(0,10)

x = range(0,10)
print type(x)

start = 0
stop = 20
x = range(start,stop)
print x

x = range(start,stop,2)
print x

"""Generator allows the generation of generated objects that are provided at that instance
but does not store every instance generated into memory.
xrange does not create a list like range does, but instead provides a one time generation of numbers
"""
for num in range(10):
	print num

for num in xrange(10):
	print num

"""Use xrange when you don't need to save the resulting list"""

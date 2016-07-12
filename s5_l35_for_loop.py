#For Loop
#Section 5 Lecture 35
"""
num_list = [1, 2, 3,4,5]
for num in num_list:
	print num

for num in range(len(num_list)):
	print num_list[num]

# % operator known as modulo

for num in num_list:
	if num % 2 == 0:
		print num
	else:
		print 'Odd number'
"""
#Tuple examples
l = [(2,4),(6,8),(10,12)]
for tup in l:
	print tup

for (tup1,tup2) in l:
	print tup1

#Dictionary examples
d = {'k1':1,'k2':2,'k3':3}
for item in d:
	print item

#Creates a generator
for k,v in d.iteritems():
	print k 
	print v

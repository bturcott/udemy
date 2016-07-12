#Chained Comparison Operators
#Section 4 Lecture 32

#Chained Comparison
print 1 < 2 < 3
#Equivalent to above
print 1 < 2 and 2 <3

print 1 < 3

print 1 < 3 > 2
#Python is checking both comparisons due to 'and' operator
print 1 < 3 and 3 > 2

#Python only checks one as it is only looking for a 1
print 1 < 3 or 3 > 2



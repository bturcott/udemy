#Print Formatting Lesson
#Section 3 Lecture 19

x = 'Sample String'
y = 3.145

print 'Place my variable here: %s' %x
print 'Floating point number: %1.2f' %y
#first number is minimum number of digits in must contain
#second is to show how many after

#conversion format methods - two different methods similar result
print 'Convert to string %s' %(123)
print 'Convert to string %r' %(124)

#multiple examples
print 'First: %s, Second: %s' %(x,y)

#Pythonic method to do this is using the string.format method
print 'First: %s, Second: %s' %(2,2)
print 'First: {y} Second: {x}'.format(x='inserted', y='2!')

#Objects and Data Structures Assessment

#Numbers - any number value int or float
#Strings - any alphanumeric character 
#lists - collection of any number of different elements
#Tuples - immutable list
#Dictonary - Hash map, think key value pairs. key's must be unique and immutable

x = ((((100.25-.25)/100)*2)**4)+100-15.75
print x

#2/3 will produce 0 as it will be floored division
#needs to be a float to produce .66667
print 2.0/3

#Resulting type will be a float 3+1.5+4 
print type(3+1.5+4)

#You would use the ** operator
print 4 ** (1.0/2)

s = 'hello'
print s[1]

print s[::-1]

x = [0]*3
print x

x = [0,0,0]
print x
l=[1,2,[3,4,'hello']]
l[2][2] = 'goodbye'
print l
l = [3,4,5,5,6]
l = sorted(l)
l.sort()

d = {'simple_key':'hello'}
print d['simple_key']

#d=['k1']['k2']
#d=['k1'][0]['nest_key'][2]

#You can't sort a dictionary

#Tuples are immutable
#Sets remove duplicates
l = set(l)
print l

#Boolians
# False
# False
# False
# False
# False
# False



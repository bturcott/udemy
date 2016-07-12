#Lists Lesson
#Section 3 Lecture 21

my_list = [1,2,3]
print my_list

sample = ['string',3,4.21,'second string']
print sample
#Can hold different object types

print len(sample)

#Same as .append
sample += ['Hello']
print sample
sample.append('world!')
print sample

sample.pop()
print sample
#same as .pop 
sample = sample[:-1]
print sample
#Reverse list
print sample[::-1]

#same as above except modifies the list permenantly
sample.reverse()
print sample

sample.sort()
print sample
#No type or size constraint

#Nested lists
nested = [[2,3,4],[2,5,1]]
print nested[0][1]

nested_faq = [1,2,[1,2]]
print nested_faq[2][1]

#List comprehensions
first_col = [x**2 for x in range(0,10,2)]
print first_col
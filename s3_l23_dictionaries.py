#Dictionaries Lesson
#Section 3 Lecture 23
#Think of dictionaries as a hash table
#Key's must be immutable 
#dictionary is mutable
my_dict = {'key1':[1,2,3],'key2':'string'}
print my_dict['key1'][1]
my_dict['key1'].append(5)
print my_dict['key1']

print my_dict.keys()
print my_dict.values()
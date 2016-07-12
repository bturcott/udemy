#Files Lesson
#Section 3 Lecture 26
#create simple text file named test_file.txt
f = open("test_file.txt")
#print f.read()
#Returns to top of file
f.seek(0)
#print f.read()
f.seek(0)
#print f.readlines()
#readlines stores all of the data in memory

for line in open('test_file.txt'):
	print line
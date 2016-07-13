#s8_l59_OOP_special_methods.py

class Book(object):

	def __init__(self, title, author, pages):
		print "A book has been created!"
		self.title = title
		self.author = author
		self.pages = pages

	#Set apart with DUNDER!!
	#Defines how print interacts with class
	def __str__(self):
		return "Title: %s, Author: %s, pages %s " %(self.title,self.author,self.pages)
	#Defines how built in functions interact with class
	def __len__(self):
		return self.pages
	
	#Deleted automatically when the program finishes (Clears memory)
	def __del__(self):
		print "A book is gone!"

b = Book('Python','Jose',100)

print b



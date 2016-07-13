#s8_l58_OOP_inheritance.py

#Inheritance - a way to build class built on other classes

class Animal(object):

	def __init__(self):
		print "Animal Created"
	def whoAmI(self):
		print "Animal"
	def eat(self):
		print "Eating"

class Dog(Animal):

	def __init__(self):
		Animal.__init__(self)
		print "Dog Created"
	def whoAmI(self):
		print "Dog"
	def bark(self):
		print "Woof!"


d = Dog()
d.eat()
d.whoAmI()


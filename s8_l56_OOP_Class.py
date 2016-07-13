#OOP - Classes

#Simple class
class Sample(object):
	pass

x = Sample()
print type(x)

#Attribute is a characteristic of an object
#Method is an operation we can perform with the object

#Attributes
"""
self.attribute = something
__init__() - used to initalize attributes in object
"""


#Sample class with attributes
class Dog(object):

	#Class Object Attribute
	species = 'mammal'

	#Method - function inside class
	#takes in self variable
	def __init__(self,breed,name='Rover',fur=True):
		self.breed = breed
		self.name = name
		self.fur = fur

	def fetch(self):
		print self.name, "has fetched a ball!"

sam = Dog(breed = 'Lab')

#Breed amd species are attributes not methods
print sam.breed
print sam.species
print sam.name
sam.name = 'Sammy'
print sam.name
sam.fetch()




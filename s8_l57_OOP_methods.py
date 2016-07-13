#s8_l57_OOP_methods.py

#Methods - functions inside  a class. Modify the attributes of a class.

class Circle(object):

	#class object attributes
	
	#class attribute
	pi = 3.14

	def __init__(self,radius=1):
		self.radius = radius
		self.perimiter = (2 * Circle.pi * radius)

	def area(self):
		#radius**2 * pi
		return self.radius**2 * Circle.pi

	def set_radius(self,new_radius):
		"""
		This method takes in a radius and resets the current radius of the circle
		"""
		self.radius = new_radius
		self.perimiter = (2 * Circle.pi * new_radius)

	def get_radius(self):
		"""
		Returns the radius of a circle
		"""
		return self.radius

	def get_perimiter(self):
		return (2 * Circle.pi * self.radius)

c = Circle(radius=100)
print c.pi
print c.radius

print c.area()

d = Circle(10)
print d.area()

d.set_radius(5)
print d.radius
print d.area()
print d.get_radius()

print d.perimiter
print d.get_perimiter()




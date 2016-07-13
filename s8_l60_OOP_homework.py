#s8_l60_OOP_homework.py


#Problem 1
class Line(object):

	def __init__(self,coor1,coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		x_dist = (self.coor2[0]-self.coor1[0])**2
		y_dist = (self.coor2[1]-self.coor1[1])**2
		return (x_dist + y_dist)**(1.0/2)


	def slope(self):
		#rise over run
		rise = self.coor2[1]-self.coor1[1]
		run = self.coor2[0]-self.coor1[0]
		return float(rise)/float(run)

coord1 = (3,2)
coord2 = (8,10)
li = Line(coord1,coord2)
print li.distance()
print li.slope()

#Problem 2
class Cylinder(object):
	def __init__(self,height=1,radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		return (3.14 * (self.radius**2) * self.height)

	def surface_area(self):
		top_area = 3.14 * (self.radius**2)
		bot_area = 3.14 * (self.radius**2)
		side_area = 2 * 3.14 * self.radius * self.height 
		return (top_area + bot_area + side_area)

	def __str__(self):
		return "Cyclinder with a height of %s and a radius of %s" %(self.height,self.radius)

c = Cylinder(2,3)
print c.volume()
print c.surface_area()
print c
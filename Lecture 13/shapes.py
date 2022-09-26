from calculations import Calculator
from math import pi

cal = Calculator()

class Circle:	
	def __init__(self,radius):
		self.radius = radius
	def area(self):
		return cal.mul(cal.mul(self.radius,self.radius),pi)
	def circumference(self):
		return cal.mul(cal.mul(2,pi),self.radius)


circle1 = Circle(7)
# print(circle1.area())
# print(circle1.circumference())


class Parallelogram:
	def __init__(self,edges):
		if len(edges)==4 and len(set(edges))<=2:
			self.edges = edges
		else:
			print("Invalid Parallelogram")

	def perimeter(self):
		return sum(self.edges)

	def isRhombus(self):
		return len(set(self.edges))==1

par1 = Parallelogram([2,2,2,2])

print(par1.perimeter())
print(par1.isRhombus())
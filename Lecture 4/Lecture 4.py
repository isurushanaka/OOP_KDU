# class Item:
# 	def __init__(self, name: str, price: float, quantity=0):
# 		# validating input arguments
# 		assert price>=0, "invalid price"
# 		assert quantity>=0, "invalid quantity"

# 		#assign attribute values
# 		self.name = name
# 		self.price = price
# 		self.quantity = quantity

# 	def cal_total_price(self):
# 		return self.price*self.quantity

# Item1 = Item(quantity=3, price=100, name="Phone")



# class Vehicle:
# 	discount = 0.2
# 	def __init__(self, vtype:str, rate:float, hrs:float):
# 		#validate input args
# 		assert rate>=0, "Invalid rate"
# 		assert hrs>=0, "Invalid hrs"

# 		#assign attributes
# 		self.vtype = vtype
# 		self.rate = rate
# 		self.hrs = hrs
# 	def cal_total_rate(self):
# 		return self.rate*self.hrs

# 	def apply_discount(self):
# 		return self.cal_total_rate()*(1-self.discount)

# Car = Vehicle("4-wheel",100,2)
# # Car.discount=0.4
# print(Car.apply_discount())















class Vehicle:
	def __init__(self, no_wheels, colour, front_drive):
		self.no_wheels = no_wheels
		self.colour = colour
		self.front_drive = front_drive

class Truck(Vehicle):
	def __init__(self, no_wheels, colour, front_drive, trailer, canopy):
		super(Truck, self).__init__(no_wheels, colour, front_drive)
		self.trailer = trailer
		self.canopy = canopy
		self.colour=(255,255,255)

Truck1 = Truck(no_wheels=4,colour=(0,0,0),front_drive=True,trailer=True,canopy=False)
print(Truck1.colour)
class Vehicle():

	def __init__(self, location, hrs, rate, regNo):
		self.location = location
		self.hrs = hrs
		self.rate = rate
		self.__regNo = regNo
	
	def cal_total(self):
		return self.hrs*self.rate

	@property
	def regNo(self):
		return self.__regNo
	@regNo.setter
	def set_regNo(self,new_regNo):
		self.__regNo = new_regNo

class Car(Vehicle):
	def __init__(self, location, hrs, rate, regNo, nwheels):
		super().__init__(location, hrs, rate, regNo)
		self.nwheels = nwheels
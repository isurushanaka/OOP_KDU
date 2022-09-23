
class Vehicle:
	def __init__(self, Type, RegNo, Time, Price):
		self.__Type = Type
		self.__RegNo = RegNo
		self.Time = Time
		self.Price = Price
	
	@property
	def Type(self):
		return self.__Type
	
	@Type.setter
	def set_Type(self,newType):
		self.__Type = newType

	@property
	def RegNo(self):
		return self.__RegNo

	@RegNo.setter
	def set_RegNo(self,newRegNo):
		self.__RegNo = newRegNo


vehicle1 = Vehicle("Car","KT-1212",2,100)
print(vehicle1.Type)
print(vehicle1.RegNo)

vehicle1.set_Type = "new Car"
vehicle1.set_RegNo = "LH-5656"

print(vehicle1.Type)
print(vehicle1.RegNo)





# print(vehicle1.Type)
# print(vehicle1.RegNo)
# vehicle1.__Type = "Lorry"
# vehicle1.__RegNo = "Lorry"
# print(vehicle1.Type)
# print(vehicle1.RegNo)
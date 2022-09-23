
# class ProgrammingCourse():
# 	def __init__(self):
# 		self.__courseName = "Python Programming" #Private variable
# 		self.duration = "12 days"

# 	def __course_details(self): # Private method
# 		return self.__courseName



# course1 = ProgrammingCourse()
# course1.__courseName = "Java Programming"
# print(course1.__course_details())



class Item():

	def __init__(self, Name, Price, Qty):
		self.__Name = Name
		self.Price = Price
		self.Qty = Qty

	def getName(self):
		return self.__Name

	def setName(self, newName, pw):
		if pw=="abc":
			self.__Name = newName
		else:
			print("Invalid Password")

item1 = Item("Laptop",1000,5)
print(item1._Item__Name) # before changing

item1.setName("Phone","abc")
print(item1.getName()) # after changing

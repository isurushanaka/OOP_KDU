class Calculator:
	def __init__(self,):
		# print("Calculator object created")
		pass
	
	def add(self,num1,num2):
		return num1+num2

	def sub(self,num1,num2):
		return num1-num2

	def mul(self,num1,num2):
		return num1*num2

	def div(self,num1,num2):
		try:
			return num1/num2
		except Exception as e:
			print("ZeroDivisionError")

	def test(self):
		print("addition test ok") if self.add(1,2)==3 else print("addition test failed")
		print("substraction test ok") if self.sub(1,2)==-1 else print("substraction test failed")
		print("multiplication test ok") if self.mul(1,2)==2 else print("multiplication test failed")
		print("division test ok") if self.div(1,2)==0.5 else print("division test failed")

if __name__=="__main__":
	caltest = Calculator()
	caltest.test()
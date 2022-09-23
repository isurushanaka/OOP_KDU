# statement
print("my_module is being imported")


# function 1
idx = 0
def find_index(list_to_search, target):
	for idx,item in enumerate(list_to_search):
		if item == target:
			return idx
	return -1

# function 2
def test():
	print("Tesing has been completed")

'''
def find_index(list_to_search,target):
	for idx in range(len(list_to_search)):
		if list_to_search[idx]==target:
			return idx
		else:			
			if idx==len(list_to_search)-1:
				return -1
'''
# import csv

# with open('Lec_8.csv','r') as myfile:
# 	reader = csv.DictReader(myfile)
# 	items = list(reader)
# 	for item in items:
# 		print(item["name"],float(item["price"]),int(item["quantity"]))

# import sys

# def linux_interation():
# 	assert ('linux' in sys.platform), "This code runs on Linux only"
# 	print("Running the linux code")

# try:
# 	linux_interation()
# except AssertionError as e:
# 	print(e)
# except ZeroDivisionError as e1:
# 	h = 1
# except FileNotFoundError as e2:
# 	print("Make a file and try again")
# except Exception as en:
# 	print(en)




import csv

try:
	f = open('Lec_8.csv','r')
	reader = csv.DictReader(f)
	items = list(reader)
	for item in items:
		print(item["name"],float(item["price"]),int(item["quantity"]))
except FileNotFoundError as e:
	print("File is not available")
finally:
	try:
		f.close()
		print("File is closed")
	except NameError as e:
		print("File is not openned")

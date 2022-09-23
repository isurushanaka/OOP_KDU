# import my_module as mm
# from my_module import find_index, test
from my_module import *

my_list_to_search = ["Math","English","History","Science","Physics"]
my_target = "History"

index = find_index(list_to_search=my_list_to_search,target=my_target)
print(index)

test()


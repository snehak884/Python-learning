# my_list = [1, "hello", 3.14, True]
# print(my_list)  # [1, 'hello', 3.14, True]



# ✅ Python Array (array module)

# Provided by the array module.

# Can store only one type of data (all integers, or all floats, etc.).

# More memory-efficient than lists, but less flexible.


import array
my_array = array.array('i', [1, 2, 3, 4])  # 'i' means integer
print(my_array)  # array('i', [1, 2, 3, 4])

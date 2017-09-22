# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

import numpy as np

def numpy_info():
	print (dir(np))

#numpy_info()

# creating NumPy Array
my_array = np.array([1,2,3])
print(my_array)
#print(dir(my_array))

matrix_array = np.array([[1, 2], [3, 4]])
print (matrix_array)

list_array = [[1, 2],[3, 4]]

print (dir(matrix_array))
print ("\n")
print (dir(list_array))
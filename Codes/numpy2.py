# ***********************************
#  string1.pr
#  CCAM Workshop - 2017
#  Written by Arjang Fahim
#
# ***********************************

import numpy as np

data = np.loadtxt("Data/numbers.txt")
print(data)

print ("The matrix dimension is:" , data.shape)
print ("The matrix size is: ", data.size)
print ("The transpose matrix is ", data.T)
inverse = np.linalg.inv(data)
print ("The inverse matrix is ", inverse)
result = np.dot(data,inverse)
print (result)
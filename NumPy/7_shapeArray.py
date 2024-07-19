# Shape of an array : the shape of an array is the  number of element in each dimensions

# now to we will try to get a shape of the array

import numpy as np
test = np.array([[[1, 2, 3], [3, 4, 5]], [[1, 2, 3], [3, 4, 5]]])
print(test.shape)
print(test.ndim)

# now see from making 5D arry using ndim
fiveD = np.array([2, 3, 4, 5, 6], ndmin=5)
print(fiveD, "and shape is: ", fiveD.shape)

next = np.array([[[[[2, 3, 4, 5, 6], [2, 3, 4, 5, 6]]], [[[2, 3, 4, 5, 6], [2, 3, 4, 5, 6]]]]])
print(next, "and shape is: ", next.shape)

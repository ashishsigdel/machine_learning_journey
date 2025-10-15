# Array Indexing is same as array accessing.
# index start from 0 and 1, 2, 3, ...

# 1D array

import numpy
ashish = numpy.array([1, 2, 3, 4])
print(ashish[0])

print(ashish[2] + ashish[3])

# 2D array
import numpy as np
ashish = np.array([[1, 2, 3], [4, 5, 6]])
print("from 2D", ashish[0, 1])
print("from 2D", ashish[1, 2])

# 3D array
import numpy as np
threeD = np.array([[[1, 2, 3], [3, 4, 5]], [[1, 4, 9], [16, 25, 36]]])
print(threeD.ndim)
print(threeD[1, 0, 2])
print(threeD[0, 0, 2])

#4D array

import numpy as np
fourD = np.array([1, 2, 3, 4], ndmin=4)
print(fourD[0, 0, 0, 2])
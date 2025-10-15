import numpy as np

# ndarray = array object in numpy

x = np.array([1, 2, 3, 4, 5])
print(x)
print(type(x)) 


# we can pass any array like sturcture (list, tuple or other) in array() 

y = np.array((3, 4, 5, 8)) #passing tuple
print(y)
print(type(y))

# Dimensions in arrays = nested array
# 0-D Arrays
import numpy as np
x = np.array(42)
print(x)
print(type(x))

#1-D Arrays
import numpy as np
x = np.array([1, 2, 3, 4, 5])
print(x, type(x))

# 2-D
import numpy as np
x = np.array([[1,2,3], [1,4,9]])
print(x, type(x), "\n\n")

#3-D = two 2-D array
import numpy as np
x = np.array([[[1, 2, 3], [1, 4, 9] ], [[3, 4, 5], [9, 16, 25]]])
print(x)

# check dimension : ndim
import numpy as np
a = np.array(24)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1,2,3], [1,4,9]])
d = np.array([[[1, 2, 3], [1, 4, 9] ], [[3, 4, 5], [9, 16, 25]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#we can create a ndarray with required dimension as
import numpy as np
a = np.array([1, 2, 3, 4, 5], ndmin=5)
print(f"array = {a}, num of dimension = {a.ndim}, type: {type(a)}")
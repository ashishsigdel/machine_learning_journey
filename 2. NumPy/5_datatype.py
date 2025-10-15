# data type in python : integer. string. float.. boolean. complex

# data type in numpy
# i for integer
# f for float
# b for boolean
# u for unsigned integer
# c for complex float
# m for timedelta
# M for dataTime
# O for object
# S for String
# U for unicode string
# V for memory

# checking the data type of numpy array - dtype
import numpy as np
test = np.array([2, 3, 4, 5, 6])
print(test.dtype)

# checking the data type of numpy array - dtype
import numpy as np
test = np.array(["apple", "banana", "orange"])
print(test.dtype)

# creating array with defined dataatype

test = np.array([1, 3, 4, 5], dtype="S")
print(test)
print(test.dtype)

# now we will create an array with data type of 4 byte int:
import numpy as np
data = np.array([1,2, 3, 4], dtype="i4")
print(data)
print(data.dtype)

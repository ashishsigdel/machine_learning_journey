#Slicing = divide into multiple part
# [start : end] or [start : end : step]

#example
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array[1 : 5])
print(array[1 : 10 : 2])
print("End blank", array[5 : ])
print("Start blank", array[ : 5])

#negative Slicing
print("Negative Slicing...")
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# index as       [....................-3 -2  -1]
print(array[-3 : ])
print(array[-1 : -6 : -2])  # step 2 in negative

# only step
print("Only step")
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("with 3", array[::3])

# slicing 2-D array
import numpy as np
array = np.array([[1, 2, 3, 4, 5], [4, 5, 9, 45, 56]])
print(array[1, 1 : 3])

print(array[0 : 2, 2])

print(array[0:2, 2:5])
# Array Spliting : reverse of joining the array
# array_split()

# split the array in 3 parts 
import numpy as np
test = np.array([1, 2, 3, 4, 5, 6])
testNew = np.array_split(test, 3)
print(testNew)
# now split in 4 part 
testNew6 = np.array_split(test, 4)
print(testNew6)
print(testNew6[0])

# spliting the 2-D 
test2 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
testnew2 = np.array_split(test2, 3)
print("split 2-D:\n", testnew2)
print("split 2-D and element", testnew2[1])

# spliting the 2-D into three 2-D along with rows
now = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
nownew = np.array_split(now, 3, axis=1)
print("split 2-D along rows:\n", nownew)

# spliting the 2-D into three 2-D along using hsplit
now = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
nownew = np.hsplit(now, 3)
print("split 2-D with hsplit:\n", nownew)
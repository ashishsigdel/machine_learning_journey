# Array Reshaiping : change the shape of array by adding or removing the element

#reshaping 1D to 2D
import numpy as np
test = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(test.shape)
test1 = test.reshape(3, 4)
print(test1, test1.shape)

# to 3D 
test2 = test.reshape(2, 3, 2)
print("next\n", test2)

# now checking it return view or copy 
print(test.reshape(2, 3, 2).base)

# if it display original array then it is view and if it is not then it is copy
#  ==> since it display same as test, It is view.

# unknown dimension: pass -1
# we can only give one unknown dimension

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
unknown = array.reshape(2, 3, -1);
print("unknown\n", unknown)

# flattening the array by converting multidimensional array into 1D
oneD = unknown.reshape(-1)
print(oneD)

# other function which can reshape array
# ravel() : return a flattened array
# flatten() : return a copy of the array
# also rearrange the array element: rot90, flip, fliplr, flipud.

print("ravel", unknown.ravel())
print("flatten", oneD.flatten())
# sort() : is a function which sort the specified array

import numpy as np
test = np.array([3, 5, 2, 1, 7])
print(np.sort(test))

alphabet = np.array(["cat", "apple", "ball"])
print(np.sort(alphabet))

Boolean = np.array([False, True, False, True, True])
print(np.sort(Boolean))

# Sorting 2D array
test2 = np.array([[1, 5, 3], [5, 3, 8]])
print(np.sort(test2))   

test3 = test2.flatten()
print(np.sort(test3))

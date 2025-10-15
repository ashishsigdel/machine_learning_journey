# search array = using where 
import numpy as np
test = np.array([1, 2, 3, 4, 5, 4, 4])
test1 = np.where(test == 4)
print(test1)

# find index where even number stored
test2 = np.where(test % 2 == 0)
print(test2)

#searchsorted : perform binary search in array

# we will find the index where the value 7 is inserted so that array is sorted

import numpy as np
test = np.array([6, 7, 9, 10])
test1 = np.searchsorted(test, 7)
print(test1)

# search from right
import numpy as np
hello = np.array([6, 7, 8, 9, 10])
hello2 = np.searchsorted(hello, 7, side="right")
print(hello2)

import numpy as np
hello = np.array([6, 7, 1, 4, 8, 9, 10])
hello2 = np.searchsorted(hello, 7, side="right")
print(hello2)
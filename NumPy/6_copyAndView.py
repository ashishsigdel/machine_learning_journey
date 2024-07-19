# different between numpy array copy and view

# we will make a copy of array change in original array and display both

import numpy as np
data = np.array([2, 5, 6, 5, 4])
data1 = data.copy()
data[0] = 56
print(data, "and copied", data1)

# now we will make a view, change original and display both

import numpy as np
data = np.array([2, 5, 6, 5, 4])
data1 = data.view()
data[0] = 56
print(data, "and viewed", data1)

# note 
# view : original
# copy : changed
# Joining the numpy array - here we will pass concatenation

import numpy as np
baishak = np.array([1, 2, 3])
jetha = np.array([4, 5, 6])
aasar = np.concatenate((baishak, jetha))
print("concatenate:\n", aasar)

# joining of 2-D 
saun = np.array([[1, 2], [3, 4]])
bhadra = np.array([[1, 2], [3, 4]])
aasoj = np.concatenate((saun, bhadra), axis=1)
print("concatenate in 2D:\n", aasoj)

# joining array using stack function 
import numpy as np
baishak = np.array([1, 2, 3])
jetha = np.array([4, 5, 6])
aasar = np.stack((baishak, jetha), axis=1)
print("stack: \n", aasar)

# stacking along with row using hstack()
import numpy as np
baishak = np.array([1, 2, 3])
jetha = np.array([4, 5, 6])
aasar = np.hstack((baishak, jetha))
print("hstack:\n", aasar)

# stacking along with column using vstack()
import numpy as np
baishak = np.array([1, 2, 3])
jetha = np.array([4, 5, 6])
aasar = np.vstack((baishak, jetha))
print("vstack:\n", aasar)

#stacking along with height(depth)
import numpy as np
baishak = np.array([1, 2, 3])
jetha = np.array([4, 5, 6])
aasar = np.dstack((baishak, jetha))
print("dstack: \n", aasar)
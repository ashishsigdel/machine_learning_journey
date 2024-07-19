# Iterating array: going through the elements one by one or step by step 
# like for loop

# iterate element of 1-D 
import numpy as np
test = np.array([1, 2, 3, 4, 5])
for i in test:
    print(i)

#iterate element of 2-D
import numpy as np
test2D = np.array([[1, 2, 3],[4, 5, 6]])
for i in test2D:
    print(i)
# for each element
for i in test2D:
    for a in i:
        print(a)

# iterate element of 3-D 
import numpy as np
test3D = np.array([[[1, 2, 3],[4, 5, 6]], [[5, 2, 3],[4, 5, 6]]])
for i in test3D:
    print(i)

# for each element
for i in test3D:
    for a in i:
        for b in a:
            print(b)

# Iterate array using nditer() : for higher dimension to print each element it is tedious to write for loop so nditer() is used.
import numpy as np
test = np.array([[[1, 2, 3],[4, 5, 6]], [[5, 2, 3],[4, 5, 6]]])
print("\nfrom nditer\n")
for i in np.nditer(test):
    print(i)

# now with step size
import numpy as np
test = np.array([[[1, 2, 3],[4, 5, 6]], [[5, 2, 3],[4, 5, 6]]])
print("With step size.\n")
for i in np.nditer(test[:, ::2, ::3]):
    print(i)
# filter : getting some element from existing array
import numpy as np
test = np.array([41, 42, 43, 44,34, 65, 43, 45, 12])
test1 = [True, False, False, True, True, False, False, True, True]
finaltest = test[test1]
print(finaltest)

# return only greater than 42 
greaterthan42 = []
for i in test:
    if i > 42:
        greaterthan42.append(True)
    else: 
        greaterthan42.append(False)
testNew = test[greaterthan42]
print("only greater than 42:\n", testNew)


# return only even 
evenCheck = []
for i in test:
    if i % 2 == 0:
        evenCheck.append(True)
    else:
        evenCheck.append(False)

testEven = test[evenCheck]
print("Even only:\n", testEven)

# we can fitler element directly
# lets create for element greater than 42
testEmpty = test > 42
testNew = test[testEmpty]
print("directly: \n", testNew)
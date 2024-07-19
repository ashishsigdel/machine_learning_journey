import pandas as pd

var = pd.DataFrame({"A" : [1, 2, 3, 4, 5], "B" : [7, 5, 6, 8, 9]})

print(var)

var.insert(1, "python", var["A"])
print(var)

var.insert(2, "python_1", [3,2,5,3,2])
print(var)

var["python_2"] = var["A"][:3]
print(var)

#delete

var1 = var.pop("python_2")
print(var1)
print(var)
del var["A"]
print(var)
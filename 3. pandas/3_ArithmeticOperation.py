import pandas as pd
var = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [5, 6, 7, 8]})
print(var)

var["C"] = var["A"] + var["B"]
print(var)

var["D"] = var["C"] <=10
print(var)

var["E"] = var["C"] == 12
print(var)
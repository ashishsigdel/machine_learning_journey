import pandas as pd

var = pd.read_csv("./6_DemoData.csv")

# var["TITLE"] =  var["TITLE"].replace(to_replace="R380", value="hello")

# var["SN"] = var["SN"].replace([1, 2, 3, 4, 5, 6, 7, 8, 9], 100)

var["NAME"] = var["NAME"].replace(["A-Za-z"], "python", regex=True)

# inplace true to replace in original file 

print(var)
import pandas as pd

var = pd.read_csv("6_DemoData.csv")

# print(var.dropna())
# print(var.dropna(axis=1))   # 0 -> row, 1-> col

# print(var.dropna(how="all"))
# print(var.dropna(subset="RATIO"))
# print(var.dropna(inplace=True))
# print(var.dropna(thresh= 2))

# print(var.fillna("python"))
# print(var.fillna({"RATIO" : 0.50, "CHANGE" : 5.00, "TITLE" : "Untitled", "NAME" : "No name"}))
# print(var.fillna(method = "ffill"))  #forward fill
# print(var.fillna(method = "bfill"))    #backward fill
# print(var.fillna(method = "ffill", axis=1))  
# print(var.fillna(12, inplace=False))
print(var.fillna("python", limit=1))
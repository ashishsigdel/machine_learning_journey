import pandas as pd

var = pd.read_csv("6_DemoData.csv")

# print(var.interpolate())
# print(var.interpolate(method="linear", axis=0))
# print(var.interpolate(limit_direction="backward", limit=2))
# print(var.interpolate(limit="outside"))
var_1 = (var.interpolate())
print(var_1)



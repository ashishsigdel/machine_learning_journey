import pandas as pd

csv_1 = pd.read_csv("6_DemoData.csv")



# print(csv_1.index)
# print(csv_1.columns)

# print(csv_1.describe()) 
# print(csv_1.head(2))
# print(csv_1.tail(2))
# print(csv_1[:2])
# print(csv_1[6:10])
# print(type(csv_1))
# print(csv_1.index.array)
# print(csv_1.to_numpy())

# import numpy as np
# v = np.asarray(csv_1)
# print(v)

# print(csv_1.sort_index(axis=0, ascending=False))

# csv_1["TITLE"][0] = "hELLO WORLD"
# print(csv_1)

# csv_1.loc[0, "TITLE"]= "Python"
# print(csv_1)

# print(csv_1.loc[[3, 4], ["NAME", "CHANGE"]])
# print(csv_1.iloc[0, 2])
# print(csv_1.drop("NAME", axis=1))
print(csv_1.drop(0, axis=0))

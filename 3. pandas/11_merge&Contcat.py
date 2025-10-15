import pandas as pd

var1 = pd.DataFrame({"A" : [1, 2, 3, 4], "B" : [11, 12, 13, 14]})
var2 = pd.DataFrame({"C" : [1, 2, 3, 5], "B" : [21, 22, 23, 24]})

# print(pd.merge(var1, var2))
# print(pd.merge(var1, var2, on="A"))
# print(pd.merge(var1, var2, how="outer"))
# print(pd.merge(var1, var2, how="outer", indicator=True))
# print(pd.merge(var1, var2, left_index=True, right_index=True))
# print(pd.merge(var1, var2, left_index=True, right_index=True, suffixes=("name", "id")))

# Concat
sr1 = pd.Series([1, 2, 3, 4])
sr2 = pd.Series([21, 22, 34, 43])

# print(pd.concat([sr1, sr2]))

print(pd.concat([var1, var2], axis=1, join="inner", keys=["d1", "d2"]))

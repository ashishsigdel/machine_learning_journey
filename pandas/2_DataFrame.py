import pandas as pd

list = [1, 2, 3, 4, 5, 6]
dic = {"name" : ["python", "c", "javascript"], "rank" : [2, 3, 1], "popularity" : [23, 25, 34]}

var = pd.DataFrame(list)
var1 = pd.DataFrame(dic, columns=["name", "rank"], index=[1, 2, 3])

print(var)
print(var1)
print(var1["name"][3])

list_1 = [[1, 2, 3, 4, 5], [11, 12, 13, 14, 14]]
var2 = pd.DataFrame(list_1)
print(type(var2))
print(var2)

sr = {"s" : pd.Series([1, 2, 3, 4]), "r" : pd.Series([5, 6, 7, 8])}
var3 = pd.DataFrame(sr)
print(type(var3))
print(var3)
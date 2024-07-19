import pandas as pd

x = [1, 2, 3, 4,5]
var = pd.Series(x, index=['a', 's', 'd', 'f', 'g'], dtype=float)

print(var)
print(type(var))

dic = {"name" : ["python", "c", "javascript"], "rank" : [2, 3, 1]}
var1 = pd.Series(dic)
print(var1)

s1 = pd.Series(12, index=[1, 2,3,4,5,6,7,8,9])
s2 = pd.Series(11, index=[1, 2,3,4])
print(s1+s2)
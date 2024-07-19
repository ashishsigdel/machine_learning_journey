import pandas as pd

# var = pd.DataFrame({"days": [1, 2, 3, 4, 5, 6], "st_name" : ["A", "B", "C", "A", "B", "C"], "eng" : [12, 23, 12, 34, 45, 33], "maths" : [12, 23, 12, 34, 45, 33]})

# print(var.pivot(index="days", columns='st_name', values="eng"))


var = pd.DataFrame({"days": [1, 1, 1, 1, 2, 2], "st_name" : ["A", "B", "C", "A", "B", "C"], "eng" : [12, 23, 12, 34, 45, 33], "maths" : [12, 23, 12, 34, 45, 33]})

# print(var.pivot(index="days", columns='st_name', values="eng"))
print(var.pivot_table(index="st_name", columns="days", aggfunc="mean", margins=True))
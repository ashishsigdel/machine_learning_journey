import pandas as pd

dis = {"a": [1, 2, 3, 4, 5, 6], "s": [1, 2, 5, 3, 4, 6], "d" : [5, 3, 5, 6, 7, 9]}

data = pd.DataFrame(dis)

print(data)

# data.to_csv("5_testNew.csv")
# data.to_csv("5_testNew1.csv", index=False)
data.to_csv("5_testNew2.csv", header=["No. of Apple","No. of Banana","No. of Orange" ])
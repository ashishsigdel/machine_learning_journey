import pandas as pd

# csv_1 = pd.read_csv("6_DemoData.csv")
# csv_1 = pd.read_csv("6_DemoData.csv", nrows=3)
# print(type(csv_1))

# csv_1 = pd.read_csv("6_DemoData.csv", usecols=["RATIO", "NAME"])
# csv_1 = pd.read_csv("6_DemoData.csv", usecols=[0, 3])
# csv_1 = pd.read_csv("6_DemoData.csv", skiprows=[0])
# csv_1 = pd.read_csv("6_DemoData.csv", index_col=["SN"])
# csv_1 = pd.read_csv("6_DemoData.csv", header=[2])
# csv_1 = pd.read_csv("6_DemoData.csv", skiprows=[0], header=None)
csv_1 = pd.read_csv("6_DemoData.csv", dtype={"CHANGE" : "float"})





print(csv_1)
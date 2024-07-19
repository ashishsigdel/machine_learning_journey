import pandas as pd

var = pd.DataFrame({"days": [1, 2, 3, 4, 5, 6], "eng" : [12, 23, 12, 34, 45, 33], "maths" : [12, 23, 12, 34, 45, 33]})

# print(pd.melt(var, id_vars=["days"]))
print(pd.melt(var, id_vars=["days"], var_name="Subject", value_name="marks"))


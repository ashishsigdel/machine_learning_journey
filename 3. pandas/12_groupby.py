import pandas as pd

var = pd.DataFrame({
    "name": ["a", "b", "c", "d", "a", "b", "a", "b", "a", "c", "c", "d"],
    "s_1": [67, 45, 34, 55, 34, 23, 57, 76, 45, 57, 23, 89],
    "s_2": [55, 34, 23, 57, 76, 67, 45, 34, 55, 34, 23, 79]
})

var_new = var.groupby("name")
# print(var_new)

# for x,y in var_new:
#     print(x)
#     print(y)
#     print()

# print(var_new.get_group("a"))

# print(var_new.min())
# print(var_new.max())
# print(var_new.describe())

li = list(var_new)
print(li)
the_count = [1, 2, 3, 4, 5]
fruits = ["apple", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"This is {fruit}")

for i in change:
    print(f"{i}")

elements = []

for i in range (0, 10):
    print(f"Adding {i}")
    elements.append(i)

for i in elements:
    print(i)
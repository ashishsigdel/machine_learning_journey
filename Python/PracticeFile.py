from sys import argv
script, filename = argv
list = []

with open(filename, "r") as file:
    list = file.read()

nums = list.split(" ")
print(nums)
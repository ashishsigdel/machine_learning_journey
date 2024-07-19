from sys import argv

script, filename = argv

print(f"We're going to to erase the content of {filename}")
print(f"Enter ctrl + c (^C) to cancel.")
print("Press enter to continue");

# input("? ")

# print("Opening the file....")
# target = open(filename, "w")

# print("Truncating the file, Good Bye!")
# target.truncate()

# print("Now I am going to ask you three lines.")

# line1 = input("Line 1: ")
# line2 = input("Line 2: ")
# line3 = input("Line 3: ")

# print("I am going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

targeRead = open(filename)
print(f"Now Content in the {filename} is \n")
print(targeRead.read())
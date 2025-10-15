from sys import argv
import os

script, filename = argv

txt = open(filename)

print(f"Here is your {filename}")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

os.remove("aaa.txt")
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying the content of {from_file} to {to_file}")
in_file = open(from_file)
indata = in_file.read()

print(f"The input data is {len(indata)} bytes of size.")

print(f"Does the destination file exits ? {exists(to_file)}")
print("Ready, Press enter to continue, Ctrl C to abort.")
input()

out_file = open(to_file, "w")
out_file.write(indata)

print("Copied Successfully...")

out_file.close()
in_file.close()
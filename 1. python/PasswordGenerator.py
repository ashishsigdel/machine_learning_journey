import random
import string

n = int(input("Enter length of password: "))

genString = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(n):
    password = password + random.choice(genString)

print("Generated password: ", password)
if(n<6):
    print("Your password is short. May be guessable.")
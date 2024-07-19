def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1} and arg2: {arg2}")

def print_two_again(arg1, arg2): 
    print(f"arg1: {arg1} and arg2: {arg2}")

def print_one(arg1):
    print(f"One arg: {arg1}")

def no_argu(): 
    print("I'm Nothing.")

print_two("Ashish", "Sigdel")
print_two_again("Ashish", "Sigdel")
print_one("hello")
no_argu()


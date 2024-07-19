def add(a, b):
    return a + b
def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def square(a):
    return a * a

def cube(a):
    return a * a * a

def print_something(method, a):
    print(f"The result when {method} is : {a}")

print("Let's do some math with just functions!")

print_something("sum", add(3,5))
print_something("sub", sub(30,5))
print_something("multiply", multiply(3,5))
print_something("divide", divide(30,5))
print_something("square", square(5))
print_something("cube", cube(5))




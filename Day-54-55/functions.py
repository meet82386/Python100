def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

# You can give function as an argument
def calculate(function, a, b):
    return function(a, b)

print(calculate(add, 3, 5))


# You can define a function inside a function
# def outer_function():
#     print("Outer Function")
#
#     def inner_function():
#         print("Inner Function")
#
#     inner_function()
#
#
# outer_function()

# Functions can be returned from functions also

def outer_function():
    print("Outer Function")

    def inner_function():
        print("Inner Function")

    return inner_function

inner_func = outer_function()
inner_func()

# Decorator function
import time

def decorator_function(fn):
    def wrapper_function():
        time.sleep(2)
        fn()

    return wrapper_function

@decorator_function
def say_hello():
    print("Hello")

def say_bye():
    print("Bye")

say_hello()
say_bye()



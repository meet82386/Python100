
def func_info(function):
    def wrapper(*args):
        print(f"You called  : {function.__name__}({args[0]},{args[1]},{args[2]})")
        print(f"It returned : {function(args[0], args[1], args[2])}")
    
    return wrapper

@func_info
def a_function(i, j, k):
    return i + j + k


a_function(2,3,4)
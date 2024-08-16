import time

def time_calculator(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        print(f"Total {end - start} time needed")

    return wrapper


@time_calculator
def loop():
    j = 0
    for i in range(10000000):
        j = i * i

loop()
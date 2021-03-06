import time
import math

def speed_calc_decorator(function):
    def wrapper_function():
        start = time.time()
        function()
        end = time.time()
        delay = end - start
        print(f"{function.__name__} run speed was {delay} seconds.")
    return wrapper_function
    
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator        
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()


print(math.ceil(3.6))
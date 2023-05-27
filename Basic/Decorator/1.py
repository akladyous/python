from time import time
import datetime as dt


def timer(func):
    def wrapper(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print("elapsed time: ", after - before)
        return (rv)
    return wrapper


#@timer
def add(x, y=10): return x + y
add = timer(add)
print(add(20, 20))

@timer
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(5))


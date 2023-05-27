# def func1(f,*args):
#     return f(*args)
# print(func1(sum,(2,3,4)))


def percent3(val1,val2):
        return round(val1 * (1+ (1 * val2/100) ), 2)

def percent4(func,val1,val2):
    return func(val1,val2)

print(percent4(percent3,1000,20))
# -----------------------------------------------
def generate_power(exponent):
    def decorator(f):
        def inner(*args):
            result = f(*args)
            return exponent**result
        return inner
    return decorator


@generate_power(2)
def raise_two(n):
    return n

print(raise_two(7))


@generate_power(3)
def raise_three(n):
    return n

print(raise_two(5))
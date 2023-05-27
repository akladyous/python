def factorial(num):
    if num == 1:
        return num
    return num * factorial(num -1)

x=factorial(5)
print(x)
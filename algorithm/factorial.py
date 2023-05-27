
# def factorial(n):
#      return n*factorial(n-1) if n>=1 else 1

# print(factorial(6))


# def factorial(n):
#     return n * factorial(n-1) if n else 1


# def fact(n):
#     if n >= 1:
#         return n*fact(n-1)
#     else:
#         return 1
# print(fact(4))

def fact1(n):
    x=1
    for i in range(n,0,-1):
       x=x*i 
    return x
print(fact1(6))


# print([ (lambda g : g(n, 0, 1, g) ) (lambda n, a, b, f : b if n < 1 else f(n - 1, b, a + b, f)) for n in range(200)])



# x= lambda g : g(n, 0, 1, g)
# x(10)

# def f1(n,0,1,g):
#     pass

# def f2(n,a,b,f):
#     return b if n < 1 else f(n - 1, b, a + b, f)

def fibo(n):
    return (fibo(n-1) + fibo(n-2) ) if n > 1 else n

#factorial
def f(n):
    return n*f(n-1) if n else 1

#permutation without Repetition
def p(n,k):
    return f(n)/f((n-k))

#combinations without Repetition
def c(n,k):
    return f(n)/(f(k)*f(n-k))


#print(f(4))
print(p(4,4))
print(c(4,4))

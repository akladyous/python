



def outer(b):
    def inner(x,y):
        return x+y+b
    return inner

f=outer(2)
x=f(2,2)
print(x)

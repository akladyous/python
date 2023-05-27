# -
def mydecorator(func):
    def decorator():
        print('decorator1 function before execution...')
        func()
        print('decorator1 function after execution...')
    return decorator

def xfunc():
    print('function xfunc1...')
print(mydecorator)
print(xfunc)

xfunc=mydecorator(xfunc)
print(xfunc)

xfunc()


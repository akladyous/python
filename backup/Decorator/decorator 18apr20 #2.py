# --------------------------------------
def decorator2(func):
    def inner(*args):
        print('just before external function')
        # func(*args)
        print('just after external function')
        return args[0].upper()
    return inner

# func=decorator(func)
@decorator2
def func(nome):
    print(f"ciao {nome} come stai?")
    return nome
x=func('paolo')
print(x)


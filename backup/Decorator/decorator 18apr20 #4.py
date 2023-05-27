def decorator(funzione):
    def inner(value):
        value+=1
        # funzione(value)
        return funzione(value)
    return inner
# @decorator
# def func1():
#     print('func1 ...........')
# func1()
# ---
@decorator
def func2(value):
    ff=value**2
    return ff
x=func2(1)
print(x)
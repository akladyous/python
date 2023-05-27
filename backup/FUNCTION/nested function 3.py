# nested function> get final result inner function object
def ii_passaggi(value1):
    def inner(value2):
        return value1+value2
    return inner

x=ii_passaggi(10)
y=x(10)
print(y)
del x
del y
# ------------------------
def CondNestFunc(valore):
    def somma(valore1):
        return valore+valore1
    def sottrazione(valore1):
        return valore-valore1
    if valore > 10:
        return somma
    else:
        return sottrazione
    return CondNestFunc

cnf1=CondNestFunc(20)
cnf2=cnf1(2)
print(cnf2)
del cnf1
del cnf2
# ------------------------
def func1(val1,val2):
    def inner():
        return val1+val2
    return inner()
xf=func1(10,5)
print(xf)
del xf
# ------------------------
def func2(val1,val2,tester):
    def somma():
        return val1+val2
    def sottrazione():
        return val1-val2
    if tester == 1:
        return somma
    else:
        return sottrazione
    return func2

xf2=func2(10,10,0).__call__()
print(xf2)


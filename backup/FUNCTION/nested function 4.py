# def func(func):
#     return func+1
# # ----------------------------------
# def percent(num, num_percent):
#     return (num*num_percent)/100
#
# x=percent(100,12)
# print(x)
# y=func(percent(100,10))
# print(y)
# # ----------------------------------


def deco1(func):
    def deco1inner(var):
        var1 = func(var)
        var2 = var1.upper()
        return var2
    return deco1inner

def deco2(func):
    def deco2inner(var):
        dati = func(var)
        datisplit = dati.split()
        return datisplit
    return deco2inner

@deco2
@deco1
def uno(args):
    return args

print(uno("ciao a tutti belli e brutti"))
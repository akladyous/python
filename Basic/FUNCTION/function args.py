t1=(1,2,3,4,5,6,7,8,9,10)
l1=[1,2,3,4,5,6,7,8,9,10]
print("-"*40)
def myarg(*args):
    for x in range(len(args)):
        #print (type(args), len(args))
        print(args[x])
myarg(1,2,3,4,5,6, t1, l1)
print("-"*40)
def func2(msg):
    def inner():
        print("inner function - " , msg)
    return inner()

func2("test 1")
x1=func2("test 2")
print("-"*40)
def func3(val1):
    print("outer", val1)
    def inner(val2):
        print("inner", val2)
        percentage = 1 + (1 * val2 / 100)
        return round(val1 * percentage, 2)
    return inner

valore=func3(10500)
print(valore(6))
print("-"*40)
def func4(x):
    #valore = inner4(y)
    inner()
    













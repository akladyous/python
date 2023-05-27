
def multiplicatore1(x):
	def multiplicatore2(y):
		return y*x
	return multiplicatore2

m1=multiplicatore1(2)
print("funzione multiplicatore : " , m1(2))

#------------------------------------------
def outer():
        def inner(a,b):
                return a*b
        return inner

f=outer()
print ("funzione outer : ", f(2,3))

#------------------------------------------
#funzione parametro
def somma(a,b):
        return a+b
        return somma

def func(f,x,y):
        return f(x,y)
        return func

print ("parameter funcion : " , func(somma,50,50))

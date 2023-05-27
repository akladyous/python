class test1(object):
    _ninstance = 0
    listaistanze = []

    def __new__(cls, *args, **kwargs):
        if  cls._ninstance >= 6:
            raise ValueError("hai superato il numero di istanze permesso!!")
        else:
            istanza = super(test1,cls).__new__(cls)
            cls.listaistanze.append(istanza)
            print("valore istanza xx", istanza)
        return istanza
    
    def __init__(self, var1):
        self.var1 = var1
        test1._ninstance += 1

x1=test1(10)
x2=test1(10)
x3=test1(10)
x4=test1(10)
x5=test1(10)
x6=test1(10)

print('valore istanza x1', x1)
# ----------------------------------------
print(vars(x1))
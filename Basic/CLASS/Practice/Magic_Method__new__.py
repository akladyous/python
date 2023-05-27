class Test:
    InstanceLimit = 3
    InstanceList=[]
    def __new__(cls, *args, **kwargs):
        if len(cls.InstanceList) >= cls.InstanceLimit :
            raise ValueError ("supera limite massimo di istanze!")
        else:
            # istanza = object.__new__(cls)
            istanza = super(Test, cls).__new__(cls)
            cls.InstanceList.append(istanza)
            print('-' * 50)
            print('funzione __new__ istanza : ', istanza)
            print("cls.__class__.__name__" , cls.__class__.__name__)
            print('-' * 50)
            return istanza

    def __init__(self, a,b):
        self.a = a
        self.b = b
        print('funzione __init__ istanza: ', self)

x1=Test(1,2)
x2=Test(3,4)
# x3=Test(5,6)
# x4=Test(7,8)

# t1=Test.__dict__
# t2=x1.__dict__
# print(f"x1: tipo t2: {type(t1)} \n valore x1.__dict__: {t1}")
# print('-' * 60)
# print(f"x1: tipo t2: {type(t2)} valore x1.__dict__: {t2}")



#  https://howto.lintel.in/python-__new__-magic-method-explained/

class Prova:
    _contatore = 0
    _lista = [] # dev'essere inzializzata proprio lista con []
    _limit = 3
    def __new__(cls, *args, **kwarg):
        istanza = super(Prova, cls).__new__(cls)
        if (not cls._lista):
            cls._lista=[]
        if len(cls._lista) >= cls._limit:
            raise ValueError ("no more instances avaliable")
        cls._contatore += 1
        cls._lista.append(istanza)
        return istanza

    def __init__(self, var1):
        self.var1 = var1

    def __str__(self):
        return f"valore assegnato alla variabile e: {self.var1}"

    def __setattr__(self, attribute, value):
        if not attribute in self.__dict__:
            print ("peccato********")
        else:
            self.__dict__[attribute] = value

a=Prova('paolo')
# b=Prova('paolo')
# c=Prova('paolo')
# d=Prova('paolo')
print(a)

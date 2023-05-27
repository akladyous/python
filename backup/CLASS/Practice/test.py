

# class cane:
#     counter = 5
#
#     def __init__(self, vInstance):
#         self.vInstance = vInstance
#
# test1=cane(1)
# test2=cane(2)
# print(test1.vInstance)
# print(test2.counter)
# print(cane.counter)
# print(str(cane.__dict__))
# print(str(test1.__dict__))
# print(str(test2.__dict__))
class spese:
    contatore = 0
    listaistanze=[]

    def __init__(self,prodotto, prezzo, quantita):
        self.prodotto = prodotto
        self.prezzo = prezzo
        self.quanti = quantita
        spese.contatore += 1
        spese.listaistanze.append(self)

    def getprice(self):
        if hasattr(self, "discount"):
            return self.prezzo * self.discount
        else:
            return self.prezzo

    def SetDiscount(self, discount):
        self.discount = discount

    @classmethod
    def istanza(cls):
        return cls.contatore



p1=spese('mela',4,1)
p2=spese('pera',2.5,1)
p3=spese('banana',1.5,1)
p4=spese('uva',4,1)


print ("\n il prezzo prima e", p1.getprice())
p1.SetDiscount(0.5)
print ("\n il prezzo dopo e", p1.getprice())

print(type(p1))
print(isinstance(p1, spese))
xx=spese.istanza()
print(f"contatore istanza e' {xx}")

for x in spese.listaistanze:
    print(x)


# for x in p1.__dict__:
#     print(x)
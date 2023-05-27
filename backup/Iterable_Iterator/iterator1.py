# x=(1,2,3,4,5)
# def f1(*args):
#     misura=len(args)
#     for v in range(misura):
#         print(args[v])
# f1(1,2,3,4,5)


class MyIterator:
    def __init__(self,*lista):
        self.size = len(lista)
        self.valori = lista
    def __iter__(self):
        self.contatore = 0
        return 
    def __next__(self):
        if self.contatore < self.size:
            self.valore = self.valori[self.contatore]
            self.contatore += 1
            print(self.valore)

x=MyIterator(1,2,3,4,5)
x.__iter__()
x.__next__()
x.__next__()
x.__next__()

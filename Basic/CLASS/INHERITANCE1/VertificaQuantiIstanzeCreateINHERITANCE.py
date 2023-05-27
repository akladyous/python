class Base1:
    def __new__(cls, *args, **kwargs):
        istanza = super(Base1, cls).__new__(cls)
        print('istanza Base1:', istanza)
        return istanza
    def __init__(self, name):
        self.name = name
    def stampa(self):
        print("BASE1")
    def isEmployee(self):
        return False
    @staticmethod
    def prova():
        print('prova staticmode from Base1')

class Base2(Base1):
    def __new__(cls, *args, **kwargs):
        istanza2 = super(Base2, cls).__new__(cls)
        print('istanza Base2:', istanza2)
        return istanza2
    def isEmployee(self):
        return True

# n1=Base1('paolo')
# print(n1.stampa(), n1.isEmployee())
# print(help(n1))
n2=Base2('paola')
n2.prova()
# print(n2.stampa(), n2.isEmployee())
# print('-' * 60)
# print(help(n2))
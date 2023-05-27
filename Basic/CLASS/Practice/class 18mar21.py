
class Clients:
    __counter = 0
    __instances = []
    __limit = 3

    def __new__(cls, *args, **kwargs):
        if len(cls.__instances) > cls.__limit -1 :
            print('error')
        else:
            cls._inst = super(Clients, cls).__new__(cls)
            cls.__instances.append(cls._inst)
            cls.__counter += 1
            print(len(cls.__instances), cls.__counter)
            return cls._inst
    
    def __init__(self, name):
        self.name = name

# paolo = Clients('paolo')
# milena = Clients('milena')
# david = Clients('david')
# paola = Clients('paolo')


import sys
sys.tracebacklimit=0
class Test:
    def __new__(cls, a1, a2):
        print('\m************ new method ************')
        numist =  super(Test, cls).__new__(cls)

        if a1 not in ['paolo','david','paulina','milena']:
              raise ValueError ("\n\nErrore: valore non permesso")
        return numist 
   
    def __init__(self, first_name, last_name):
        print('\n************ init method ************')
        self.fname = first_name
        self.lname = last_name
    
    
    # def modify(self, name):
    #     self.fname = name
    
    @classmethod
    def prova(cls, name_str):
        print('prova', name_str)
    

t1=Test('milena','david')
Test.prova('prova')


# day, month, year = map(int, '23-10-2005'.split(('-')))
# print(day, month, year)


class House:

	def __init__(self, price):
		self.price = price
h=House
h.price = 1000

property()
# 𓂀
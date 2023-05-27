#bank account operations
class account(object):
    counter = 0
    Balance = 0

    def __init__(self , name) :
        self.name = name
        self.counter = 0

    def setbalance(self, balance=0):
        self.balance = balance
        
    def withdraw(self, amount):
        self.amount = amount
        if amount <= self.Balance :
            self.Balance -= amount
        else:
            print("importo richiesto piu alto rispetto la sua disponibilita'")
        return self.Balance

    def deposit(self, amount):
        self.amount = amount
        self.Balance += amount
        print ( "e stato versato correttamente l importo di " + str(amount) )
        #print ( "il saldo attuale del suo conto e " + self.Balance)
        return self.Balance


a1=account("paolo")
a1.setbalance()
a1.deposit(1500)
a1.withdraw(500)
print(a1.name, a1.Balance)
a1.deposit(750)
print(a1.name, a1.Balance)

class operations(account):
    counter = 0
    def __init__(self, name, operation_name):
        self.operation_name = operation_name
    


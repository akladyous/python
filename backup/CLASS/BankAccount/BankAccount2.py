import random
class Customer:
    __counter = 0
    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        x=super(Customer, cls).__new__(cls)
        return x
    def __init__(self, FirstName, LastName, DateOfBirth):
        self.c_fname = FirstName
        self.c_lname = LastName
        self.c_dob = DateOfBirth
    def __str__(self) -> str:
        return "First Name\t{}\nLast Name\t{}\nDate of Birth\t{}\n".format(self.c_fname, self.c_lname, self.c_dob)
# ---------------------------------------------------------------------------------
class BankAccount(Customer):
    __counter = 0
    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        return super(BankAccount, cls).__new__(cls)
    def __init__(self, FirstName, LastName, DateOfBirth, AccountType, Currency):
        super().__init__(FirstName, LastName, DateOfBirth)
        self.acc_type = AccountType
        self.acc_currency = Currency
        self.acc_number = BankAccount.acc_num_generator(self)
        self.acc_status = True
        self.acc_amount = 0
        self.acc_balance = 0    
    def acc_num_generator(self):
        __x= random.randint(1000,5000)
        return __x
    def Deposit(self):
        self.acc_deposit_amount = int(input("deposit amount: "))
        self.acc_balance += self.acc_deposit_amount
        print(f"current balance is: {self.acc_balance}")
        return True
    def Withdraw(self):
        var1=int(input("withdraw amount: "))
        self.acc_balance -= var1
        print(f"current balance is: {self.acc_balance}")
        return true
    def __str__(self):
        return "Account Type :\t{}\nCurrency :\t{}\nAccount Num:\t{}\nAcc.Status:\t{}".format(self.acc_type, self.acc_currency, self.acc_number,self.acc_status)

# ---------------------------------------------------------------------------------

c1=BankAccount('boula', 'akladyous', '07/10/1974','cash','usd')
print(c1)
c1.Deposit()
c1.Deposit()
c1.Withdraw()
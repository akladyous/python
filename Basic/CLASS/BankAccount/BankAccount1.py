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
    def trappola(self):
        print('trappola da Customer')
        return True
# ---------------------------------------------------------------------------------
class Account(Customer):
    __counter = 0
    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        return super(Account, cls).__new__(cls)
    def __init__(self, FirstName, LastName, DateOfBirth, AccountType, Currency):
        super().__init__(FirstName, LastName, DateOfBirth)
        self.acc_type = AccountType
        self.acc_currency = Currency
        self.acc_number = Account.acc_num_generator(self)
        self.acc_status = True    
    def acc_num_generator(self):
        __x= random.randint(1000,5000)
        return __x
# ---------------------------------------------------------------------------------
class Deposit(Account):
    __counter = 0
    __acc_deposit_type = ['cash', 'check']
    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        print(args[0])
        if not args[0] in cls.__acc_deposit_type:
            raise ValueError("deposit type not allowed")
        else:
            return super(Deposit, cls).__new__(cls)
    def __init__(self, deposit_type, amount):
        self.acc_type = deposit_type
        self.acc_amount = amount
# ---------------------------------------------------------------------------------
class Withdraw(Account):
    __counter = 0
    def __new__(cls, *args, **kwargs):
        cls.__counter += 1
        return super(Withdraw, cls).__new__(cls)
    def __init__(self, account_number, amount):
        self.acc_num = account_number
        self.acc_amount = amount




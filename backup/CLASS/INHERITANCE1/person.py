# 
class PersonalInfo:
    _counter = 0
    _lista = None

    def __init__(self, first_name, last_name, age, residence):
        self.fname = first_name
        self.lname = last_name
        self.age = age
        self.residence = residence
    
    # def __str__(self):
    #     return f"dati Personal INFO:\nNome {self.fname}\nCognome {self.lname}\nEta' {self.age}\nResidenza {self.residence}\n"
    def getInfo(self):
        print(f"dati Personal INFO:\nNome\t\t{self.fname}\nCognome\t\t{self.lname}\nEta\t\t{self.age}\nResidenza\t{self.residence}\n")

# p1=PersonalInfo('boula', 'akladyous', 46, 'florida')
# print(p1)

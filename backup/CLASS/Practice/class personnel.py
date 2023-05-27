class personnel:
    counter = 0
    def __init__(self, name, lastname, address, tel):
        self.name = name
        self.lastname = lastname
        self.address = address
        self.tel = tel
        personnel.counter += 1

    def PersonnelCard(self):
        return self.name, self.lastname, self.address, self.tel

    def ModifyCard(self):
        choice = input("wich item you want modify:  1- name 2- lastname 3-address 4- tel")
        if choice == str(1) :
            self.name = input("insert  name")
        if choice == str(2) :
            self.lastname = input("insert last name")
        if choice == str(3) :
            self. address = input("insert address")
        if choice == str(4) :
            self.tel = input("insert telephone")

#------------------------------------------------------------------------------------------------
class student(personnel):
    TypeCounter = 0
    def __init__(self, name, lastname, address, tel, course):
        super().__init__(name, lastname, address, tel)
        self.course = course
    def StudentCard(self):
        return super().PersonnelCard(), self.course
#------------------------------------------------------------------------------------------------
class teachers(personnel):
    TeachersCounter = 0
    def __init__(self, name, lastname, address, tel, subject=None):
        super().__init__(name, lastname, address, tel)
        if subject is None:
            self.subject = list()
        else:
            self.subject = subject
    def TeachersCard(self):
        return super().PersonnelCard(), self.subject



p1=personnel("boula", "akladyous", "wellington", "9548952497")
p2=personnel("milena", "akladyous", "miami", "2323232323")
p3=personnel("david", "akladyous", "new york", "4000000000")

s1=student("studente 1", "de martinez", "parma", 232039234, "nulla proprio")
s2=student("studente 2", "lupo", "cusano", 9090909090, "matematica")
s3=student("studente 3", "salvini", "roma", 1020304050, "geografia")

t1=teachers("teacher uno", "uno", "cinisello balsamo", 505050505050, ["latino", "ginastica"])
t2=teachers("teacher due", "due", "cormano", 9090909090, ["filosofia"])
t3=teachers("teacher tre", "tre", "alessandria", 2020202020, ["scienza", "arte"])


print(personnel.counter)
print(p1.PersonnelCard())
print(p2.PersonnelCard())
print(p3.PersonnelCard())
print("-"*60)
print(s1.StudentCard())
print(s2.StudentCard())
print(s3.StudentCard())
print("-"*60)
print(t1.TeachersCard())
print(t2.TeachersCard())
print(t3.TeachersCard())
print("-"*60)
p1.ModifyCard()
print(p1.PersonnelCard())
print("-"*60)
class User1:
    counter = 0
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        User1.counter += 1

class User2:
    counter = 0
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        User1.counter += 1

u1=User1('nome1', 'cognome1')
u2=User1('nome2','cognome2')
c1=User2('nome1','cognome1')
c2=User2('nome2','cognome2')

print(isinstance(u1,User2))

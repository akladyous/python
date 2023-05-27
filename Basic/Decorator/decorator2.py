# decorator without arguments ------------------------
from datetime import datetime
x=datetime.now().hour
if 15 <= datetime.now().hour < 17:
    print('orario delle 1600 del pomeriggio')

def mydecorator(func):
    def wrapper(val):
        func(val)
        if val > datetime.now().hour :
            print('hai scelta orario sbagliato!!')
        else:
            print('orario coretto!!')
    return wrapper

@mydecorator
def checktime(orario):
    print(f"l'orario e: {orario}")

checktime(15)

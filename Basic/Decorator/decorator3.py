# decorator with arguments ------------------------
from datetime import datetime

def mydecorator(func):
    def wrapper(val):
        return func(val)
        # if val > datetime.now().hour :
        #     print('hai scelta orario sbagliato!!')
        # else:
        #     print('orario coretto!!')
    return wrapper
@mydecorator
def checktime(orario):
    # print(f"l'orario e: {orario}")
    return f"{orario}"

x=checktime(19)
print(x)

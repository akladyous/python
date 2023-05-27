credit = 10
attempts = 1
vincita = 1


def add(val1,val2):
    return val1 + val2
    return add

def subtract(val1, val2):
    return val1 - val2
    return subtract

def f_dobalance(operazione, a_credit, a_attempts):
        global credit
        global attempts
        global vincita
        return operazione(a_credit, a_attempts)
        return f_dobalance




f_dobalance(subtract,credit, attempts)

f_dobalance(add,credit,vincita)

print (credit)
print(attempts)
print(vincita)




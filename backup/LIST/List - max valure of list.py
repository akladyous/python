l1 = [1, 2, 3904, 5, 2310, 22, 90, 607, 540, 980,3905]
l2=l1.copy()

def maggiore(lista):
    dato = lista[0]
    for x in lista:
        if x > dato:
            dato = x
    return dato

def minore(lista):
    dato = lista[0]
    for x in lista:
        if x < dato:
            dato = x
    return dato

print("il numero maggiore della lista e : ", maggiore(l1))
print("il numero miore della lista e : ", minore(l1))

print ("lista l1 : ", l1)

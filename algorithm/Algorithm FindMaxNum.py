
# lista = [13,10,14,12,0,2,4,9,5,1,7,3,0,0,1,2]
lista = [13,10,14,12]
def find_max(items):
    if len(items) == 1 :
        return items[0]

    op1 = items[0]
    op2 = find_max(items[1:])

    if op1 > op2:
        return op1
    else:
        return op2

print(find_max(lista))
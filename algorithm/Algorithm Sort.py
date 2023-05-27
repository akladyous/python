lista=[9,10,11,12,0,2,4,9,5,1,7,3]

def insertionsort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while (i >=0) and (A[i] > key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

insertionsort(lista)
print (lista)

lista=[13,10,14,12,0,2,4,9,5,1,7,3,0,0,1,2]
def sortlog(vlist):
    for x in range(1, len(vlist)):
        j=x-1
        key = vlist[x]
        while j >= 0 and vlist[j] > vlist[j+1]:
            vlist[j+1] = vlist[j]
            vlist[j] = key
            j = j - 1

sortlog(lista)
print(lista)


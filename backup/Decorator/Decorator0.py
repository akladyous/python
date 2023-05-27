data = list()
f=open("/Users/boula/Dropbox/Archivio/Python/Decorator/pnr.txt","r")
data = f.readlines()
f.close()
#data.sort()
print (data)

#def dspacedel(funzione):
#    def sspacedel(lista):
#        for line in lista:
#            stringa = 'pnr : ' + line
#            print(stringa)
#            lista.remove(line)
#            lista.append(stringa)
#            stringa = ''
#        funzione(lista)
#    return sspacedel


def decoratore(lista):
    def inner():
        for line in lista:
            stringa = 'pnr : ' + line
            print(stringa)
            lista.remove(line)
            lista.append(stringa)
            stringa = ''
    inner()

@decoratore
def spacedel(lista):
    for x in range(len(lista)):
        for line in lista:
            stringa = line.strip()
            lista.append(stringa)
            lista.remove(line)

spacedel(data)

data.sort()
print(data)

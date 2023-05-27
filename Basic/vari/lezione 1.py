alfa = "abcdefghijklmopqrstuwxyz"

def contrario(stringa):
    indice = len(stringa) - 1
    nuova_stringa = ""
    while indice >= 0:
        nuova_stringa = stringa[indice]
        print (nuova_stringa)
        indice -= 1
        print (indice)
        
    print (nuova_stringa)
        


contrario(alfa)

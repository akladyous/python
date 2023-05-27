p1=[]
p2=[]

while True:
    classe=input('inserive la classe oppure STOP : ')
    tasse=input('inserice il valore delle tasse: ')
    if classe.upper()!='STOP' and tasse.upper()!='STOP':
        p1.append(classe)
        p2.append(tasse)
        print(p1)
        print(p2)
    else:
        print('fine')
        break

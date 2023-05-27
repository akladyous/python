nome=input("ciao... come ti chiami ???")

if nome.upper() == "DAVID":
    print ("ok david")
else:
    print ("mi spiace KO")

listadavid=[]

for x in range(4):
    print("il numero del contatore attuale e: ", x)
    namelist = input("insert you name :")
    listadavid.append(namelist)
    print("il nome che hai inserito e: ", namelist)
print("*"*60)
print ("la lsita attuale e ")
print ( listadavid)
print ("fine programma numero 2")
print("*"*60)
for x in listadavid:
    print ("il dato e : ", x)
    if x.upper() == "DAVID":
        print ( " hai vinto il premio selezionato.. auguri")
        
        




    
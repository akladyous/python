inventario = list()

def creatitems():
    while True :
        items = input("insert item :")
        if items == "stop":
            break
        else:
            inventario.append(items)
    print(inventario)

def ilista():
    while True:
        items = input ("insert item ")
        if items == "stop" :
            break
        else:
            inventario.append(items)
    print ( inventario )


def isrepete(valore):
    vr = inventario.count(valore)
    if vr > 1:
        print("valore repetuto " + str(vr) + " volte")
    else:
        print("valore non ripettuto")

def delitem(valore):
	while inventario.count(valore)>1:
		inventario.remove(valore)


creatitems()

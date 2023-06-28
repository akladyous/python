eta = input("quanti anni hai")
patente = input("hai la patente")


print("la tua eta è di " + str(eta))

if int(eta) >= 18 and patente == "si":
    print("sei maggiorenne \n puo nolleggiare una macchina")
elif int(eta) >= 18 and patente != "si":
    print("sei maggiorenne \n ma non puoi nolleggiare una macchina")
else:
    print("sei minoorenne")

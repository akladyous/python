# sum numbers on list
lista = list()
duplist = list()
newlist = list()

while True:
		val = input("insert item : or nn to Exit program ")
		try:
				lista.append(int(val))
				print(lista)
		except:
				if str(val) != "nn":
						print("valore non ammesso !!!")
				else:
						print("fine programma")
						break


def ListDupItems(ListName): u
	for x in range(len(ListName)):
    if ListName.count(x) > 1:
	    return True
    return False


vsum = 0
multiplicator = 1
lodd = list()
leven = list()

try:
		for x in range(len(lista)):
				multiplicator = multiplicator * int(lista[x])
				vsum = vsum + int(lista[x])
				if int(lista[x]) % 2 == 0:
						lodd.append(x)
				else:
						leven.append(x)

		print("--------------------------------------")
		print("avarage numero in list is :", int(vsum / len(lista)))
		print("highest number in list is :", max(lista))
		print("lower number in list is :", min(lista))
		print("list numbers multiplication :", multiplicator)
		print("there are ", str(len(lodd)), "odd numbers")
		print("there are ", str(len(leven)), "even numbers")
except:
		print("not enough elements to excute program ")

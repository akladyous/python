myList = [[32, 12, 52, 63], [32, 64, 67, 52], [64,64,17,34], [17, 76, 98]]
myset=set()
# mySet = set(i for j in myList for i in j)

# for x in myList:
#     myset.add(tuple(x))
myset=set(tuple(x) for x in myList) # cancella e crea un nuovo set
print(myset)
print('*' * 50)
myset=set()
myset.add(999)
myset.update(set(tuple(x) for x in myList))
print(myset)

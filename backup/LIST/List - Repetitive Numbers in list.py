l1 = [1, 2, 3904, 5, 2310, 22, 90, 607, 540, 980,0,0,0,0,0]

for x in l1 :
    NumCount = l1.count(x)
    if NumCount > 2:
        print("--- 2 volte")
        for xz in range(NumCount-1):
            l1.remove(x)
    elif NumCount == 2:
        l1.remove(x)
print(l1)

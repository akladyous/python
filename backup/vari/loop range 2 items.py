l1 = [1, 2, 3, 4, 5]
l2 = ['one', 'two', 'three', 'four', 'five']
l3 = ['a', 'b', 'c', 'd', 'e']
l4 = ['uno', 'due', 'tre', 'quattro', 'cinque']

l1234=list(zip(l1,l2,l3,l4))
for w,x,y,z in zip(l1,l2,l3,l4):
    print(w,x,y,z)



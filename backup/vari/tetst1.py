l1=['a','b','c']
l2=[1,2,3]
mix=[]
for x in l1:
    for y in l2:
        if x != y:
            mix.append((x,y))


l1l2=[(x,y) for x in l1 for y in l2 if x!=y]

print(l1l2)


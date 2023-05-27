# a = [[1,2],[3,4],[5,6],[7,8],[9,10]]
# b=[]
# for x in a:
#     for xs in x:
#         b.append(xs)
# print (b)
# print("-"*30)
# c=[]
# #la stessa in formato list comprehension
# c=[x for xs in a for x in xs]
# print(c)
# print("-"*30)
# ------------------------------------------------------------------------------------
from typing import List

l1 = [1, 2, 3, 4, 5]
l2 = ['one', 'two', 'three', 'four', 'five']
l3 = ['a', 'b', 'c', 'd', 'e']
l4 = ['uno', 'due', 'tre', 'quattro', 'cinque']

print ('4 compressed lists in new list comprehension .................')
ll1 = [[w, x, y, z] for w in l1 for x in l2 for y in l3 for z in l4]
# [1, 'one', 'a', 'uno'], [1, 'one', 'a', 'due'], [1, 'one', 'a', 'tre']
print (ll1)
print ('')

print ("stessa lista uncompressed................")
ll1u = [x for y in ll1 for x in y]
print (ll1u)
print ('')
print ('stessa lista uncompressed senza lista comprehension...')
nll1 = []
for x in ll1 :
    for y in x :
        nll1.append (y)
print (nll1)
print ("-" * 30)
print ('')

# ------------------------------------------------------------------------------------
print ('valore lista LL2 e :  nested list comprehension .....')
ll2 = [[[w, x], [y, z]] for w in l1 for x in l2 for y in l3 for z in l4]
# [[1, 'one'], ['a', 'uno']], [[1, 'one'], ['a', 'due']], [[1, 'one'], ['a', 'tre']], [[1, 'one']
print (ll2)
print ('')

print ('stessa lista senza list comprehensione......... NLL2')
nll2 = []
for x in ll2 :
    for y in x :
        for z in y :
            nll2.append (z)
print (nll2)
print ('')
# ll2u=[valore for componente in ll2 for valore in componente for valore in componente]
print ('LL2U nested list comprehension......................')
# print(ll2u)
print ("-" * 30)
# ------------------------------------------------------------------------------------
pd: List[str] = ["Pari" if num % 2 == 0 else "Dispari" for num in range (1, 11)]
# ------------------------------------------------------------------------------------

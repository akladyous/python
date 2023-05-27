# 26 ottobre 2020 //
from typing import List, Any

l1 = [[1, 2, 3], [3,2,1], [2,1,3], [5,6,7],[9,8,2]]
l2: list[Any]=list()
s1 = set()
t1 = tuple()
result = list()
#------------------------------------------------------------
# solution number 1 without list comprehension
#------------------------------------------------------------
# for x in l1:
    # t1=tuple((sorted(x)))           #<--|
    #                                     | soluzione uno !!!
    # s1=s1.union({t1})               #<--|
    #--------------------------------------------------------
    # s1 = s1 | {tuple(sorted(x))}      #<--|
    #                                       | soluzione due !!!
    # l2=s1                             #<--|
    # -------------------------------------------------------
    # l2 = s1 = s1 | {tuple(sorted(x))}   #<--| soluzione tre !!!
#------------------------------------------------------------
# soluzione con list comprehension
#------------------------------------------------------------
l2=list(set(tuple(sorted(x)) for x in l1))
print(l2)
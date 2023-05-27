import itertools


l1=[x for x in range(10)]

vzip1=list(zip(itertools.count(start=0, step=1), l1))
print(vzip1)


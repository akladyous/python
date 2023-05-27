import itertools


l1=[x for x in range(10)]

vzip2=list(zip(itertools.zip_longest(range(15), l1)))
print(vzip2)


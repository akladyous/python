import itertools

list1=[x for x in range(10)]

data1=list(itertools.zip_longest(list1, range(11)))
print(data1)

data2=list(itertools.zip_longest(range(15), list1))
print(data2)
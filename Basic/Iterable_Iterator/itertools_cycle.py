import itertools

l1=[x for x in range(10)]

x=itertools.cycle(('on','off'))

print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
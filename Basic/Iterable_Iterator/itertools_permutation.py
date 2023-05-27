import itertools

lista=['boula', 'paulina', 'milena', 'david']
result = itertools.permutations(lista, 2)
print(list(result))

print(list(itertools.permutations(['a','b','c','d'],2)))

# print(list((itertools.combinations((0,1,2,3,4,5,6,7,8,9),4))))

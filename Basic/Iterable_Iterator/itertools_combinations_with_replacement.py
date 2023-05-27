import itertools

# alfa = l=[chr(x) for x in range(97,124,1)]
# lista=list((itertools.combinations_with_replacement((0,1,2,3,4,5,6,7,8,9),4)))
alfa=['a','b','c']

result = itertools.combinations_with_replacement(alfa, 2)
print(list(result))
# frase='ciao'
# l1=[(ord(x), ord(y)) for x in frase for y in frase]
# print(l1)

# l2=list()
# for x in range(3):
#     for y in range(3):
#         l2.append((x,y))
# print(l2)
# l2=[(x,y) for x in range(3) for y in range(3)]
# print(l2)
# #
# ShoppingList = list()
# stock = ['Radishes', 'Snow Peas', 'tomato', 'Zucchini', 'Peas Green', 'Pepper', 'okra', 'Eggplant',
#          'Broccoli', 'onion', 'peanuts']
# ShoppingList[:] = [item for item in stock if item not in ShoppingList]
# print(ShoppingList)
#
ShoppingList = list()
qty=[1]
stock = ['Radishes', 'Snow Peas', 'tomato', 'Zucchini', 'Peas Green', 'Pepper', 'okra', 'Eggplant',
         'Broccoli', 'onion', 'peanuts']
ShoppingList[:] = [[item,quantity] for item in stock if item not in ShoppingList for quantity in qty]
print(ShoppingList)

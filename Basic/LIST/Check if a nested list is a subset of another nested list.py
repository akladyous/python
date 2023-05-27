from typing import Set, Union, Tuple

l1 = [[2, 3, 1], [4, 5], [6, 8]]
l2 = [[1,4, 5], [7,9],[6, 8,0],[8,6]]

set1: set[Union[tuple[int, int, int], tuple[int, int]]] = {(2,3,1), (4,5), (6,8)}
set2 = {(4,5), (6,8)}
set3 = set()

def checksubset(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if sorted(y) == sorted(x):
                result = True
    return result

print(f"the result of 2 list's comparison is {checksubset(l1,l2)}")

# for x in list2:
#     for y in list1:
#         result = set([tuple(y)]).issubset([tuple(x)])
#         if result == True :
#             print("risultato True")
#             break
#         else:
#             print("risultato False")



# print(result)
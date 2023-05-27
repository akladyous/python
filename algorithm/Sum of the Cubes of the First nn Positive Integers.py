# Sum of the Cubes of the First nn Positive Integers
#   pow(x,2) * pow((n+1),2)
#   -----------------------
#           2


from math import pow


def sum_cubic_first_positive_intiger(nums):
    return (pow(max(nums),2) * pow((max(nums)+1), 2)) / 4

l1 = list(range(1,201))
print(sum_cubic_first_positive_intiger(l1))





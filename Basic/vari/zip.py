from itertools import zip_longest

a1 = [1, 2, 3]
a2 = [4, 5, 6, 7, 8, 9, 10]

arr_shortest = list(zip(a1, a2))
print(arr_shortest)

arr_longes = list(
    zip_longest(
        a1,
        a2,
        fillvalue=None,
    )
)
print(arr_longes)

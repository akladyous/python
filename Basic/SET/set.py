import random

s1 = {1, 2, 3}

s1.add(4)
print(s1)
s1.clear()
print(s1)
print(len(s1))
print("-" * 50)

random_set1 = {random.randint(1, 100) for _ in range(10)}
random_set2 = random_set1.copy()
print("set.copy() {}".format(random_set2))
print("-" * 50)


s1 = {1, 2, 3, 4, 5}
s2 = {3, 4}
print(s1, s2)
print("set.difference : {}".format(s1.difference(s2)))
print("-" * 50)

A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 11}
set_diff_update = A.difference_update(B)
print(set_diff_update)

char1 = {"a", "b", "c", "f"}
char2 = {"d", "e", "f", "a"}
symmetric_diff = char1.symmetric_difference(char2)
print(sorted(symmetric_diff, key=lambda c: ord(c)))

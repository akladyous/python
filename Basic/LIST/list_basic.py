import random

l1 = [x for x in range(10)]
l1.append(10)
l1.insert(len(l1),len(l1))
print(l1)


random_numbers = [random.randint(1, 100) for _ in range(10)]

print(random_numbers)



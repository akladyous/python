from collections import Counter

c1 = Counter('abc')
print(c1)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
c2 = Counter(car)
print(c2)
print(c2['price'])

words_list = ['Cat', 'Dog', 'Horse', 'Dog']
c3 = Counter(words_list)
print(c3)


def add(x, y):
    return x+y


print(add.__closure__)

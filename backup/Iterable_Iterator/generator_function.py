

def genfunc():
    for x in range(5):
        yield x
        if x >5:
            return x

x=genfunc()
print(x)
for x in x:
    print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
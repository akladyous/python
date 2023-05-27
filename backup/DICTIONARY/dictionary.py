dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = dict()
for x in range(3):
    dic4.update(dic1)
    dic4.update(dic2)
    dic4.update(dic3)
print(dic4)
#
dic5 = dict()
for x in range(10):
    dic5.update({x: x * x})

print(dic5)
#
dic6 = dict()
for x in range(len(dic5)):

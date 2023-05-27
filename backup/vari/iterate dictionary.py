d1={1: 'nissan', 2: 'renault', 3: 'merceders', 4: 'mazda', 5: 'hyundai' }
d2={'color': 'black', 'year': '2020', 'alimentation': 'gas', 'option': 'full', 'change': 'auto'}
print(d1)
print(d2)

for (k1,v1), (k2,v2) in zip(d1.items(),d2.items()):
    print(k1,v1)
    print(k2,v2)
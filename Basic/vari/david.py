valore = input("Number? ")

if int(valore) > 10:
    print("PIU DI 10")
else:
    print("MENO DI 10")


print("ciao")


l1 = ['num uno', 'num due', 'num tre', 'num quattro', 'num cinque',
      'num sei', 'num sette', 'num otto', 'num nove', 'num dieci']
l2 = [x.replace(' ','_') for x in l1]
print(l2)

x= enumerate(l1)
print(x)
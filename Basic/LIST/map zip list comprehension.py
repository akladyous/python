
d1={'uno': 1, 'due': 2, 'tre': 3, 'quattro': 4, 'cinque': 5}
d2={'sei': 6, 'sette': 7, 'otto': 8, 'nove': 9, 'dieci': 10}
d3={'uno': 100, 'due': 110, 'tre': 120, 'quattro': 130, 'cinque': 140, 'sei': 140, 'sette': 150, 'otto': 160, 'nove': 170}


cities = ["miami", "madrid", "milan", "new york", "paris", "zurigh"]  #lista citta
airports = ["mia", "mad", "mil", "nyc", "par", "zrh"] #lista aeroporti
airline = ["alitalia", "swissair", "delta", "american"]

ozip = zip(cities, airports)
oziplist = list(ozip)
print (oziplist)

def union(par1,par2,par3):
    testo = par1 + " " + par2 + " " + par3
    return testo.upper()

rs = list(map(union, cities, airports, airline))

print (rs)

lista1=[oziplist[x][0]+" "+ oziplist[x][1] for x in range(len(oziplist))]
print ("list comprehension uno",)
print (lista1)

lista2 = [(x,y) for x in cities for y in airports]
print ("list comprehension due`",)
print (lista2)

#dictionary comprehension
l1=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
l2=[1,2,3,4,5,6,7,8,9,10]
d4={key: value for key, value in zip(l1,l2)}
print ("dictionary comprehension")
print (d4)

# funziona per calcolare la percentuale di un valore
def percentage(val, percent):
    percentuale = 1 + (1 * percent / 100)
    return round(val * percentuale, 2)


d1 = {
    "uno": 100,
    "due": 110,
    "tre": 120,
    "quattro": 130,
    "cinque": 140,
    "sei": 140,
    "sette": 150,
    "otto": 160,
    "nove": 170,
}

# d2={(key.capitalize(): value() for (key, value) in map(percentage(value, 10), d1) }

d2 = {}
for chiave, valore in d1.items():
    d2[chiave] = valore + 1
print(d2)

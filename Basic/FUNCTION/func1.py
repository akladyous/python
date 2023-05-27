l1=[1,2,3,4,5,6,7,8,9,10]
d1={"uno": 100, "due": 200, "tre": 300, "quattro": 400, "cinque": 500}

def percent2(basic_value, percent_value):
    def percentage_operation():
        return round(basic_value * (1+ (1 * percent_value/100) ), 2)
    return percentage_operation()

d1={"uno": 100, "due": 200, "tre": 300, "quattro": 400, "cinque": 500}

for chiave, valore in zip(d1.keys(), d1.values()):
    d1[chiave]=percent2(valore, 15.5)
print(d1)

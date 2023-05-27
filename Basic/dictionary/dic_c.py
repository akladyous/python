l1=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
l2=[1,2,3,4,5,6,7,8,9,10]

d1={"a": 20,"b": 30, "c": 40, "d": 50, "e": 60, "f": 70, "g": 80, "h": 90, "i": 100}

d2={key: val for key, val in d1.items() if val > 20 and val < 80 }
print ("dictionary comprehension from dictionary FILTERED")
print (d2)

d3={key: val for key, val in zip(l1, l2)}
print ("dictionary comprehension from LIST")
print (d3)

d4={key: val for key, val in zip(l1,l2) if val <6 }
print ("dictionary comprehension LIST with FILTER")
print (d4)


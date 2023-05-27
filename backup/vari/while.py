stato = True
val = 0
array=list()
while bool(stato)== True:
    val = input("insert value to append to array ")
    array.append(val)
    stato = bool(input("vuoi continuare ? True or False "))
    if stato == bool(True):
        print("stato true")
        continue
    else:
        break

print(f"ciao a tutti")
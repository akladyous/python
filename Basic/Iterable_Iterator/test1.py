

even=[2,4,6,8,10,12,14,16,18,20]
it_even=iter(even)

while True:
    try:
        x=next(it_even)
        print(x)
    except StopIteration:
        break

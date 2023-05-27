lpass = list()
lpass.append('Alejandro2310')
lpass.append('Milena 1102')
lpass.append('23102005')

def sp(word):
    for x in range(len(word)):
        print ('count number : ' + str(x))
        for y in word[x]:
            print ('valore : ' + y)
            if y.isspace():
                print ('space chr found !!')
                return True
                
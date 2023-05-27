lista=set()
while True:
    classe=input('inserisce la classe oppure No per terminare: ')
    if not classe.upper()=='NO':
        lista.add(classe)
    else:
        print(lista)
        print('fine programma')
        break

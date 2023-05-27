def riempi_classe():
    classe = []
    while True :
        nome_classe = input('inserice il nome della classe :')
        if nome_classe == 'nn':
            break
        else:
            classe.append(nome_classe)
            print('la lista delle classe sono i seguneti: ' + str(classe))


riempi_classe()

    

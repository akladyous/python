
lista=[]

while True :
    x=input('vuoi inserire un nuovo prodotto : ')
    if x.upper()== 'SI':
        prodotto = input('inserisce il prodotto: ')
        prezzo = input('inserisci il prezzo: ')
        fee = input('inserisci le commissioni : ')
        lista.append([prodotto,prezzo,fee])
        print(lista)
        
    else:
        print('niente')
        break
    
    
        

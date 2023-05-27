import random

jolly = 0
playlist = []
credit = 10
attempts = 0
vincita = 0


print("welcome to Dice Rolling Simulator..")
print("your have " + str(credit) + " dollar at your disposal .. each attempt costs 1$")
print("for every win you earn 1$\n")

def f_credit_ok():
    global credit
    global attempts
    if attempts <= credit:
        return True
    else:
        return False



while True:
    valore = str(input("vuoi continuare a giocare ?? "))
        if f_credit_ok() == True and :

            if valore.upper() == "YES":
                print ("------------------------------------------------------------")
                attempts = int(input("how many times you would like to play ? "))
                jolly = int(input("choose a (jolly) number to play from one to six: \n"))
                if f_credit_ok() == True:
                    credit -= attempts

                    for x in range(attempts):
                        dice = random.randint(1,6)
                        playlist.append(dice)
                        #print("------------------------------------------------------------")
                        print ("tentativo numero : (" + str(x+1) + ") " + "di  (" + str(attempts) + ")")
                        print ("il numero del dado è : " + str(dice))
                        print("------------------------------------------------------------")

                        if dice == jolly:
                            credit += 1
                            vincita += 1
                            print("hai vinto; il tuo credito sara aumentato di 1 dollaro")
                            print("------------------------------------------------------------")
                        counter = attempts - x
                        if counter == 1:
                            print("------------------------------------------------------------")
                            print("hai raggiunto i tuoi ( " + str(attempts) + " ) tentativi ")
                            print("il tuo saldo è " + str(credit))
                            print("fine del gioco ----------")
                            print("------------------------------------------------------------")
            else:
                print("------------------------------------------------------------")
                print("il tuo saldo è " + str(credit))
                print("fine programma")
                break
        else:
            print("hai finito il tuo credito... il tuo saldo attuale è di " + str(credit))
            print("hai  fatto ( " + str(vincita) + " ) vincità")
            for x in range(len(playlist)):
                print(" tentativo numero ( " + str(x+1) + " ) - numero jolly è ( " + str(playlist[x]) + " )")
            print("end program")






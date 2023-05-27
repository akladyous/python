class studenti:
    numero_studenti = 0
    
    def __init__(self, nome, cognome, eta, colore):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.colore = colore
        studenti.numero_studenti += 1
    
    def scheda_personale(self):
        return self.nome, self.cognome, self.eta, self.colore


studente1=studenti("boula", "akladyous", 45, "nero")
studente2=studenti("milena", "akladyous", 18, "bianco")
studente3=studenti("david", "akladyous", 14, "bianco")


print(studente1.scheda_personale())
print(studenti.numero_studenti)

for x in range(studenti.numero_studenti):
    nstudent =""
    





class animale:
    counter = 0
    def __init__(self,nome):
        animale.counter += 1
        self.nome = nome
    def info(self):
        print ("il nome dell'animale e: {}".format(self.nome))
    @classmethod
    def istanze(cls):
        print(cls.counter)

class tipo(animale):
    def __init__(self, nome, tipo):
        super().__init__(nome)

class razza(tipo):
    def __init__(self, nome, razza):
        super().__init__(nome)
        self.razza = razza

a1=animale('bobby')
a1.info()
t1=tipo('lulu', 'cane')
t1.info()
animale.istanze()

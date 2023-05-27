class School:
    counter=0
    def __init__(self, nome):
        School.counter += 1
        self.nome = nome

    @classmethod
    def istanze(cls):
        print(cls.counter)

s1=School('paolo')
print(s1.nome)

s2=School('paulina')
print(s2.nome)

School.istanze()
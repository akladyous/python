# class AirLine:
#     contatore = 0
#     def __init__(self, name,iata_code, iata_name):
#         self.name = name
#         self.iata_code = iata_code
#         self.iata_name = iata_name
#         AirLine.contatore += 1
#     @classmethod
#     def istanze(cls):
#         return cls.contatore

# az=AirLine('alitalia', 55, 'az')
# lx=AirLine('swiss air', 724, 'lx')
# ms=AirLine('egyptair', 77,'ms')
# lh=AirLine('lufthansa', 220, 'lh')

# co=AirLine.istanze()
# print(f"numero istanze nella classe {co}")
# print(f"check AZ is instance of {isinstance(az,AirLine)}")

    # ----------------------------------------------------------------
class Clienti:
    __contatore  = 0
    __clienttype = ['customer', 'agency',]

    def __init__(self, fname, lname, dob, tel, client):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.tel = tel
        if (client not in Clienti.__clienttype):
            raise ValueError ("tipo cliente sbagliato!!!")
        else:
            self.client = client
        Clienti.__contatore += 1

    def ModifyTel(self, nTel):
        if hasattr(self, "tel"):
            setattr(self, 'tel', nTel)
            # oppure usare la forma literal come la seguente riga
            # self.tel = nTel
        else:
            raise ValueError("valore non esistente!")

    @classmethod
    def getclient(cls):
        return cls.__clienttype
    @classmethod
    def instanze(cls):
        return cls.contatore
    
    @staticmethod
    def getclasscounter():
        return Clienti.__contatore

c1=Clienti('boula', 'akladyous', '10jul74', 3401280777,'customer')
c1.ModifyTel('230230230')
print(c1.tel)
print(Clienti.__con)
print(c1.getclient())

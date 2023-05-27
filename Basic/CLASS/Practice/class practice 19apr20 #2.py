class School:
    related = 'famiglia'

    def __init__(self, name, school_name, matricola):
        self.name = name
        self.school_name=school_name
        self.matricola = matricola

    def description(self):
        return "nome : {} Scuola {} Matricola: {}".format(self.name, self.school_name, self.matricola)

s1=School('david','media',"2310")
s2=School('milena','superiore',"1102")
s3=School('paulina','latina academy','2103')
s4=School('paolo','python school','1007')
s4.related = 'amici'

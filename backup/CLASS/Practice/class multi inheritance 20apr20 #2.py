class families:
    f_counter = 0
    def __init__(self, family_name):
        families.f_counter += 1
        self.family_name = family_name
    @classmethod
    def istanze(cls):
        print(cls.f_counter)

class householders(families):
    h_counter = 0
    def __init__(self, family_name, house_holder):
        householders.h_counter += 1
        families.__init__(self, family_name)
        self.house_holder = house_holder
    @classmethod
    def istanze(cls):
        print(cls.h_counter)

f1=families('akladyous')
f2=families('teran lopez')
f3=families('piazzola')
h1=householders('akladyous', 'paolo')
h2=householders('teran lopez', 'paulina')

families.istanze()
householders.istanze()

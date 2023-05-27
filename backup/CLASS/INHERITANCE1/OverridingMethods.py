class Parent:
    def funzione(self):
        print('Posizione : Parent.Funzione')
class Child(Parent):
    def funzione(self):
        print('Posizione : Child.Funzione')
        super(Child, self).funzione()
class Nephews(Child):
    def funzione(self):
        print('Posizione : Nephews.Funzione')
        super(Nephews, self).funzione()

obj=Nephews()
obj.funzione()
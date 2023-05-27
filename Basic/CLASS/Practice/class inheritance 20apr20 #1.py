class Person:
    counter = 0
    type = "persona"
    def __init__(self, name, age):
        Person.counter += 1
        self.name = name
        self.age = age
    def speak(self):
        print("my name is {} and i'm {} years old...".format(self.name, self.age))
    def eat(self, food):
        self.food = food
        print("{} eats {} ".format(self.name, self.food))
    def action(self):
        print("{} walks".format(self.name))
    @classmethod
    def istanze(cls):
        print(cls.counter)

class Baby(Person):
    type = "baby"
    def speak(self):
        print("onhya yah yah ")
    def nap(self):
        print("{} takes a nap".format(self.name))

p1=(Person('paolo',46))
p1.speak()
p1.eat("pasta aglio oglio")
p1.action()
print('')
b1=Baby("david", 1)
b1.speak()
b1.eat("baby meal")
b1.nap()
print('')
print(p1.type)
print(b1.type)
Person.istanze()
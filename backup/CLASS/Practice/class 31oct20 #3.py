

class Vehicle(object):
    kind='car'
    counter = 0
    def __init__(self, manufacture, model):
        self.manufacture = manufacture
        self.model = model
        Vehicle.counter += 1

car1=Vehicle('nissan', 'xentra')
car2=Vehicle('hyundai', 'tucson')
print(f'Vehicle Counter is {Vehicle.counter}') #2
print(f"vehicle kind: {Vehicle.kind} \t car1.kind: {car1.kind} \t car2.kind: {car2.kind}")
Vehicle.kind='suv'
print(f'Vehicle Counter is {Vehicle.counter}') #2
print(f"vehicle kind: {Vehicle.kind} \t car1.kind: {car1.kind} \t car2.kind: {car2.kind}")
# car1.kind='carro'

# print(car1.__dict__)
# class_state = car1.__dict__.copy()
# print(class_state)
print('-' * 60)
valoredict=car1.__dict__.copy()
print(type(valoredict))
print(car1.__dict__)
print(valoredict)
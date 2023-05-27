import sys
sys.tracebacklimit = 0


class Person:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, first_name, last_name, age) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._age = self.set_age(age)

    def set_age(self, age):
        if age < 18:
            raise ValueError('The age must be positive')
        return age

    def full_name(self):
        return ' '.join([self._first_name, self._last_name])

    @staticmethod
    def method_static():
        print('static method')

    # def __str__(self) -> str:
    #     retun f"{self._first_name} {self._last_name} {self._age}"


p1 = Person('John', 'Doe', 21)
print(p1.full_name())

from abc import abstractmethod
import logging

logging.basicConfig(level=logging.INFO)


class LoggedAgeAccess:
    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info("Accessing %r giving %r", "age", value)
        return value

    def __set__(self, obj, value):
        logging.info("Updating %r to %r", "age", value)
        obj._age = value


class User_instances:
    user_instances = []

    def __get__(self, instance, owner):
        print("self : ", self)
        print("instance : ", instance)
        print("owner : ", owner)
        self.__class__.__name__
        return self.user_instances

    def __set__(self, instance, value):
        print("self : ", self)
        print("instance : ", instance)
        print("value : ", value)
        instance._value = value


class User:
    # min_age = 18
    age = LoggedAgeAccess()  # Descriptor instance

    def __init__(self, first_name: str, last_name: str, age: int, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.id = id
        # self.__dict__["email"] = f"{self.id}@gmail.com"


u1 = User("john", "doe", 20, 1234)
print(u1.age)
# print(u1.min_age)
# x = u1.min_age = []
# print(x)

from typing import NewType, Type
from enum import Enum
from mypy import checker


T = NewType("T", str)
user: T
user = "John"

T = NewType("T", str)
user: T
user = "John"  # No error, 'user' is assigned a string value

# Uncomment the line below to see MyPy error
# user = 42  # Raises a MyPy error: "Incompatible types in assignment"


class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def start_date(day: Weekday):
    print(day)


class User:
    def __init__(self, name: str, age: int, start_day: Weekday) -> None:
        self.name = name
        self.age = age


u1 = User("a", 20, "Monday")


def user_info(user: User):
    print(user.name)


user_info(u1)

monday = Weekday.MONDAY
print(Weekday(1))

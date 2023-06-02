from typing import TypeVar

import sqlite3

CONNECTION = sqlite3.connect("./orm.db")
CURSOR = CONNECTION.cursor()


class Pet:
    all: list[PetType] = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(
        self: object, name: str, species: str, temperament: str, id: str = None
    ) -> None:
        self.name = name
        self.species = species
        self.temperament = temperament
        self.id = id
        Pet.all.append(self)


class Pet1:
    PET_TYPES = Enum("Pet_Type", ["dog", "cat", "rodent", "bird", "reptile", "exotic"])
    x = PET_TYPES.cat

    def __init__(
        self, name: str, pet_type: PetType, breed: str, temperament: str, id=None
    ) -> None:
        self.id = id
        self.name = name
        self.species = species
        self.temperament = temperament

    @classmethod
    def create_table():
        sql = """
        CREATE TABLE IF NOT EXISTS pets
            (id INTEGER PRIMARY KEY,
            name TEXT,
            species TEXT,
            breed TEXT,
            temperament TEXT)
    """

    @classmethod
    def drop_table():
        sql = """
          DROP TABLE IF EXISTS pets
        """
        res = CURSOR.execute(sql)
        return res
